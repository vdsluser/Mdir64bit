# 파일 충돌·취소·폴더 주석 조사

조사일: 2026-10-21. 생성 등록번호로 등록한 FAT12 작업 이미지 C:/D:를 DOSBox-X 2026.10.01 / DOS 6.22에서 실행했다. `M.EXE /X`, 합성 8.3 파일명, ASCII 주석만 사용했다. 원본 자료·기준 이미지는 보존했고 실제 사용자 파일이나 물리 장치는 사용하지 않았다.

## 충돌 대화상자의 결과

C:\CASE5의 A/B/C.TXT에는 각각 `SOURCE-A/B/C`와 `source-a/b/c` 주석, D:\DST5의 같은 이름에는 `TARGET-A/B/C`와 `target-a/b/c` 주석을 두었다. 내용은 모두 CRLF를 포함한 10바이트로 크기가 같아 해시·바이트로 판정했다.

| 선택 | 파일 결과 | 주석 결과 |
|---|---|---|
| A.TXT OverWrite | 대상이 SOURCE-A로 변경, 원본 유지 | 기존 `A.TXT target-a`를 지우지 않고 `A.TXT source-a` 추가. 같은 파일명 항목 두 개 |
| B.TXT Skip | TARGET-B 유지 | target-b 유지, source-b 추가 안 됨 |
| C.TXT 충돌 창에서 Esc | TARGET-C 유지 | target-c 유지, source-c 추가 안 됨 |
| C.TXT 충돌 창의 Rename→CNEW.TXT | 기존 TARGET-C 유지, CNEW.TXT에 SOURCE-C 복사 | `CNEW.TXT source-c` 추가 |

대상 목록을 새로 열었을 때 A.TXT의 표시는 **source-a**였다. 파일 저장 원문은 아래처럼 중복을 포함했다. 해당 표본은 뒤쪽 항목이 화면에 보였지만, 모든 파서·모든 갱신 동작의 중복 처리 규칙까지 확정한 것은 아니다.

```text
A.TXT target-a
B.TXT target-b
C.TXT target-c
A.TXT source-a
CNEW.TXT source-c
```

관련 증거: [충돌 창](evidence/2026-10-21/conflict-05/c001-copy-a.txt), [Skip 후](evidence/2026-10-21/conflict-05/c004-skip.txt), [Esc 후](evidence/2026-10-21/conflict-05/c005-copy-c.txt), [Rename 입력](evidence/2026-10-21/conflict-05/c009-rename-option.txt), [대상 목록](evidence/2026-10-21/conflict-05/c016-target-display.txt). 각 단계의 원본/대상 주석·파일 검증은 [검증 기록](evidence/2026-10-21/conflict-05/file-verification.json)에 있다.

이번에는 단일 파일 OverWrite/Skip/Rename/Esc만 확인했다. All/sKip_all/Newer, 서로 다른 시간과 속성, 이동 중 충돌, 기존 대상을 덮어쓰는 도중 취소는 남아 있다.

## 복사 진행 후 Esc

BIG.BIN은 `bytes(range(256)) * 2048`로 만든 524288바이트다. 게스트 DOS 쓰기 호출 `BPINT 21 40`에 중단점을 걸고 BIG.BIN 복사 진행 창까지 진행했다. 중단점을 제거한 뒤 BIOS 키 큐로 Esc를 넣어 재개했다. 실행 파일은 수정하지 않았다.

작업 후 메뉴로 복귀했고 다음을 확인했다.

- 원본 BIG.BIN의 전체 바이트와 주석 유지.
- 대상 파일시스템에 BIG.BIN 없음, 대상 주석에도 BIG.BIN 없음.
- 중단 전후 원시 이미지의 512바이트 섹터 255개가 다름. 그중 253개는 이번 원본 표본 패턴이 새로 기록된 섹터이며, 섹터 번호 1378~1630에 위치.

따라서 이 사례는 **실제 데이터 기록 후 대상 파일과 주석을 정리한 취소**다. 원시 이미지 전체를 기록 전 상태로 되돌린 것은 아니다. 삭제된 데이터 영역의 패턴 잔존을 보안 삭제나 복구 보장으로 해석하지 않는다. 디버거가 시점을 제어하므로 실제 하드웨어의 취소 지연·성능은 측정하지 않았다.

