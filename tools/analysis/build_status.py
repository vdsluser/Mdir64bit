"""Build the current 173-feature ledger from preserved observation reports.

Run from any directory; --check verifies committed outputs without writing them.
Uses only the Python standard library. Historical inputs are never modified.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
BASE = 'docs/evidence/2026-10-20/runtime-status.json'
SUPPLEMENTS = [
    ('docs/evidence/2026-10-21/vv-02/status.json', 'docs/VV_RUNTIME_FINDINGS.ko.md'),
    ('docs/evidence/2026-10-21/registered-03/status.json', 'docs/REGISTERED_OPERATIONS.ko.md'),
    ('docs/evidence/2026-10-21/disk-04/status.json', 'docs/DISK_RUNTIME_FINDINGS.ko.md'),
    ('docs/evidence/2026-10-21/conflict-05/status.json', 'docs/CONFLICT_RUNTIME_FINDINGS.ko.md'),
    ('docs/evidence/2026-10-21/description-06/status.json', 'docs/DESCRIPTION_RULES.ko.md'),
    ('docs/evidence/2026-10-22/partial-07/status.json', 'docs/PARTIAL_FAILURE_FINDINGS.ko.md'),
    ('docs/evidence/2026-10-22/shell-08/status.json', 'docs/SHELL_RUNTIME_FINDINGS.ko.md'),
]
JSON_OUT = 'docs/evidence/current-status.json'
MD_OUT = 'docs/CURRENT_STATUS.ko.md'
DATE = '2026-10-22'
LABELS = {
    'PARTIAL': '부분 관찰', 'NOT_RUN': '미실행',
    'BLOCKED_TOOL': '외부 도구 차단', 'MENU_OBSERVED': '메뉴만 관찰',
    'OBSERVED_CASE': '개별 사례 관찰', 'DIFF': '문서와 차이',
    'PARTIAL_WITH_ANOMALY': '부분 관찰·예외',
}
ISSUES = {
    'VAR-011': ['P0-01'], 'TREE-003': ['P0-02', 'P0-03'],
    'DESC-001': ['P0-11'],
    'DESC-002': ['P0-03', 'P0-06', 'P0-11'], 'VAR-015': ['P0-04'],
    'CMD-001': ['P0-04'], 'FORMAT-001': ['P0-05', 'P0-10'],
    'FILE-001': ['P0-06'], 'FILE-002': ['P0-06'],
    'FILE-003': ['P0-06'], 'FILE-004': ['P0-06'],
    'FILE-006': ['P0-06'], 'ARC-002': ['P0-07'],
    'COPY-001': ['P0-10'], 'COPY-002': ['P0-10'],
    'LEGACY-004': ['P0-09'], 'DESC-003': ['P0-09'],
}


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8-sig'))


def catalog():
    rows = {}
    for line in (ROOT / 'docs/FEATURE_CATALOG.ko.md').read_text(encoding='utf-8').splitlines():
        cells = [part.strip() for part in line.split('|')[1:-1]]
        if cells and re.fullmatch(r'[A-Z]+-\d{3}', cells[0]):
            key = cells[0]
            if key in rows:
                raise ValueError(f'Duplicate catalog ID: {key}')
            title = cells[1]
            if key.startswith('SET-'):
                title += ' / ' + cells[2]
            rows[key] = title
    return rows


def observation(row, source, report, date):
    evidence = [(Path(source).parent / name).as_posix() for name in row['evidence']]
    for path in [source, report, *evidence]:
        if not (ROOT / path).is_file():
            raise ValueError(f'Missing evidence: {path}')
    return {
        'date': date, 'source': source, 'report': report,
        'status': row['status'], 'scope': row.get('scope', row.get('observed', '')),
        'evidence': evidence,
    }


def build():
    titles = catalog()
    baseline = read_json(BASE)
    features = {}
    for row in baseline['features']:
        key = row['id']
        if key in features:
            raise ValueError(f'Duplicate baseline ID: {key}')
        obs = observation(row, BASE, 'docs/RUNTIME_FINDINGS.ko.md', baseline['observed_date_seoul'])
        features[key] = {'id': key, 'title': titles[key], 'status': row['status'],
                         'scope': obs['scope'], 'observations': [obs],
                         'open_issues': ISSUES.get(key, [])}
    if set(titles) != set(features) or len(features) != 173:
        raise ValueError('Catalog/baseline ID mismatch; review new scope explicitly')

    for source, report in SUPPLEMENTS:
        data = read_json(source)
        seen = set()
        for row in data['features']:
            key = row['id']
            if key not in features or key in seen:
                raise ValueError(f'Unknown/duplicate supplement ID: {key}')
            seen.add(key)
            obs = observation(row, source, report, data['date'])
            target = features[key]
            target['observations'].append(obs)
            if row['status'] == 'UNTESTED':
                # Explicitly release the historical license blocker; do not claim
                # that unexecuted fonts/colors/resolutions have been observed.
                if target['status'] == 'BLOCKED_REGISTERED':
                    target['status'] = 'NOT_RUN'
                    target['scope'] = '등록 제한은 해소됐으나 글꼴·색상·해상도는 미실행'
            else:
                target['status'] = row['status']
                target['scope'] = obs['scope']

    # This observation is in the registration report rather than a separate
    # status supplement; keep the manual evidence mapping explicit and narrow.
    registration_source = 'docs/evidence/2026-10-21/registration-verification.json'
    registration = read_json(registration_source)
    if not registration['positive']['fresh_main_registered']:
        raise ValueError('Registration positive evidence missing')
    row = {
        'status': 'PARTIAL',
        'scope': '합성 번호의 REG 생성·새 프로세스 등록 표시와 잘못된 suffix 대조 확인; 모든 입력·설정 조합 미검증',
        'evidence': ['registration-verification.json', 'generated-about.txt'],
    }
    target = features['SET-007']
    target['observations'].append(observation(row, registration_source,
                                            'docs/REGISTRATION_ANALYSIS.ko.md', registration['date']))
    target['status'], target['scope'] = row['status'], row['scope']

    counts = Counter(item['status'] for item in features.values())
    if set(counts) - set(LABELS):
        raise ValueError(f'Unreviewed status labels: {set(counts) - set(LABELS)}')
    output = {
        'documented_date_seoul': DATE, 'stage': 'P0 in progress; P1 not yet entered',
        'feature_rows': len(features), 'fully_verified_feature_rows': 0,
        'status_semantics': 'Latest scoped observations with full history; no overall completion percentage',
        'sources': [BASE, *[path for path, _ in SUPPLEMENTS], registration_source],
        'historical_registered_blockers': 8,
        'current_registered_blockers': counts.get('BLOCKED_REGISTERED', 0),
        'summary': dict(sorted(counts.items())), 'features': list(features.values()),
    }
    lines = [
        '# 원본 기능의 현재 통합 상태', '',
        f'갱신: {DATE}. 기존 173개 ID와 관찰 이력을 유지한다. P0 진행 중이며 P1은 미진입이다.', '',
        '[미해결 항목·진입 조건](P0_REVIEW.ko.md) · [기능 정의](FEATURE_CATALOG.ko.md) · [JSON 원장](evidence/current-status.json)', '',
        '메뉴 관찰·개별 사례·부분 관찰은 기능 전체 검증이 아니다. 전체 검증 완료 행은 0개이며 완료율로 환산하지 않는다.', '',
        '과거 등록 차단 8개는 현재 차단에서 해제했다. 그중 글꼴·색상·해상도 VIEW-004는 미실행이다. 과거 차단 증거는 각 행의 관찰 이력에 남긴다.', '',
        '| 상태 | 기능 행 수 |', '|---|---:|',
    ]
    for key, value in sorted(counts.items()):
        lines.append(f'| {LABELS[key]} (`{key}`) | {value} |')
    lines += ['', '합계 173행. 아래 증거는 최신 관찰이며 이전 증거는 JSON의 observations에 보존된다.', '',
              '| ID | 기능 | 현재 상태 | 최신 관찰/증거 | 미해결 |', '|---|---|---|---|---|']
    for item in features.values():
        last = item['observations'][-1]
        report = Path(last['report']).name
        links = [f'[보고서]({report})']
        links += [f'[증거 {index}](../{path})' for index, path in enumerate(last['evidence'], 1)]
        issues = ', '.join(item['open_issues']) or '—'
        title = item['title'].replace('|', '\\|')
        lines.append(f"| {item['id']} | {title} | {LABELS[item['status']]} | {' · '.join(links)} | {issues} |")
    return {JSON_OUT: json.dumps(output, ensure_ascii=False, indent=2) + '\n',
            MD_OUT: '\n'.join(lines) + '\n'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    outputs = build()
    for name, content in outputs.items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                raise SystemExit(f'Stale output: {name}')
        else:
            path.write_text(content, encoding='utf-8', newline='\n')
    print(f'{"Checked" if args.check else "Built"} 173 feature rows with preserved evidence history')


if __name__ == '__main__':
    main()
