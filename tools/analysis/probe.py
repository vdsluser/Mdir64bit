"""Local DOSBox debugger harness: BIOS key queue + VGA text evidence."""
import json, urllib.request, pathlib, time, sys, struct, os
ROOT=pathlib.Path(os.environ.get('MDIR_ANALYSIS_DIR', str(pathlib.Path(__file__).resolve().parents[2]/'analysis-local')))
OUT=ROOT/'evidence'
OUT.mkdir(exist_ok=True)

def command(*commands):
    request=urllib.request.Request('http://127.0.0.1:58992',data=json.dumps({'commands':commands}).encode(),headers={'Content-Type':'application/json'})
    result=json.load(urllib.request.urlopen(request,timeout=30))
    if not result['ok'] or any(' ERR' in lines[0] for lines in result['output']):
        raise RuntimeError(result)
    return result

def capture(case):
    command('BREAK',f'EXEC MEMDUMPBIN 40:0 100 {OUT/case}.bda',f'EXEC MEMDUMPBIN B800:0 8000 {OUT/case}.vga','EXEC RUN')
    bda=(OUT/(case+'.bda')).read_bytes()
    video=(OUT/(case+'.vga')).read_bytes()
    cols=struct.unpack_from('<H',bda,0x4a)[0]
    rows=bda[0x84]+1
    page=struct.unpack_from('<H',bda,0x4e)[0]
    text='\n'.join(video[page+i*cols*2:page+(i+1)*cols*2:2].decode('cp437').rstrip() for i in range(rows))
    (OUT/(case+'.txt')).write_text(text,encoding='utf-8')
    return text

KEYS={'esc':0x011b,'enter':0x1c0d,'f1':0x3b00,'f10':0x4400,'f11':0x8500,'f12':0x8600,'up':0x4800,'down':0x5000,'left':0x4b00,'right':0x4d00,'home':0x4700,'end':0x4f00,'space':0x3920,'alt-c':0x2e00,'alt-m':0x3200,'alt-r':0x1300,'alt-k':0x2500,'alt-v':0x2f00,'alt-f':0x2100,'alt-n':0x3100,'alt-e':0x1200,'alt-s':0x1f00,'alt-t':0x1400,'alt-u':0x1600,'alt-x':0x2d00,'alt-1':0x7800,'alt-2':0x7900,'ctrl-f12':0x8a00,'alt-enter':0x1c00,'ctrl-z':0x2c1a,'alt-i':0x1700}

def keys(values):
    # Pause before replacing only the BIOS keyboard ring; no executable bytes are changed.
    for value in values:
        words=[ord(c) for c in value[5:]] if value.startswith('text:') else [int(value[4:],16) if value.startswith('hex:') else KEYS[value]]
        for pos in range(0,len(words),14):
            chunk=words[pos:pos+14]
            data=b''.join(struct.pack('<H',w) for w in chunk)
            ptr=struct.pack('<HH',0x1e,0x1e+len(data))
            command('BREAK','EXEC SM 40:1e '+' '.join(f'{v:02x}' for v in data),'EXEC SM 40:1a '+' '.join(f'{v:02x}' for v in ptr),'EXEC RUN')
            time.sleep(.25)

if __name__=='__main__':
    case=sys.argv[1]
    values=sys.argv[2:]
    if values: keys(values)
    time.sleep(.2)
    text=capture(case)
    log=OUT/'bios-actions.jsonl'
    with log.open('a',encoding='utf-8') as f: f.write(json.dumps({'case':case,'keys':values,'time':time.time(),'method':'BIOS keyboard queue via debugger'},ensure_ascii=False)+'\n')
    print(text)

