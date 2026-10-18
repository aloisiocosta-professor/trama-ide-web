"""Pure audit rules: consistency is distinct from historical preservation/completion."""
import re
from pathlib import PurePosixPath

MANIFEST = 'docs/research/inventario.json'

def governed(path):
    return path != MANIFEST and (path == 'AGENTS.md' or path.startswith(('docs/research/', 'docs/session/', 'prototype/', 'tools/', 'paper/', '.github/')))

def validate_inventory(tree_paths, entries):
    expected = {path for path in tree_paths if governed(path)}
    listed = []
    for item in entries:
        path = item['path']
        if PurePosixPath(path).is_absolute() or '..' in PurePosixPath(path).parts:
            raise ValueError('Unsafe manifest path: '+path)
        if not re.fullmatch('[0-9a-f]{64}', item['sha256']):
            raise ValueError('Invalid SHA-256: '+path)
        listed.append(path)
    if len(set(listed)) != len(listed): raise ValueError('Duplicate manifest path')
    missing = expected - set(listed)
    extra = set(listed) - expected
    if missing or extra:
        raise ValueError('Inventory coverage: missing='+str(sorted(missing))+' extra='+str(sorted(extra)))
    return len(expected)

def conventional(title):
    return bool(re.match(r'^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\([^)]+\))?!?: .+',title))

def assess_completion(root, descendants, expected_numbers):
    """Status only. The function never closes issues or invents acceptance evidence."""
    actual = {issue['number']: issue for issue in descendants}
    missing = sorted(set(expected_numbers)-set(actual))
    unresolved = [{'number':issue['number'],'state':issue['state'],'state_reason':issue.get('state_reason')} for issue in [root,*descendants] if not (issue['state']=='closed' and issue.get('state_reason')=='completed')]
    return {'status':'complete' if not missing and not unresolved else 'incomplete','missing_issues':missing,'unresolved_issues':unresolved,'completion_requires':'all scoped issues including parent closed with state_reason=completed'}
