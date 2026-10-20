"""Generate local-evidence metadata and the documentation-based feature ledger."""
from pathlib import Path
import hashlib
import re
import struct

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'mdir'
DOCS = ROOT / 'docs'
texts = {p.name: p.read_bytes().decode('cp949', errors='replace').splitlines()
         for p in SOURCE.iterdir() if p.suffix.upper() in {'.DOC', '.HLP', '.BAT'}}

def ref(name, needle):
    for i, line in enumerate(texts[name], 1):
        if needle in line:
            return f'`{name}:L{i}`'
    raise ValueError((name, needle))

def md(s):
    return s.replace('|', '\\|').replace('\x1a', '')

inventory = ['# 원본 파일 인벤토리', '', '2026-10-20 로컬 파일을 직접 읽어 생성. 경로는 원본 폴더 기준이다. SHA-256은 내용 식별용이며 정품/무변조/권한을 보증하지 않는다.', '',
             '원본 자료의 전문과 등록정보는 공개하지 않는다. `serial.txt`는 존재·크기·해시만 조사했다.', '',
             '| 파일 | 바이트 | SHA-256 | 구조 관찰 |', '|---|---:|---|---|']
for p in sorted([ROOT/'mdir.zip', *SOURCE.iterdir()], key=lambda p:p.name.lower()):
    if not p.is_file():
        continue
    b = p.read_bytes()
    kind = '미분석 데이터/지원 파일'
    if b[:2] == b'MZ':
        ptr = struct.unpack_from('<I', b, 60)[0] if len(b) >= 64 else 0
        pe = ptr >= 64 and ptr + 4 <= len(b) and b[ptr:ptr+4] == b'PE\0\0'
        kind = 'MZ; PE 확인' if pe else 'MZ; 유효한 PE 서명 미확인'
    elif p.suffix.lower() == '.com': kind = 'COM 확장자; 명령/기능 미분석'
    elif p.suffix.lower() == '.doc': kind = '일반 텍스트 설명서; 한국어 CP949로 읽기 가능'
    elif p.suffix.lower() == '.hlp': kind = '텍스트 도움말; 한글 코드별 별도 파일'
    elif p.suffix.lower() == '.zip': kind = '원본 배포 ZIP'
    inventory.append(f'| {p.name} | {len(b)} | `{hashlib.sha256(b).hexdigest()}` | {kind} |')
inventory += ['', '## 자료 해석 범위', '',
              '- CP949 디코딩은 한국어 문서 조사에 사용한 방법이다. 파일마다 완성형/조합형/이진 포맷이 다를 수 있으므로 모든 파일의 인코딩을 확정한 것은 아니다.',
              '- MZ만으로 16비트 여부·컴파일러를 단정하지 않는다. 실행 검증 및 추가 구조 분석이 필요하다.',
              '- 소스 확장자 C/C++/ASM/PAS 등은 현재 제공 폴더에서 발견되지 않았다.',
              '- MOUSE.COM, HE.COM, DSCMAN.EXE는 파일명이 기능을 확정하는 근거가 아니다.',
              '- 원본 ZIP과 폴더가 완전히 같은지는 아래 멤버 비교 결과를 따른다.', '']
import zipfile
with zipfile.ZipFile(ROOT/'mdir.zip') as z:
    names = []
    mismatch = []
    for member in z.infolist():
        if member.is_dir(): continue
        name = Path(member.filename.replace('\\', '/')).name
        names.append(name)
        local = SOURCE / name
        if not local.exists() or local.read_bytes() != z.read(member): mismatch.append(name)
    extra = sorted(p.name for p in SOURCE.iterdir() if p.is_file() and p.name not in names)
    inventory.append(f'ZIP 파일 멤버 {len(names)}개; 같은 파일명으로 비교한 내용 불일치/누락 {len(mismatch)}개; 폴더의 추가 파일 {len(extra)}개.')
    inventory.append(f'불일치/누락: {", ".join(mismatch) or "없음"}. 추가: {", ".join(extra) or "없음"}.')
(DOCS/'ORIGINAL_INVENTORY.ko.md').write_text('\n'.join(inventory)+'\n', encoding='utf-8')