[복사 진행 창](evidence/2026-10-21/conflict-05/c024-write-break-progress.txt), [취소 후](evidence/2026-10-21/conflict-05/c025-active-cancel.txt), [입력 방법](evidence/2026-10-21/conflict-05/cancel-method.json).

## 용량 부족의 사전 취소

D:에 600KiB FILL.BIN을 추가한 뒤 같은 BIG.BIN 복사를 시도했다. `Not enough free space for COPY. Continue?`의 No를 선택하자 메뉴로 복귀했다. 대상의 기존 파일·주석과 FILL.BIN 내용은 유지됐고 BIG.BIN은 생성되지 않았다.

[용량 경고](evidence/2026-10-21/conflict-05/c027-space-warning.txt), [No 후](evidence/2026-10-21/conflict-05/c028-space-decline.txt). 경고에서 Yes를 선택해 실제 디스크 부족까지 진행한 부분 실패는 이번 결과에 포함하지 않는다.

## 폴더 작업의 진입 경로 차이

메인 목록에서 TREE를 선택하고 Alt-C로 들어간 대상 선택 모드에서는 F3로 D:를 선택할 수 있었다. Alt-C로 폴더를 복사한 뒤 Alt-M으로 같은 폴더를 이동하는 경로를 관찰했다. 별도 재현에서는 이동을 수행하지 않고 **C:\CASE5\TREE→D:\TREE 복사만** 실시해 원본 유지와 대상 내부 파일·DESCRIPT.ION의 바이트 일치를 확인했다.

별도 재현에서 COPYONLY라는 문자 입력은 대상 모드의 디렉토리 선택으로 작동하지 않았고, 실제 목적지는 D: 루트였다. 이를 의도한 경로의 성공으로 적지 않고 종료 후 확인한 실제 D:\TREE를 검증했다. [별도 복사 완료](evidence/2026-10-21/conflict-05/c030-copy-only.txt).

이 경로는 앞선 MCD F10→F5에서 F3가 비활성으로 보였던 경로와 다르다. **교차 드라이브 폴더 복사 자체는 가능**하되, MCD F5 경로 차이의 원인은 아직 미해결이다. [D: 선택](evidence/2026-10-21/conflict-05/c012-folder-copy-drive.txt), [메인 Alt-C 복귀](evidence/2026-10-21/conflict-05/c013-folder-copied.txt).

메인 Alt-C/Alt-M 경로에서도 폴더 내부 주석 파일은 함께 처리됐지만, 폴더 자체의 부모 주석 `TREE parent-tree`는 대상 부모에 추가되지 않았다. 이동 후 원래 부모 쪽 항목도 남았다. 앞선 MCD 경로와 같은 범위의 관찰이며 모든 폴더 작업으로 일반화하지 않는다.

## 검증과 다음 조사

[검증 기록](evidence/2026-10-21/conflict-05/file-verification.json)의 파일·주석·등록 파일·부분 기록 검사 19개를 통과했다. 원시 이미지와 메모리 덤프는 로컬에 보존하며 공개 자료에는 합성 주석과 해시·섹터 수만 포함한다. [기능별 후속 상태](evidence/2026-10-21/conflict-05/status.json)는 기존 ID의 부분 관찰이며 전 기능 완료를 뜻하지 않는다.

Windows판에서 충돌 정책은 파일 내용과 주석 갱신을 함께 정의해야 한다. 중복 주석을 읽을 때의 선택 규칙과 저장 시 중복 유지/정규화 정책은 P1 호환 검토 항목으로 추가한다. 취소 결과에는 파일 정리 여부와 이미 기록된 범위를 구분하고, 중간 파일·기존 대상 보호 전략을 별도로 설계한다.

다음은 P0-11 중복 주석의 읽기·편집·삭제 규칙, 남은 충돌 정책과 이동·덮어쓰기 중단을 조사한다. MCD F5 진입 경로 차이와 같은 드라이브 폴더 주석도 미해결 목록에 유지한다.
