# 원본 기능의 현재 통합 상태

갱신: 2026-10-22. 기존 173개 ID와 관찰 이력을 유지한다. P0 진행 중이며 P1은 미진입이다.

[미해결 항목·진입 조건](P0_REVIEW.ko.md) · [기능 정의](FEATURE_CATALOG.ko.md) · [JSON 원장](evidence/current-status.json)

메뉴 관찰·개별 사례·부분 관찰은 기능 전체 검증이 아니다. 전체 검증 완료 행은 0개이며 완료율로 환산하지 않는다.

과거 등록 차단 8개는 현재 차단에서 해제했다. 그중 글꼴·색상·해상도 VIEW-004는 미실행이다. 과거 차단 증거는 각 행의 관찰 이력에 남긴다.

| 상태 | 기능 행 수 |
|---|---:|
| 외부 도구 차단 (`BLOCKED_TOOL`) | 1 |
| 문서와 차이 (`DIFF`) | 1 |
| 메뉴만 관찰 (`MENU_OBSERVED`) | 79 |
| 미실행 (`NOT_RUN`) | 43 |
| 개별 사례 관찰 (`OBSERVED_CASE`) | 7 |
| 부분 관찰 (`PARTIAL`) | 37 |
| 부분 관찰·예외 (`PARTIAL_WITH_ANOMALY`) | 5 |

합계 173행. 아래 증거는 최신 관찰이며 이전 증거는 JSON의 observations에 보존된다.