# One row is a testable behavior group, not a claim of exhaustive runtime coverage.
raw = r'''
UI|도움말과 메뉴|F1; F12/Ctrl-Ins|도움말; 정보 상자; 연결 명령 목록; 한글 코드 메뉴|M.DOC|풀다운 메뉴에서만|P2
UI|상태선 안내|Alt/Ctrl|수정키에 따른 단축키 안내; 경로·용량·선택 합계|M-K.HLP|간략한 명령키|P2
UI|목록 열 구성|Alt-0..6|1~6열과 자동 구성; 열별 표시 항목|M.DOC|가로 한줄당|P2
UI|화면 구성|Alt-=; Alt-역슬래시|크기 고정/자동, 구분선·스크롤·화면 행 수|MSET.DOC|세로크기고정|P2
UI|파일 표시|Alt-A/Z/G/L/F|속성·숨김·실행파일 필터·소문자·패턴 필터|M-K.HLP|파일필터|P2
UI|정렬|Alt-N/E/S/T/B/Q/O/-|이름·확장자·크기·날짜·색·실행 우선·정렬 해제·역순|M.DOC|Alt-Q :|P2
UI|정렬 동률 규칙|MSET|기준별 2차/3차 정렬과 역순의 적용 범위|MSET.DOC|1차,2차,3차|P2
NAV|커서 이동|방향/Home/End/Pg 및 Ctrl|파일·화면·디렉토리 단위 이동|M.DOC|^Home / ^End|P2
NAV|문자 빠른 검색|문자/BS/Ctrl-L/Esc|검색 문자열 편집·반복·취소; 확장검색 설정|M.DOC|빨리찾기수정|P2
NAV|드라이브/상위/루트|Shift-문자; [ ]; .; 역슬래시|드라이브 이동과 부모/루트 복귀|M-K.HLP|드라이브명으로 선택막대|P2
NAV|작업 디렉토리|Alt-W/Ctrl-W|작업 대상 지정·현재 경로와 교환·해제|M.DOC|작업디렉토리를 닫|P4
NAV|이전 대상 복귀|Ctrl-BS|이전 탐색 경로 또는 마지막 파일작업 대상으로 이동|M.DOC|이전 디렉토리로 간다|P4
MOUSE|마우스 입력|좌/우/중간/양쪽 버튼|파일창 좌=이동/Enter, 우=선택, 중간/양쪽=Tab; 페이지·펑션키·상태선 영역|M.DOC|중간,양쪽:Tab|P2
MOUSE|상태선 명령|크기/속성/볼륨 클릭|복사·속성·볼륨 변경; 열·정렬·숨김·필터 영역 확인|M.DOC|상태라인 속성표시부분 클릭|P2
SEL|선택 집합|Space/Alt-U/숫자패드 * + - /|단일·전체·반전·패턴·동일 확장자; 키별 모순 조사|M-K.HLP|파일명으로 파일선택|P2
SEL|선택 순서|Alt-1|선택 순서 표시와 작업 후 선택 해제|M.DOC|선택된 순서는|P2
FILE|복사|Alt-C/Ins|파일·폴더·다중 선택; Ins/Del 설정별 단일 대상|M.DOC|《복사》|P3
FILE|충돌 처리|복사 대화상자|덮어쓰기·모두·모두 건너뛰기·건너뛰기·이름 변경·새 파일만|M.DOC|OverWrite(덮어씀)|P3
FILE|부족 용량/부분 실패|복사/이동; Esc|사전 용량 안내·매체 교체·실패 후 계속·완료분만 선택 해제|M.DOC|복사가 끝난 파일만|P3
FILE|이동|Alt-M|동일 드라이브 이동과 교차 드라이브 복사/원본 삭제|M.DOC|《이동》|P3
FILE|이름 변경|Alt-R|파일/폴더·복수 와일드카드·예약 이름 거부|M.DOC|《이름》|P3
FILE|삭제|Alt-D/Del|보호 속성/비어있지 않은 폴더 추가 확인; 루트 삭제 3회 확인; 대상 설정|M.DOC|《삭제》|P3
FILE|폴더 생성|Alt-K|경로 입력·중복·긴 이름|M-K.HLP|디렉토리 만들기|P3
FILE|속성 변경|Ctrl-Z; A/R/H/S; Enter/End|속성 토글; 현재 파일 저장 또는 이후 전부 저장|M.DOC|현재이후 파일전부|P3
FILE|문서 보기/인쇄|Alt-V/Alt-P|외부 뷰어 연동; 텍스트 인쇄 대상과 실패|M-K.HLP|텍스트파일 인쇄|P6
DISK|볼륨명|Ctrl-V|드라이브 볼륨 표시·이름 변경|M-K.HLP|볼륨명바꾸기|P8
DISK|포맷/복제/파킹|Ctrl-F/C/P|외부 프로그램 또는 내장 파킹 호출; 디스크 작업 구분|M-K.HLP|디스크 포맷|P8
TREE|MCD 탐색|F10; 방향키/Home/End/Pg|트리 선택·폴더 검색·드라이브 전환|M.DOC|디렉토리 관리기(MCD)|P4
TREE|MCD 재검색/캐시|F2/F3|트리 재구축·현재 경로 누락 시 재검색·CD/LAN별 캐시|M.DOC|자동 재검색기능은|P4
TREE|MCD 폴더 작업|F4..F8|가지 이동·복사·이름 변경·생성·하위 포함 삭제|M.DOC|F4     : 디렉토리 이동|P4
TREE|MCD 크기/정렬|F9/Alt-N|하위 폴더·파일 수·용량 통계, 이름 정렬|M.DOC|Number of SubDir|P4
QCD|즐겨찾기|F11/Shift-F1..F10|10개 경로 등록·삭제·이동·MCD에서 선택·오류 경로|M.DOC|QCD에 디렉토리를 지정|P4
RUN|실행 방식|Enter/Tab/Ctrl-Enter/Shift-Tab|직접/연결 실행·사전 옵션 편집·스와핑 차이|M.DOC|Tab       : 스와핑하여|P5
RUN|종료 후 실행|Alt-Space/Ctrl-Space|셸 종료 후 실행·명령 편집·대체 단축키|M.DOC|Alt-SPACE : M3가 종료|P5
RUN|28개 펑션키|F2..9; Ctrl/Alt-F1..10|단일 명령 또는 복수 명령 선택 메뉴|M.DOC|여러개를  지정한|P5
RUN|확장자 연결|Enter/Tab; MSET|압축 Enter 탐색 우선과 Tab 외부 실행 차이|M.DOC|tab키를 사용해야|P5
RUN|마지막 실행 화면|Ctrl-T|종료한 프로그램/압축 작업 화면 확인|M.DOC|이전에 실행한|P5
CMD|명령줄|일반 / 또는 ?|명령 입력; 배치/스와핑; 실행후 정지; 모든 변수 사용|M.DOC|슬래쉬(/)키는|P5
CMD|입력 편집/삽입|Ctrl-Y/Home/End/BS/Del/Ins|초기값 수정·대체·취소; 파일/경로/QCD 삽입|M.DOC|문장입력(String input)|P5
CMD|명령 이력|위/아래; PgUp/PgDn/F12|이전 명령·메뉴·수정 후 실행·M.HIS 저장|M.DOC|히스토리 메뉴|P5
CLI|실행 인자|M [옵션] [파일] [경로]|패턴·유사 경로 이동·옵션 연결·마지막 옵션 우선|M.DOC|동일한 항목이 여러번|P5
CLI|표시/정렬 옵션|/? /1..6 /N/E/S/T /D/L/A/Z /=|도움말·열·정렬·필터·표시 설정|M.DOC|선택사항(Command line|P5
CLI|환경 옵션|/J/K/! /V/v /+ /X /m|코드/화면/키속도/메모리/색상표; 대소문자 차이|M.DOC|M /m|P5
CLI|시작/종료 모드|/C/c /P/p /R|MCD 시작·종료·DIR 대체·트리 갱신|M.DOC|M /cp|P5
CLI|BAT 래퍼|MDIR.BAT/MCD.BAT|각각 /p, /cp 및 최대 4개 인자 전달|MDIR.BAT|%1|P5
DESC|주석 편집|Alt-Enter|단일·다중·수정·삭제; DESCRIPT.ION 호환|M.DOC|주석(Description)|P4
DESC|주석 동반|복사/이동/이름 변경/삭제|파일 작업시 주석 유지; 등록판 제한 조사|M.DOC|따라다닌다|P4
DESC|주석 표시/긴 이름|Ctrl-Q/Alt-1/MSET|자동·상단·1열 표시; Win95 긴 이름 변환·매체 차이|M.DOC|Ctrl>-<Q|P4
ARC|압축 인식|Enter|LZH/ARJ/ZIP/SQZ/OMP/RAR/UC2/ARC/ICE/ZOO/HPK; SFX/틀린 확장자|M-K.HLP|LZH, ARJ, ZIP|P7
ARC|내부 탐색|Enter/Esc/./루트/Alt-전환키|트리 재현·평탄 목록·경로 주석·내부 선택|M.DOC|디렉토리 재현기능 ON/OFF|P7
ARC|생성/추가|Ctrl-A|기본 형식·확장자 지정·기존 압축에 추가|M.DOC|Ctrl-A : 압축파일 만들기|P7
ARC|압축 후 원본 삭제|Ctrl-M|SQZ/UC2는 Add와 같은 동작이라는 예외|M.DOC|SQZ와 UC2|P7
ARC|추출/내부 삭제|Ctrl-X/Alt-C/Alt-D|다중 형식 일괄 추출·선택 추출·내부 삭제|M.DOC|Ctrl-X,Alt-C|P7
ARC|내부 파일 실행/보기|Enter/Tab/Alt-V/펑션키/명령|임시 추출·외부 도구·실행 복귀·임시 정리|M.DOC|압축파일 처리|P7
FIND|파일 검색|Alt-I/MFF|드라이브·모든 비플로피 드라이브·최대20 패턴|MFF.DOC|최대 20개|P6
FIND|검색 취소|Esc|중단 확인·현재 결과 유지 또는 계속 검색|MFF.DOC|찾는도중 Esc|P6
FIND|결과 탐색/정렬/선택|Alt-N/E/S/T/A/O; Ctrl-오른쪽; Space|정렬·축약 표시·빠른 검색·다중 선택|MFF.DOC|☞ 정렬|P6
FIND|결과에서 작업|Enter/Alt-D/V/Tab|파일 위치로 복귀·삭제·뷰어·실행|MFF.DOC|해당 파일이 있는|P6
VIEW|코드 인식|VV; F9/Alt-C/Shift-F9|조합형·완성형·영문·이진·한자 변환|VV.DOC|조합형,  완성형|P6
VIEW|문서 이동|방향/Pg/Home/End/Ctrl/Space/Enter|행·페이지·수평·문서 처음/끝 이동|VV.DOC|화면이동|P6
VIEW|문서 표시|F11/1..0/F8/F4|줄바꿈·탭 크기·갱신 방법·상태줄|VV.DOC|워드랩|P6
VIEW|색상/글꼴/해상도|F5/F6/Shift/Tab/Alt-F/숫자패드 + -|한글/영문 글꼴 각9개·한자 글꼴·색상·그래픽 모드|VV.DOC|최대 9개|P6
VIEW|설정 저장|F2|색상·글꼴·표시·해상도·줄바꿈을 실행파일에 보존|VV.DOC|실행파일에 기록|P6
VIEW|메뉴/종료/화면보호|F1/F12/Ctrl-Ins/Esc/Alt-X/숫자패드 *|도움말·팝업·양쪽마우스 종료·즉시 보호·CLI 옵션|VV.DOC|메인화면|P6
FORMAT|플로피 포맷|MF; Ins/F3..7/Esc|용량·퀵/DOS 방식·검사·방향·중단·에러|MF.DOC|Format           Ins|P8
COPY|디스켓 복제|MCOPY; Ins/Alt-R/W/F3..5|읽기·버퍼 쓰기·원본/대상·최대9999 사본·CLI|MCOPY.DOC|9999|P8
COPY|포맷 옵션 모순|MCOPY Format|미지원 표기와 후속 설명 충돌; 실행 확인 필요|MCOPY.DOC|아직 지원않음|P8
LEGACY|화면보호|Ctrl-S; 대기|내장·외부 보호·마우스 복귀·대기시간|M.DOC|Ctrl-S    -|P8
LEGACY|한글 변환|HCONV|완성형/조합형·이야기 특수문자·한자 변환; CLI 미조사|MUPDATE.DOC|HCONV|P6
LEGACY|추가 실행파일|HE.COM/DSCMAN.EXE/MOUSE.COM|역할·인자·호출 관계 확인 필요|M.DOC|파일목록|P0
LEGACY|구형 실행환경|XMS/EMS/DISK/PIF/한글BIOS/LAN|스와핑·Win95 키 충돌·긴 이름·드라이버 의존|M.DOC|SPAWNO|P0
'''
catalog = ['# 문서 기반 기능·설정 추적표', '',
           '작성: 2026-10-20. 모든 행의 근거 수준은 **DOC(문서)**, 원본 실행 상태는 **미검증**이다. 제품 구현 상태는 전부 미착수다. 번호는 문서 변경에도 유지한다. 자동 생성 결과에 새로 발견한 기능을 수동 병합할 때 기존 ID를 재번호화하지 않는다.', '',
           '근거는 로컬 원본을 CP949로 디코딩하고 줄바꿈 기준으로 센 1기반 줄 번호다. 원본 전체 텍스트는 공개 저장소에 올리지 않는다. 행은 검증 가능한 동작 묶음이며 테스트 사례는 더 세분화한다.', '',
           '## 주요 기능', '', '| ID | 기능 | 진입/키 | 확인할 동작 | 로컬 근거 | 단계 | 실행 |', '|---|---|---|---|---|---|---|']
