# Mdir64bit

Mdir III의 사용 흐름을 분석하여 Windows 11 x64용 파일 관리자로 재구현하기 위한 프로젝트입니다.

현재 단계는 **기능 조사와 전환 계획**입니다. 제품 구현은 시작하지 않았습니다.

- [원본 기능 명세 및 전환 로드맵](docs/ANALYSIS_AND_ROADMAP.ko.md)
- [기능·설정 추적표](docs/FEATURE_CATALOG.ko.md)
- [원본 파일 지문과 분석 근거](docs/ORIGINAL_INVENTORY.ko.md)
- [원본 실행 검증 절차](docs/VALIDATION_PLAN.ko.md)
- [P0 원본 실행 조사 1차 결과와 차단 항목](docs/RUNTIME_FINDINGS.ko.md)
- [등록번호 생성 로직과 등록판 기능 조사](docs/REGISTRATION_ANALYSIS.ko.md)

2026-10-21 기준: 주요 파일작업·MCD/QCD·검색·주석·설정 저장을 조사했고, 등록번호 생성 로직을 복원해 합성 이름으로 원본 등록과 VV 실행을 검증했습니다. FAT 이미지에서 등록판 MF 포맷과 MCOPY 복사도 확인했습니다. 173개 기능의 최초 실행 추적표는 보존하며, 등록 관련 최신 결과는 위 후속 보고서를 우선합니다. P0는 진행 중이며 전체 기능 검증 완료를 뜻하지 않습니다.

원본 실행 파일, 설명서 전문, 등록정보는 이 저장소에 포함하지 않습니다. 원본 자료는 로컬 `mdir/`에서 조사합니다.
