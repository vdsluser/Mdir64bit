# Mdir64bit

Mdir III의 사용 흐름을 분석하여 Windows 11 x64용 파일 관리자로 재구현하기 위한 프로젝트입니다.

현재 단계는 **기능 조사와 전환 계획**입니다. 제품 구현은 시작하지 않았습니다.

- [원본 기능 명세 및 전환 로드맵](docs/ANALYSIS_AND_ROADMAP.ko.md)
- [기능·설정 추적표](docs/FEATURE_CATALOG.ko.md)
- [원본 파일 지문과 분석 근거](docs/ORIGINAL_INVENTORY.ko.md)
- [원본 실행 검증 절차](docs/VALIDATION_PLAN.ko.md)
- [P0 원본 실행 조사 1차 결과와 차단 항목](docs/RUNTIME_FINDINGS.ko.md)

2026-10-21 기준: 격리된 DOSBox-X에서 주요 파일작업·MCD/QCD·검색·주석·설정 저장을 조사했습니다. 원본은 미등록판이며 VV/MF/MCOPY 작업에 등록 제한이 있습니다. 173개 항목의 상태와 증거를 기록했으며, P0는 진행 중입니다. 전체 기능 검증 완료를 뜻하지 않습니다.

원본 실행 파일, 설명서 전문, 등록정보는 이 저장소에 포함하지 않습니다. 원본 자료는 로컬 `mdir/`에서 조사합니다.