counts = {}
for line in raw.strip().splitlines():
    cat, title, key, behavior, source, needle, phase = line.split('|')
    counts[cat] = counts.get(cat, 0)+1
    catalog.append('| '+' | '.join(map(md,[f'{cat}-{counts[cat]:03}', title, key, behavior, ref(source,needle), phase, '미검증']))+' |')
catalog += ['', '## MSET 전체 점선 메뉴 항목', '',
            '동봉 MSET.DOC의 점선으로 정의된 메뉴 항목을 전수 추출했다. 메뉴명 자체를 추적하며 하위 옵션·실제 화면의 추가 항목은 P0에서 확인한다. 원본의 위험한 설정도 조사 목록에 보존하지만 Windows판 채택을 뜻하지 않는다.', '',
            '| ID | 메뉴 그룹 | 설정 항목 | 로컬 근거 | 단계 | 실행 |', '|---|---|---|---|---|---|']
group='미분류'
settings=0
for i,line in enumerate(texts['MSET.DOC'],1):
    if '▷ "' in line and '메뉴' in line:
        group=line.split('"')[1]
    match=re.match(r'^\s{6}([^ .│└┌].*?)\.{2,}',line)
    if match:
        settings += 1
        catalog.append(f'| SET-{settings:03} | {group} | {md(match.group(1).strip())} | `MSET.DOC:L{i}` | P4（구형 옵션 P8） | 미검증 |')