| ID | 기능 | 현재 상태 | 최신 관찰/증거 | 미해결 |
|---|---|---|---|---|
| UI-001 | 도움말과 메뉴 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/019-bios-menu.txt) · [증거 2](../docs/evidence/2026-10-20/020-help.txt) | — |
| UI-002 | 상태선 안내 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| UI-003 | 목록 열 구성 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| UI-004 | 화면 구성 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| UI-005 | 파일 표시 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| UI-006 | 정렬 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/022-name-sort-single.txt) | — |
| UI-007 | 정렬 동률 규칙 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| NAV-001 | 커서 이동 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/023-select-one.txt) · [증거 2](../docs/evidence/2026-10-20/034-mcd.txt) | — |
| NAV-002 | 문자 빠른 검색 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| NAV-003 | 드라이브/상위/루트 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| NAV-004 | 작업 디렉토리 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| NAV-005 | 이전 대상 복귀 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| MOUSE-001 | 마우스 입력 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/019-bios-menu.txt) | — |
| MOUSE-002 | 상태선 명령 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| SEL-001 | 선택 집합 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/023-select-one.txt) | — |
| SEL-002 | 선택 순서 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| FILE-001 | 복사 | 부분 관찰·예외 | [보고서](PARTIAL_FAILURE_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-22/partial-07/w002-conflict.txt) · [증거 2](../docs/evidence/2026-10-22/partial-07/w004-progress.txt) · [증거 3](../docs/evidence/2026-10-22/partial-07/w005-cancelled.txt) · [증거 4](../docs/evidence/2026-10-22/partial-07/file-verification.json) | P0-06 |
| FILE-002 | 충돌 처리 | 부분 관찰 | [보고서](DESCRIPTION_RULES.ko.md) · [증거 1](../docs/evidence/2026-10-21/description-06/s008-all-conflict.txt) · [증거 2](../docs/evidence/2026-10-21/description-06/s012-skip-all.txt) · [증거 3](../docs/evidence/2026-10-21/description-06/s015-newer-conflict.txt) · [증거 4](../docs/evidence/2026-10-21/description-06/s016-newer-choice.txt) · [증거 5](../docs/evidence/2026-10-21/description-06/file-verification.json) | P0-06 |
| FILE-003 | 부족 용량/부분 실패 | 부분 관찰·예외 | [보고서](PARTIAL_FAILURE_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-22/partial-07/w005-cancelled.txt) · [증거 2](../docs/evidence/2026-10-22/partial-07/p002-warning.txt) · [증거 3](../docs/evidence/2026-10-22/partial-07/p003-continue.txt) · [증거 4](../docs/evidence/2026-10-22/partial-07/p004-write-failure-no.txt) · [증거 5](../docs/evidence/2026-10-22/partial-07/file-verification.json) | P0-06 |
| FILE-004 | 이동 | 부분 관찰·예외 | [보고서](PARTIAL_FAILURE_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-22/partial-07/m002-conflict.txt) · [증거 2](../docs/evidence/2026-10-22/partial-07/m004-progress.txt) · [증거 3](../docs/evidence/2026-10-22/partial-07/m005-cancelled.txt) · [증거 4](../docs/evidence/2026-10-22/partial-07/file-verification.json) | P0-06 |
| FILE-005 | 이름 변경 | 부분 관찰 | [보고서](REGISTERED_OPERATIONS.ko.md) · [증거 1](../docs/evidence/2026-10-21/registered-03/file-verification.json) | — |
| FILE-006 | 삭제 | 부분 관찰 | [보고서](DESCRIPTION_RULES.ko.md) · [증거 1](../docs/evidence/2026-10-21/description-06/s018-file-delete.txt) · [증거 2](../docs/evidence/2026-10-21/description-06/s019-file-deleted.txt) · [증거 3](../docs/evidence/2026-10-21/description-06/file-verification.json) | P0-06 |
| FILE-007 | 폴더 생성 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/031-mkdir-created.txt) | — |
| FILE-008 | 속성 변경 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/069-readonly-set.txt) | — |
| FILE-009 | 문서 보기/인쇄 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/vv-registration-blocked.png) | — |
| DISK-001 | 볼륨명 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| DISK-002 | 포맷/복제/파킹 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| TREE-001 | MCD 탐색 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/034-mcd.txt) | — |
| TREE-002 | MCD 재검색/캐시 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| TREE-003 | MCD 폴더 작업 | 부분 관찰 | [보고서](CONFLICT_RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-21/conflict-05/c012-folder-copy-drive.txt) · [증거 2](../docs/evidence/2026-10-21/conflict-05/c030-copy-only.txt) · [증거 3](../docs/evidence/2026-10-21/conflict-05/file-verification.json) | P0-02, P0-03 |
| TREE-004 | MCD 크기/정렬 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/035-tree-size.txt) | — |
| QCD-001 | 즐겨찾기 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/038-qcd-saved.txt) · [증거 2](../docs/evidence/2026-10-20/073-qcd-jump.txt) | — |
| RUN-001 | 실행 방식 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| RUN-002 | 종료 후 실행 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| RUN-003 | 28개 펑션키 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| RUN-004 | 확장자 연결 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| RUN-005 | 마지막 실행 화면 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/085-archive-last-screen.txt) | — |
| CMD-001 | 명령줄 | 부분 관찰 | [보고서](REGISTERED_OPERATIONS.ko.md) · [증거 1](../docs/evidence/2026-10-21/registered-03/file-verification.json) | P0-04 |
| CMD-002 | 입력 편집/삽입 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/042-mff-edit.txt) | — |
| CMD-003 | 명령 이력 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/097-command-history.txt) | — |
| CLI-001 | 실행 인자 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| CLI-002 | 표시/정렬 옵션 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| CLI-003 | 환경 옵션 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| CLI-004 | 시작/종료 모드 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| CLI-005 | BAT 래퍼 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| DESC-001 | 주석 편집 | 부분 관찰 | [보고서](DESCRIPTION_RULES.ko.md) · [증거 1](../docs/evidence/2026-10-21/description-06/s001-duplicate-read.txt) · [증거 2](../docs/evidence/2026-10-21/description-06/s002-duplicate-edit.txt) · [증거 3](../docs/evidence/2026-10-21/description-06/s003-edited.txt) · [증거 4](../docs/evidence/2026-10-21/description-06/s004-restart.txt) · [증거 5](../docs/evidence/2026-10-21/description-06/s005-delete-comment.txt) · [증거 6](../docs/evidence/2026-10-21/description-06/file-verification.json) | P0-11 |
| DESC-002 | 주석 동반 | 부분 관찰·예외 | [보고서](PARTIAL_FAILURE_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-22/partial-07/w005-cancelled.txt) · [증거 2](../docs/evidence/2026-10-22/partial-07/m005-cancelled.txt) · [증거 3](../docs/evidence/2026-10-22/partial-07/file-verification.json) | P0-03, P0-06, P0-11 |
| DESC-003 | 주석 표시/긴 이름 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/082-restart-restored.txt) | P0-09 |
| ARC-001 | 압축 인식 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/085-archive-last-screen.txt) | — |
| ARC-002 | 내부 탐색 | 외부 도구 차단 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/085-archive-last-screen.txt) | P0-07 |
| ARC-003 | 생성/추가 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| ARC-004 | 압축 후 원본 삭제 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| ARC-005 | 추출/내부 삭제 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| ARC-006 | 내부 파일 실행/보기 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| FIND-001 | 파일 검색 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/042-mff-edit.txt) · [증거 2](../docs/evidence/2026-10-20/043-mff-exact.txt) | — |
| FIND-002 | 검색 취소 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| FIND-003 | 결과 탐색/정렬/선택 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| FIND-004 | 결과에서 작업 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/044-mff-location.txt) · [증거 2](../docs/evidence/2026-10-20/045-mff-location-confirm.txt) | — |
| VIEW-001 | 코드 인식 | 부분 관찰 | [보고서](VV_RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-21/vv-02/07-ksc-auto.png) · [증거 2](../docs/evidence/2026-10-21/vv-02/08-johab-auto.png) · [증거 3](../docs/evidence/2026-10-21/vv-02/09-johab-as-ksc.png) · [증거 4](../docs/evidence/2026-10-21/vv-02/10-binary.png) | — |
| VIEW-002 | 문서 이동 | 부분 관찰 | [보고서](VV_RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-21/vv-02/11-long-end.png) | — |
| VIEW-003 | 문서 표시 | 부분 관찰 | [보고서](VV_RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-21/vv-02/01-long-off.png) · [증거 2](../docs/evidence/2026-10-21/vv-02/02-long-wrap.png) · [증거 3](../docs/evidence/2026-10-21/vv-02/04-tabs4.png) · [증거 4](../docs/evidence/2026-10-21/vv-02/05-tabs8.png) | — |
| VIEW-004 | 색상/글꼴/해상도 | 미실행 | [보고서](VV_RUNTIME_FINDINGS.ko.md) | — |
| VIEW-005 | 설정 저장 | 부분 관찰 | [보고서](VV_RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-21/vv-02/03-restart-wrap.png) · [증거 2](../docs/evidence/2026-10-21/vv-02/file-verification.json) | — |
| VIEW-006 | 메뉴/종료/화면보호 | 부분 관찰 | [보고서](VV_RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-21/vv-02/06-menu.png) | — |
| FORMAT-001 | 플로피 포맷 | 부분 관찰·예외 | [보고서](DISK_RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-21/disk-04/d027-mf-format-break.txt) · [증거 2](../docs/evidence/2026-10-21/disk-04/d028-mf-active-cancel.txt) · [증거 3](../docs/evidence/2026-10-21/disk-04/d021-mf-quick-escape.txt) · [증거 4](../docs/evidence/2026-10-21/disk-04/image-verification.json) | P0-05, P0-10 |
| COPY-001 | 디스켓 복제 | 부분 관찰 | [보고서](DISK_RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-21/disk-04/d001-write-before-read.txt) · [증거 2](../docs/evidence/2026-10-21/disk-04/d002-read-cancel.txt) · [증거 3](../docs/evidence/2026-10-21/disk-04/d009-write-cancel.txt) · [증거 4](../docs/evidence/2026-10-21/disk-04/d017-write-done.txt) · [증거 5](../docs/evidence/2026-10-21/disk-04/image-verification.json) | P0-10 |
| COPY-002 | 포맷 옵션 모순 | 부분 관찰 | [보고서](DISK_RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-21/disk-04/d008-format-off.txt) · [증거 2](../docs/evidence/2026-10-21/disk-04/d017-write-done.txt) · [증거 3](../docs/evidence/2026-10-21/disk-04/image-verification.json) | P0-10 |
| LEGACY-001 | 화면보호 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| LEGACY-002 | 한글 변환 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| LEGACY-003 | 추가 실행파일 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| LEGACY-004 | 구형 실행환경 | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | P0-09 |
| SET-001 | Mdir / 메뉴숨김 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-mdir-menu.png) | — |
| SET-002 | Mdir / 도움말 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-mdir-menu.png) | — |
| SET-003 | Mdir / 불러오기 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-mdir-menu.png) | — |
| SET-004 | Mdir / 저장하기 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/067-mset-save.txt) · [증거 2](../docs/evidence/2026-10-20/environment.json) | — |
| SET-005 | Mdir / 색깔부르기 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-mdir-menu.png) | — |
| SET-006 | Mdir / 색깔저장 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-mdir-menu.png) | — |
| SET-007 | Mdir / 등록판생성 | 부분 관찰 | [보고서](REGISTRATION_ANALYSIS.ko.md) · [증거 1](../docs/evidence/2026-10-21/registration-verification.json) · [증거 2](../docs/evidence/2026-10-21/generated-about.txt) | — |
| SET-008 | Mdir / 종료 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-mdir-menu.png) | — |
| SET-009 | 프로그램 / 확장자지정 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-program-menu.png) | — |
| SET-010 | 프로그램 / 펑션키지정 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-program-menu.png) | — |
| SET-011 | 프로그램 / 파일보기 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-program-menu.png) | — |
| SET-012 | 프로그램 / 디스크포맷 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-program-menu.png) | — |
| SET-013 | 프로그램 / 디스크복사 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-program-menu.png) | — |
| SET-014 | 프로그램 / 디스크파킹 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-program-menu.png) | — |
| SET-015 | 프로그램 / 파일찾기 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-program-menu.png) | — |
| SET-016 | 프로그램 / 화면보호 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-program-menu.png) | — |
| SET-017 | 프로그램 / 명령처리기 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-program-menu.png) | — |
| SET-018 | 프로그램 / 임시디렉토리 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-program-menu.png) | — |
| SET-019 | 프로그램 / 도스명령 정지 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-program-menu.png) | — |
| SET-020 | 프로그램 / 프로그램 정지 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-program-menu.png) | — |
| SET-021 | 메인화면 / 컬럼수 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-022 | 메인화면 / 파일정렬 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-023 | 메인화면 / 압축파일 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-024 | 메인화면 / Esc키 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-025 | 메인화면 / 가로선 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-026 | 메인화면 / 세로선 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-027 | 메인화면 / 세로크기고정 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-028 | 메인화면 / 스크롤 막대 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-029 | 메인화면 / 소문자 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-030 | 메인화면 / 속성표시 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-031 | 메인화면 / 숨은파일 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-032 | 메인화면 / 실행파일만 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-033 | 메인화면 / 삭제초기값 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-034 | 메인화면 / 풀메모리 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-035 | 메인화면 / 주석보기 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-036 | 메인화면 / 디렉토리재현 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-037 | 메인화면 / Ins/Del 차별화 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-038 | 메인화면 / @D/Del 맞바꿈 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-main-options.png) | — |
| SET-039 | MCD / 화면크기 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-mcd-menu.png) | — |
| SET-040 | MCD / 디렉토리지움 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-mcd-menu.png) | — |
| SET-041 | MCD / 루트 삭제가능 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-mcd-menu.png) | — |
| SET-042 | MCD / DEL키 사용 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-mcd-menu.png) | — |
| SET-043 | MCD / MCD 정렬 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-mcd-menu.png) | — |
| SET-044 | MCD / MCD시작 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-mcd-menu.png) | — |
| SET-045 | MCD / MCD후 종료 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-mcd-menu.png) | — |
| SET-046 | MCD / FDD 정지 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-mcd-menu.png) | — |
| SET-047 | 기타 / 화면보호시간 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-048 | 기타 / 한글코드 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-049 | 기타 / 화면크기 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-050 | 기타 / M.HIS저장 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-051 | 기타 / LAN드라이브 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-052 | 기타 / 24시간제 | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-time-option.png) · [증거 2](../docs/evidence/2026-10-20/082-restart-restored.txt) | — |
| SET-053 | 기타 / 느린상자열기 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-054 | 기타 / 로고상자표시 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-055 | 기타 / 마우스사용 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-056 | 기타 / 왼손마우스 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-057 | 기타 / 빠른초기화 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-058 | 기타 / 빠른  키입력 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-059 | 기타 / 확장빨리찾기 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-060 | 기타 / 흑백색깔사용 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-061 | 기타 / 팔레트변경가능 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-062 | 기타 / 드라이브종류 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-063 | 기타 / 캐쉬버퍼저장 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-064 | 기타 / 긴파일명지원 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-other-menu.png) | — |
| SET-065 | 색깔 / 파일확장자별 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-066 | 색깔 / MCD | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-067 | 색깔 / MCD 상태선 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-068 | 색깔 / 디렉토리명 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-069 | 색깔 / 드라이브명 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-070 | 색깔 / 메인화면 선 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-071 | 색깔 / 펑션키 보통 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-072 | 색깔 / 펑션키 강조 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-073 | 색깔 / 파일수 보통 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-074 | 색깔 / 파일수 강조 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-075 | 색깔 / 나머지 파일 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-076 | 색깔 / 도움말 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-077 | 색깔 / 빨리찾기메인 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-078 | 색깔 / 빨리찾기MCD | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-079 | 색깔 / 대화상자 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-080 | 색깔 / 메인화면배경 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-081 | 색깔 / 펑션키  배경 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| SET-082 | 색깔 / 팔레트 | 메뉴만 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/mset-colors-menu.png) | — |
| VAR-001 | `!.!` | 개별 사례 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/vars.txt) · [증거 2](../docs/evidence/2026-10-20/096-simple-variables-result.txt) | — |
| VAR-002 | `%F` | 개별 사례 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/vars.txt) · [증거 2](../docs/evidence/2026-10-20/096-simple-variables-result.txt) | — |
| VAR-003 | `!,` | 개별 사례 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/vars.txt) · [증거 2](../docs/evidence/2026-10-20/096-simple-variables-result.txt) | — |
| VAR-004 | `,!` | 개별 사례 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/vars.txt) · [증거 2](../docs/evidence/2026-10-20/096-simple-variables-result.txt) | — |
| VAR-005 | `!\` | 개별 사례 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/vars.txt) · [증거 2](../docs/evidence/2026-10-20/096-simple-variables-result.txt) | — |
| VAR-006 | `%A` | 개별 사례 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/vars.txt) · [증거 2](../docs/evidence/2026-10-20/096-simple-variables-result.txt) | — |
| VAR-007 | `!:` | 개별 사례 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/vars.txt) · [증거 2](../docs/evidence/2026-10-20/096-simple-variables-result.txt) | — |
| VAR-008 | `!\!.!` | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| VAR-009 | `%D` | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| VAR-010 | `%R` | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| VAR-011 | `%M` | 문서와 차이 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/vars.txt) | P0-01 |
| VAR-012 | `%1-%0` | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| VAR-013 | `%[xxx]` | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| VAR-014 | `%;` | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| VAR-015 | `%B` | 부분 관찰 | [보고서](REGISTERED_OPERATIONS.ko.md) · [증거 1](../docs/evidence/2026-10-21/registered-03/file-verification.json) | P0-04 |
| VAR-016 | `%N` | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| VAR-017 | `%P` | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| VAR-018 | `%$` | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| VAR-019 | `%%` | 미실행 | [보고서](RUNTIME_FINDINGS.ko.md) | — |
| VAR-020 | `%L` | 부분 관찰 | [보고서](RUNTIME_FINDINGS.ko.md) · [증거 1](../docs/evidence/2026-10-20/vars.txt) | — |
