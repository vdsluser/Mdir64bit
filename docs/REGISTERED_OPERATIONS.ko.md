# 등록판 파일·주석·MCD·메모리 실행 조사

조사일: 2026-10-21. 생성 번호로 등록한 FAT12 기준 이미지의 복사본을 C:/D:로 마운트했다. DOSBox-X 2026.10.01, DOS 6.22, XMS/EMS 사용 환경이다. 파일 작업은 `M.EXE /X`로 실행했고 풀메모리 실험에서만 `/X`를 제거했다. 원본 자료와 기준 이미지는 보존했다.

이 보고서는 [등록 분석](REGISTRATION_ANALYSIS.ko.md)과 [VV 조사](VV_RUNTIME_FINDINGS.ko.md)의 후속이다. 미등록판과 동일 입력으로 대조한 실험은 아니므로 등록판에서 성공했다는 사실만으로 판본 간 차이 전체를 확정하지 않는다.

## 파일 작업과 주석

입력은 C:\CASE의 COPY.TXT/MOVE.TXT/RENAME.TXT/DELETE.TXT와 각각의 합성 ASCII 주석이다. D:\DST에는 KEEP.TXT와 기존 주석을 두었다. 작업 종료 후 에뮬레이터를 닫고 FAT 파일시스템을 읽어 비교했다.

| 동작 | 결과 |
|---|---|
| COPY.TXT를 D:\ 루트로 복사 | 원본 유지, 대상 내용 동일, D:\DESCRIPT.ION에 `COPY.TXT copy-comment` 생성 |
| MOVE.TXT를 D:\DST로 이동 | 원본 파일과 주석 항목 제거, 대상 내용 동일, 대상 주석 추가 |
| RENAME.TXT→RENAMED.TXT | 파일 내용 유지, 주석 키를 새 이름으로 변경 |
| DELETE.TXT 삭제 | 파일과 주석 항목 제거. [삭제 확인](evidence/2026-10-21/registered-03/r013-delete.txt)과 [완료 화면](evidence/2026-10-21/registered-03/r014-delete-finish.txt) 기록 |
| 기존 대상 보존 | KEEP.TXT 내용과 `keep-comment` 유지 |

주석 항목 순서는 달라질 수 있었다. 파일명-주석 대응과 내용으로 판정하고 파일 전체의 문자열 순서만으로 실패를 판단하지 않는다. 원본 주석 파일은 처음에는 일반 파일로 만들었으며, 작업 후 목록에서 숨겨졌다. 이번 검증은 내용 중심이고 속성 비트 전체의 규칙을 확정하지 않는다.

## MCD 폴더 작업

TREE에는 INNER.TXT, DESCRIPT.ION, SUB\DEEP.TXT를 두었다. 부모 C:\CASE\DESCRIPT.ION에는 `TREE tree-comment`도 넣었다.

- **F5 같은 드라이브 복사**: C:\CASE\TREE→C:\TEST\DST\TREE. 내부 두 파일과 내부 주석 파일의 바이트가 기준과 같았다. [트리 표시](evidence/2026-10-21/registered-03/r021-dir-copied.txt).
- **F4 교차 드라이브 이동**: C:\CASE\TREE→D:\DST\TREE. 원본 디렉토리가 없어지고 대상 내부 파일·주석이 기준과 같았다. [드라이브 선택](evidence/2026-10-21/registered-03/r023-dir-move-drive.txt), [완료](evidence/2026-10-21/registered-03/r024-dir-moved.txt).
- **자기 자신을 대상으로 복사 시도**: `Cannot COPY/MOVE tree into itself`로 거부했다. [오류 기록](evidence/2026-10-21/registered-03/r018-copy-action.txt).
- **폴더 자체의 부모 주석**: 이동 후에도 C:\CASE에 `TREE tree-comment`가 남았고 D:\DST에는 추가되지 않았다. 폴더 내부의 DESCRIPT.ION 복사와 폴더 자체의 주석 이관은 서로 다르다.

이번 F5 대상 선택 상태에서는 F3 안내가 비어 있고 F3 입력으로 드라이브 선택창을 열지 못했다. 반면 F4에서는 F3로 D:를 선택했다. 설명서의 교차 드라이브 복사 지원 문구와 차이가 있으므로 **MCD 교차 드라이브 복사는 미해결**로 남긴다. 원인을 등록 상태만으로 단정하지 않는다. [등록 표시](evidence/2026-10-21/registered-03/r026-about.txt)는 같은 세션에서 확인했다.