catalog += ['', '## 명령 변수 전체 표 및 이력 보완', '',
            '| ID | 변수 | 문서상 의미 | 근거 | 단계 | 실행 |', '|---|---|---|---|---|---|']
variables=0
for i,line in enumerate(texts['MSET.DOC'],1):
    if '│' not in line: continue
    cells=line.split('│')
    if len(cells)<4: continue
    token=cells[1].strip()
    if token and token[0] in '!%,':
        variables+=1
        catalog.append(f'| VAR-{variables:03} | `{token}` | {md(cells[2].strip())} | `MSET.DOC:L{i}` | P5 | 미검증 |')
variables+=1
catalog.append(f'| VAR-{variables:03} | `%L` | 긴 파일명 반환; 업데이트 이력에서 보완 | {ref("MUPDATE.DOC", "변수 \"%L\"")} | P5 | 미검증 |')
total=sum(counts.values())+settings+variables
catalog += ['', '## 커버리지', '',
            f'현재 {sum(counts.values())}개 주요 동작 묶음 + {settings}개 MSET 메뉴 항목 + {variables}개 변수 항목 = **{total}개 추적 행**이다. 중복 영역을 포함하므로 독립 기능 수로 해석하지 않는다. 실행 관찰 완료는 **0개**다.', '',
            '문서·도움말·이력·팁·Q&A를 교차 조사했지만, 문서 전문의 모든 문장을 자동으로 기능화한 것은 아니다. MSET 하위 메뉴 값·마우스 영역별 동작·도구별 상세 CLI·문서에 없는 동작은 P0에서 추적표에 추가한다.', '',
            '마우스 좌/우/동시 버튼 및 상태선 클릭은 별도 입력 방식이다. UI/NAV/SEL/FILE/TREE/VIEW별 사례에 연결하고 키보드와 같은 결과인지 확인한다. 원본 M.DOC의 마우스 절 및 VV.DOC의 마우스 설명을 근거로 삼는다.']
(DOCS/'FEATURE_CATALOG.ko.md').write_text('\n'.join(catalog)+'\n',encoding='utf-8')
print(f'Generated inventory and catalog: {total} rows ({sum(counts.values())} behavior, {settings} settings, {variables} variables)')
