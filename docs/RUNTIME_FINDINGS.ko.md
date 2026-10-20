# P0 원본 실행 조사 — 1차 결과

원본 관찰: 2026-10-20 · 결과 정리: 2026-10-21 (Asia/Seoul). **P0 진행 중**이며 전 기능 검증 완료가 아니다. 최초 문서 원장의 173개 행에 대한 현재 상태는 [실행 추적표](evidence/2026-10-20/runtime-status.json)를 따른다. 한 행의 일부 사례를 확인했다고 전체 기능을 통과로 바꾸지 않았다.

## 확인한 원본과 환경

- 원본 시작 화면: **Mdir III 3.10 / Unregistered version / Personal use only**.
- 원본 ZIP 및 `mdir/` 36개 파일의 해시는 조사 전후 일치한다. `serial.txt`는 실행 환경에 복사하지 않았다.
- 공식 [DOSBox-X 2026.10.01 릴리스](https://github.com/joncampbell123/dosbox-x/releases/tag/dosbox-x-v2026.10.01)의 Windows x64 휴대용 패키지를 사용했다. 설치 프로그램이나 시스템 PATH 변경은 사용하지 않았다.
- DOSBox-X 내장 DOS, 보고 버전 6.22, LFN 비활성, VGA/S3, CPU normal/fixed 10000, 메모리 16MB, 키보드 us, IME 비활성이다. **실제 MS-DOS 6.22 설치본이나 Windows 95 시험이 아니다.**
- C:에는 `analysis-local/drive`만 연결했다. A:/B:는 에뮬레이터의 가상 플로피이며 이미지나 실제 드라이브를 연결하지 않았다. Z:는 DOSBox-X의 내장 드라이브다.
- `/X`로 풀메모리 배치 실행을 끄고 시작했다. 제공 CFG의 설정값을 사용했으며, 조사 도중 작업 복사본에서 24시간 표시를 저장했다. 이는 배포 초기 기본값에 대한 시험이 아니다.
- 파일 크기·내용·해시·속성은 Windows 호스트에서 직접 확인했다. 큰 파일·긴 경로·실제 장치·네트워크·성능·한글 IME는 이번에 검증하지 않았다.

환경 해시와 파일 변화는 [환경 기록](evidence/2026-10-20/environment.json), 재현 입력은 [키 입력 기록](evidence/2026-10-20/actions.jsonl)을 따른다.

재현용 준비 도구·BIOS 입력 도구와 한계는 [분석 도구 안내](../tools/analysis/README.ko.md)를 따른다. 원본 실행 파일을 배포하지 않으며 로컬 원본이 있어야 한다.

## 관찰 방법과 한계

초기에는 Windows Computer Use로 화면을 읽고 상태선 메뉴를 클릭했다. 일부 일반 키 입력이 전달되지 않아 SDL2/SDL1, 스캔코드 설정을 비교했지만 Windows 입력 경로의 원인은 확정하지 못했다. 그 결과를 Mdir 자체 버그로 판정하지 않았다.

이후 DOSBox-X의 [공식 디버거 프로토콜](https://github.com/joncampbell123/dosbox-x/blob/master/README.debugger)로 게스트 BIOS 키보드 링 버퍼에 키를 넣고 실행을 재개했다. 프로그램 코드·등록 검사·파일 처리 루틴은 수정하지 않았다. 메뉴 전환 시 입력 버퍼를 비우는 동작 때문에 여러 명령키를 한꺼번에 넣지 않고 각 키 처리 사이 간격을 두었다.

문자 화면은 BIOS 화면 크기와 VGA 텍스트 버퍼를 읽어 기록했다. 그래픽 모드인 MSET과 VV의 오류 화면은 실제 창 캡처로 확인했다. 텍스트 추출은 색·강조·커서·그래픽을 표현하지 못한다. 디버거 정지·재개가 있으므로 성능·실시간 동작·Windows 물리 키 입력의 증거로 사용하지 않는다.

## 실제 실행 결과

아래 PASS는 적힌 **개별 사례**가 통과했다는 의미다. 동일 기능의 모든 정상·오류·취소·재시작 사례가 통과했다는 의미가 아니다.

| 사례 | 결과 | 관찰 및 연결 근거 |
|---|---|---|
| 시작·판본 확인 | PASS | M.EXE 실행, 3.10/미등록판 문구 확인. 메인에 합성 파일 3개와 드라이브 목록 표시 |
| 풀다운 메뉴 | PASS | Mdir / Run / File / Directory / Archive / Option 6개 메뉴 관찰; [메뉴 기록](evidence/2026-10-20/019-bios-menu.txt) |
| 도움말 | PASS | F1 도움말 열기 및 Esc 복귀; [문자 화면](evidence/2026-10-20/020-help.txt) |
| 이름순 정렬 | PASS | GAMMA/ALPHA/BETA → ALPHA/BETA/GAMMA, 상태 Q → N; [결과](evidence/2026-10-20/022-name-sort-single.txt) |
| Space 단일 선택 | PASS | ALPHA 선택, 선택 합계 1개/14바이트, 커서가 다음 파일로 이동; [결과](evidence/2026-10-20/023-select-one.txt) |
| 복사 대상 선택 | PASS | Alt-C → 드라이브 → MCD 트리 → 대상 선택. 수동 경로 입력만의 대화상자로 가정하면 안 됨 |
| 이름 충돌 UI | PASS | OverWrite/All/sKip_all/Skip/Rename/Newer 6항목과 원본/대상 시간·크기·경로 표시; [결과](evidence/2026-10-20/026-copy-conflict.txt) |
| 충돌에서 Esc 취소 | PASS(내용 보존) / 추가 조사 | SRC/DST ALPHA의 서로 다른 해시 유지. 선택 표시는 해제되어 보임; 중간 취소의 선택 유지 규칙은 재검증 필요 |
| BETA 실제 복사 | PASS | DST/BETA 생성, SRC/BETA와 SHA-256 일치. [파일 기록](evidence/2026-10-20/029-files.json) |
| 폴더 만들기 | PASS | Alt-K, NEWDIR 입력·확정 → 실제 디렉토리 생성 |
| 폴더 이름 바꾸기 | PASS | NEWDIR → RENAMED, 호스트 파일시스템에서도 확인 |
| MCD·트리 크기 | PASS | F10/F9, SRC의 파일 3개/하위 폴더 1개/37바이트와 일치. [집계](evidence/2026-10-20/035-tree-size.txt) |
| QCD 등록·이동 | PASS | 1번에 SRC 등록, DST에서 Shift-F1으로 SRC 이동. 2~10번·삭제·오류·재시작 유지까지 검증한 것은 아님 |
| MFF 검색 | PASS | 확인된 명령 `C:\MDIR\MFF C: *.TXT`로 TXT 4개/54바이트. [검색 결과](evidence/2026-10-20/043-mff-exact.txt) |
| MFF 위치로 이동 | PASS(경로) | Enter → Yes → DST로 복귀. `/X` 사용 시 커서는 파일이 아닌 부모 행에 있음; MFF 문서의 풀메모리 OFF 제한과 비교 필요 |
| VV 문서 보기 | BLOCKED_REGISTERED | Alt-V 실행 후 `Sorry. Register version only...`. 문서 렌더링·인코딩·글꼴은 미검증. [실제 오류 화면](evidence/2026-10-20/vv-registration-blocked.png) |
| MSET 메뉴 | PASS(메뉴 관찰) | Mdir/프로그램/메인화면/MCD/기타/색깔 메뉴 관찰. 설정 82항목의 **효과 검증 완료가 아님** |
| 설정 변경·저장 | PASS | 24시간제 OFF→ON, 종료 시 저장 질문, 저장 후 시간 표시 변경. M.CFG 해시 변화 및 프로그램 재시작 후 유지 확인. [설정 화면](evidence/2026-10-20/mset-main-options.png) |
| 임시 정렬의 지속성 | 관찰 | MSET 저장 후 목록 정렬 N→Q. 메인에서 바꾼 정렬이 CFG 저장값으로 유지되는지 구분해야 함 |
| 속성 쓰기 | PASS | ALPHA에 ReadOnly 지정 → 호스트 속성 ReadOnly/Archive로 확인 |
| 보호 파일 삭제 취소 | PASS | 삭제 Yes 다음 Special attributes 확인이 추가로 표시됨. Esc 후 파일 내용·속성 유지; [추가 확인](evidence/2026-10-20/071-delete-readonly-extra.txt) |
| 같은 드라이브 이동 | PASS | GAMMA가 SRC에서 사라지고 DST에 생성. 내용 SHA-256 일치 |
| 주석 저장 | PASS | `ALPHA.TXT ALPHA NOTE\r\n` 형태의 DESCRIPT.ION 생성, 화면 표시와 재시작 후 읽기 확인 |
| 주석 길이 | PASS(편집 한계 측정) | ASCII X 120바이트 입력 → 주석 80바이트 저장. 기존 장문 읽기·한글 바이트/문자 한계는 미검증 |
| ZIP 탐색 | BLOCKED_TOOL | 합성 ZIP에서 Enter 후 실제 외부 `PKUNZIP` 호출, `Bad command or filename - "PKUNZIP"`; [작업 화면](evidence/2026-10-20/085-archive-last-screen.txt) |
| MF 포맷 | BLOCKED_REGISTERED | 메뉴는 실행됨. Format 실행 시 `Register version only`; 실제 포맷 수행 없음. [오류](evidence/2026-10-20/087-mf-no-media.txt) |
| MCOPY 읽기 | BLOCKED_REGISTERED | 메뉴는 실행됨. Read 실행 시 `Register version only`; 실제 복제 없음. [오류](evidence/2026-10-20/091-mcopy-read-no-media.txt) |
| MCOPY Format | PASS(UI) / 작업 미검증 | F로 ON/OFF 메뉴가 나오고 OFF로 바뀜. 실제 포맷 구현 여부는 등록 제한으로 미확인. [상태](evidence/2026-10-20/090-mcopy-format-off.txt) |
| 도스명령·변수 | PASS(일부) | `?` 명령에서 `ECHO %F` 결과 TEST.ZIP. 이름·확장자·현재 경로·드라이브 치환도 합성 파일로 확인 |
| %M | DIFF/원인 미확정 | 설치 디렉토리 반환이 문서 기대이나 해당 명령 시험에서 빈 값. 문맥·판본·셸 처리와 분리 재현 필요 |
| 명령 이력 | PASS(메뉴) | PgUp으로 위 두 명령이 History에 표시됨. 재실행·영속 파일까지 완전 검증한 것은 아님 |

최초 검색 명령 입력과 ZIP 외부 생성 후 캐시 갱신 과정에는 시험 도구의 입력/디렉토리 캐시 영향이 있었다. 잘못 입력된 최초 MFF 결과나 외부 파일이 아직 보이지 않았을 때의 VV 실행을 검색·압축 성공 증거로 사용하지 않았다. 수정된 명령은 실행 전에 화면으로 확인했고, ZIP은 에뮬레이터 재시작 후 표시되는 것을 확인했다.

## 전환 명세에 반영할 사항

1. **입력/대상 선택을 독립 명세로 작성**한다. 선택 집합과 커서는 별개이며 Space 후 커서가 이동한다. 복사 대상도 MCD 선택 흐름이다.
2. **충돌·보호 속성·취소를 먼저 구현할 테스트로 삼는다.** 단순 Copy 호출만으로 원본 동작이 재현되지 않는다. 취소 시 선택 해제의 규칙은 보류한다.
3. **주석 편집 한계는 80바이트 ASCII로 관찰되었다.** 문서의 ‘길이 제한 없음’은 읽기/보존 측면과 나누어 추가 조사한다. Windows판 저장 한계로 자동 승계하지 않는다.
4. **압축은 외부 도구 프로세스와 출력 파싱을 포함한다.** 원본에 내장 ZIP 목록 파서가 있다고 가정하지 않는다. Windows판은 형식별 읽기/쓰기 어댑터와 실패 표시를 설계한다.
5. **설정 파일과 실행 중 상태를 구분**한다. MSET 저장·재시작 시 정렬·시간 표시 등 실제 적용과 파일 차이를 함께 비교한다.
6. **등록 제한은 분석 결과**로 보존한다. VV/MF/MCOPY의 내부 작업·11종 압축·Win95 전용 기능을 관찰 완료로 표시하지 않는다.

## 남은 P0 작업과 차단 사유

- **등록판 의존**: VV 내부 동작, MF 포맷, MCOPY 읽기/쓰기·실제 Format. 적법하게 실행 가능한 원본이 확보되기 전까지 문서 명세와 오류 관찰만 유지한다.
- **외부 압축 도구 부재**: PKUNZIP 등 11형식별 도구·버전·출력 차이. ZIP 내부 탐색과 추출부터 필요한 도구를 정해 추가 조사한다.
- **환경 부재**: Win95/DOS 7 긴 이름·한글 BIOS·LAN/CD/실물 플로피. 내장 DOS의 보고 버전 변경을 Win95 검증으로 대체하지 않는다.
- **독립적으로 계속 가능한 항목**: 나머지 정렬·필터·열·선택 패턴, 충돌 6정책 각각의 처리, 파일/폴더 삭제·복구, 주석 동반·장문 읽기, %M 및 기타 변수, MSET 항목별 변경·취소·저장, HCONV/HE/DSCMAN 역할 분석.

따라서 **P0 완료나 P1 기술 결정 완료를 선언하지 않는다.** 현재 성과는 실행 가능한 기준선과 주요 파일작업·도구 제한을 증거로 확보한 것이다. 다음 묶음은 접근 가능한 파일작업의 오류/취소 사례와 설정 포맷 차등 분석이다.