폴더 삭제 확인을 실수로 열었던 경우에는 취소했고, 실제 삭제는 DELETE.TXT만 대상으로 했다. 취소·선택 오류를 성공 사례로 집계하지 않는다.

## 풀메모리 실행과 `/X`

원본 M.DOC L899~900은 `/` 명령과 `?` 명령을 메모리 실행 방식으로 구분하고, L311은 `/X`가 풀메모리 실행을 끈다고 설명한다. MSET.DOC L250은 `%B`를 메모리 점유 없이 실행하는 등록판 변수로 설명한다.

측정 명령은 DOSBox-X의 `MEM /C`이며 출력을 가상 C: 파일로 저장했다. 이 수치는 에뮬레이터의 모듈 보고이고 Windows 프로세스 메모리 측정이 아니다.

| 실행 조건 | 관찰 |
|---|---|
| `M.EXE /X` → `/` → `MEM /C > C:\SWAP.TXT` | Mdir로 복귀. MEM에 M 모듈 240바이트(일반 160+상위 80), 최대 실행 가능 일반 메모리 619808바이트 |
| `M.EXE /X` → `/` → `MEM /C %B > C:\FULLX.TXT` | Mdir로 복귀. 위와 동일한 M 모듈·가용 메모리. 이 조건에서는 `%B`가 `/X`를 해제하지 않음 |
| `M.EXE` → `/` → `MEM /C %B > C:\FULL.TXT` | Mdir 종료, 즉시 FULL.TXT가 생기지 않음. 루트 `_M_.BAT`와 TEMP의 `(M).BAT` 생성 |
| 생성된 `_M_.BAT`를 다음 에뮬레이터 실행에서 호출 | 명령 수행 후 Mdir 화면 복귀. MEM에 M 모듈 없음, 최대 실행 가능 일반 메모리 622224바이트. 이후 `(M).BAT`는 없어짐 |

TEMP 배치에 기록된 명령은 `MEM /C  > C:\FULL.TXT`로 `%B`가 제거되어 있었다. 생성 배치를 직접 호출한 실험은 **같은 세션의 자동 연속 실행 검증이 아니다**. M.EXE 단독 호출과 배치 실행 경로를 구분해야 하며, 일반 DOS 셸에서의 자동 재진입 경로는 추가 분석 대상이다.

가용 일반 메모리 차이는 2416바이트이고 M 모듈의 240바이트와 같지 않다. 스와핑 쪽에는 COMMAND 인스턴스도 하나 더 있어 차이 전체를 Mdir 본체 크기로 해석하지 않는다. [스와핑 출력](evidence/2026-10-21/registered-03/swap-mem.txt), [/X와 %B 출력](evidence/2026-10-21/registered-03/fullx-mem.txt), [배치 실행 출력](evidence/2026-10-21/registered-03/full-mem.txt).

## 검증 범위와 전환 반영

[파일 검증 기록](evidence/2026-10-21/registered-03/file-verification.json)에 파일·주석·등록 파일·임시 배치의 16개 검사를 남겼다. 합성 주석은 원문과 해시를 공개했으며 원본 실행 파일·등록 파일·메모리 덤프는 공개하지 않았다. [ID별 상태](evidence/2026-10-21/registered-03/status.json)는 기존 기능의 부분 관찰을 보완한다. 원본 폴더와 ZIP의 37개 지문은 별도로 기존 인벤토리에 대조했다.

Windows판에서는 파일 작업과 주석 갱신을 한 작업 결과로 묶되, 폴더 자체 주석과 내부 주석을 별도로 처리해야 한다. 실패·취소·대상 기존 주석·동명이름 충돌은 후속 검증이 필요하다. DOS의 배치 재진입/XMS 스와핑을 그대로 옮기는 대신 자식 프로세스의 작업 경로·인자·종료 코드와 부모 UI의 수명 정책을 P1/P5에서 정한다.

다음 조사 순서는 MF/MCOPY의 취소·오류·Format OFF이며, MCD 교차 드라이브 복사와 풀메모리 자동 재진입은 미해결 목록에 유지한다. P0 전체 검증이 끝난 것은 아니다.
