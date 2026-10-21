# 원본 관찰 도구

현재 기능 원장은 `python tools/analysis/build_status.py`로 생성하고 `python tools/analysis/build_status.py --check`로 재현성을 검사한다. 최초 실행 결과와 후속 보고서의 관찰 이력을 보존하며 실행 없이 성공을 판정하는 도구는 아니다. [통합 검토](../../docs/P0_REVIEW.ko.md)를 참고한다.

공개 Python 도구는 표준 라이브러리만 사용한다. 원본 자료는 저장소에 포함하지 않으므로 로컬 `mdir/`에 별도로 준비한다. 원본 실행 파일을 패치하지 않는다. 등록번호 복원 도구와 검증 범위는 [등록 분석 보고서](../../docs/REGISTRATION_ANALYSIS.ko.md)를 따른다.

1. 저장소 루트에서 `python tools/analysis/prepare_baseline.py --name run-02`를 실행한다. 새 실행 폴더를 만들며 기존 폴더를 덮어쓰지 않는다. 에뮬레이터 ZIP이 없다면 `--download`를 명시한다. 고정된 공식 릴리스의 SHA-256을 대조한다.
2. 출력된 새 실행 경로를 `MDIR_ANALYSIS_DIR` 환경변수로 지정한다. 예: PowerShell에서 `$env:MDIR_ANALYSIS_DIR = (Resolve-Path analysis-local/run-02).Path`.
3. `python tools/analysis/debug_bridge.py`를 별도 터미널에서 실행한다. 127.0.0.1의 58991(DOSBox debugger 연결), 58992(로컬 명령 HTTP) 포트를 사용한다. 동시에 한 인스턴스만 사용한다. 신뢰하는 로컬 분석 세션에서만 열고 종료 후 Ctrl-C로 닫는다.
4. 준비 스크립트가 출력한 에뮬레이터 실행 파일에 `-conf`와 출력된 설정 파일 경로, `-noconsole`을 넘겨 실행한다. 시작 로고가 사라져 메인 목록이 보일 때까지 기다린다.
5. `python tools/analysis/probe.py baseline`으로 문자 화면을 읽는다. `python tools/analysis/probe.py menu f12`처럼 사례 ID와 키를 전달한다. 입력·화면은 실행 폴더의 `evidence/`에 저장된다. 화면을 확인한 뒤 다음 입력을 결정한다.
6. 텍스트는 `text:문자열`, BIOS 키 워드는 `hex:8600`처럼 전달할 수 있다. 주요 키 이름은 probe.py의 KEYS에 정의되어 있다. 이 값은 Windows 물리 키 주입이 아니라 게스트 BIOS 입력이다.
7. 프로그램을 정상 종료하고, 에뮬레이터와 브리지를 닫는다. 원본 해시와 작업본 변화를 비교한 뒤 공개 가능한 합성 데이터·메뉴 화면만 선별한다. 메모리 덤프와 원본 바이너리·설명서 전문·등록정보는 로컬에 둔다.

MSET 같은 그래픽 화면은 텍스트 덤프로 검증할 수 없다. 실제 창 캡처를 병행한다. 디버거의 정지·재개 때문에 성능·시간 민감 동작의 검증에는 이 도구를 사용하지 않는다. 입력 기록은 실험 추적용이며 세션 재시작·UI 관찰까지 자동 재현하는 전체 테스트 러너가 아니다.

프로토콜/명령의 근거: [DOSBox-X README.debugger](https://github.com/joncampbell123/dosbox-x/blob/master/README.debugger).
