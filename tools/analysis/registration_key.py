"""Mdir III 3.10 registration-number reconstruction from original MSET behavior.

Does not modify executables. Original MSET must create MDIR.REG on the target
DOS filesystem. See docs/REGISTRATION_ANALYSIS.ko.md for scope and evidence.
"""
import argparse
import json

# Conservative avoidance of the eight serial-pair entries in this exact MSET.
# The original also checks a name fingerprint; avoiding the pair is sufficient.
BLOCKED_PAIRS = {
    (54986,47902),(63588,54106),(17684,26304),(55228,47494),
    (44260,0),(15708,38010),(57208,31388),(31560,2002),
}
CHECKSUM_POSITIONS=(2,5,7,10,12)
SECONDARY_POSITIONS=(3,6,8,11,13)

def normalized(value):
    if any(ord(char)<32 or ord(char)>126 for char in value):
        raise ValueError('Use printable ASCII; the original asks for an English name')
    value=value.replace(' ','')
    if not value: raise ValueError('Name/password must not be empty after removing spaces')
    return value

def checksum(value):
    table=[0xCFA2]
    for index in range(1,256): table.append(table[-1]^(5*index))
    state=0xCF9E
    for index,byte in enumerate(value.encode('ascii'),1):
        state=(state^0xCD1A^((table[byte]<<((index%8)+1))&0xFFFF))&0xFFFF
        table[byte]=state
    return state

def generate(name,password):
    text=normalized(name)+normalized(password)
    if len(text)>255:raise ValueError('Combined normalized input exceeds Pascal short-string length')
    primary=checksum(text)
    if primary==0:raise ValueError('This input produces zero; choose a different password')
    secondary=next(n for n in range(65536) if (primary,n) not in BLOCKED_PAIRS)
    result=list('2500-0000-0000-0001')
    for index,digit in zip(CHECKSUM_POSITIONS,f'{primary:05d}'):result[index]=digit
    for index,digit in zip(SECONDARY_POSITIONS,f'{secondary:05d}'):result[index]=digit
    # A second gate in MDIR.REG creation checks the sum of the four groups.
    # Passing only the input dialog's checksum can delete the old REG instead.
    prefix=''.join(result)
    subtotal=sum(int(group) for group in prefix.split('-')[:3])
    suffix=next(n for n in range(10000) if ((subtotal+n)%9645)%1000==154)
    result[15:19]=f'{suffix:04d}'
    return ''.join(result)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--name',required=True)
    parser.add_argument('--password',required=True)
    args=parser.parse_args()
    try:serial=generate(args.name,args.password)
    except ValueError as error:parser.error(str(error))
    print(json.dumps({'name':args.name,'password':args.password,'serial':serial},indent=2))

if __name__=='__main__':main()
