"""Prepare an isolated original-Mdir observation run; never starts the emulator."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[2]
ASSET = 'dosbox-x-vsbuild-win64-2026.10.01-portable.zip'
URL = 'https://github.com/joncampbell123/dosbox-x/releases/download/dosbox-x-v2026.10.01/' + ASSET
SHA = '3c50915e63aefe35777d65ebb4391a06b4a2c2342e4c75cbee6bbda4c6916e33'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--name', default='baseline-replay', help='New run folder name, must not exist')
    parser.add_argument('--download', action='store_true', help='Allow downloading pinned official emulator when absent')
    args = parser.parse_args()
    if not args.name or any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_' for c in args.name):
        parser.error('Run name must contain only letters, digits, dash, underscore')
    if not (ROOT/'mdir/M.EXE').is_file(): parser.error('Place your original distribution in local mdir/ first')
    run = ROOT/'analysis-local'/args.name
    if run.exists(): parser.error('Run directory already exists; choose another --name')
    tools = ROOT/'analysis-local/tools'
    archive = tools/'dosbox-x.zip'
    if not archive.exists():
        if not args.download: parser.error('Emulator archive absent; use --download to allow official download')
        tools.mkdir(parents=True,exist_ok=True)
        urllib.request.urlretrieve(URL, archive)
    if hashlib.sha256(archive.read_bytes()).hexdigest() != SHA:
        raise SystemExit('Emulator archive SHA-256 differs from pinned release')
    executable = tools/'dosbox-x/bin/x64/Release/dosbox-x.exe'
    if not executable.exists():
        with zipfile.ZipFile(archive) as z:
            z.extractall(tools/'dosbox-x')
    run.mkdir(parents=True)
    drive=run/'drive'
    (drive/'MDIR').mkdir(parents=True)
    (drive/'TEMP').mkdir()
    (drive/'TEST/SRC').mkdir(parents=True)
    (drive/'TEST/DST').mkdir()
    (run/'evidence').mkdir()
    (run/'captures').mkdir()
    for source in (ROOT/'mdir').iterdir():
        if source.is_file() and source.name.lower() != 'serial.txt': shutil.copy2(source, drive/'MDIR'/source.name)
    for name,content in [('SRC/ALPHA.TXT',b'alpha-original'),('SRC/BETA.TXT',b'beta-original'),
                         ('SRC/GAMMA.DAT',b'gamma-data'),('DST/ALPHA.TXT',b'alpha-existing')]:
        (drive/'TEST'/name).write_bytes(content)
    config=f'''[sdl]
fullscreen=false
output=surface
autolock=false
usescancodes=false
showmenu=true
titlebar=Mdir P0 isolated baseline
[dosbox]
machine=svga_s3
memsize=16
working directory option=config
captures={run/'captures'}
hostkey=ctrlalt
ime=false
mcp_server=58991
[cpu]
core=normal
cycles=fixed 10000
[dos]
ver=6.22
lfn=false
automount=false
automountall=false
automount drive directories=false
keyboardlayout=us
[autoexec]
@echo off
mount c "{drive}" -freesize 64
c:
set PATH=C:\\MDIR;Z:\\
set TEMP=C:\\TEMP
cd \\TEST\\SRC
C:\\MDIR\\M.EXE /X
'''
    (run/'baseline.conf').write_text(config,encoding='utf-8')
    print(json.dumps({'run_directory':str(run),'executable':str(executable),'config':str(run/'baseline.conf'),
                      'started':False},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
