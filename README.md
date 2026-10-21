# Mdir64bit

Mdir III의 사용 흐름을 분석하여 Windows 11 x64용 파일 관리자로 재구현하기 위한 프로젝트입니다.

현재 단계는 **기능 조사와 전환 계획**입니다. 제품 구현은 시작하지 않았습니다.

- [원본 기능 명세 및 전환 로드맵](docs/ANALYSIS_AND_ROADMAP.ko.md)
- [기능·설정 추적표](docs/FEATURE_CATALOG.ko.md)
- [173개 기능의 현재 통합 상태](docs/CURRENT_STATUS.ko.md)
- [미해결 우선순위와 P1 진입 조건](docs/P0_REVIEW.ko.md)
- [원본 파일 지문과 분석 근거](docs/ORIGINAL_INVENTORY.ko.md)
- [원본 실행 검증 절차](docs/VALIDATION_PLAN.ko.md)
- [P0 원본 실행 조사 1차 결과와 차단 항목](docs/RUNTIME_FINDINGS.ko.md)
- [등록번호 생성 로직과 등록판 기능 조사](docs/REGISTRATION_ANALYSIS.ko.md)
- [등록판 VV의 한글·줄바꿈·탭·설정 저장 관찰](docs/VV_RUNTIME_FINDINGS.ko.md)
- [등록판 파일·주석·MCD·풀메모리 실행 관찰](docs/REGISTERED_OPERATIONS.ko.md)
- [MF/MCOPY 취소·오류·Format OFF 관찰](docs/DISK_RUNTIME_FINDINGS.ko.md)

2026-10-21 기준: 등록·VV·파일/주석·MCD·메모리 실행·MF/MCOPY의 후속 결과를 기존 173개 기능에 통합했습니다. 현재 판정은 위 통합 상태를 우선하며 최초 추적표와 실행 이력은 보존합니다. P0는 진행 중이고, P1 진입 조건은 아직 모두 충족하지 않았습니다. 전체 기능 검증 완료나 Windows판 구현 완료를 뜻하지 않습니다.

원본 실행 파일, 설명서 전문, 등록정보는 이 저장소에 포함하지 않습니다. 원본 자료는 로컬 `mdir/`에서 조사합니다.
