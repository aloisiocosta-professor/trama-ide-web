"""Audit a real GitHub snapshot. Does not close issues or infer acceptance."""
import argparse
import json
from pathlib import Path
from research_governance import assess_completion

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('snapshot',type=Path)
    parser.add_argument('hierarchy',type=Path)
    parser.add_argument('output',type=Path)
    parser.add_argument('--require-complete',action='store_true')
    args=parser.parse_args()
    snapshot=json.loads(args.snapshot.read_text(encoding='utf-8'))
    hierarchy=json.loads(args.hierarchy.read_text(encoding='utf-8'))
    assert snapshot['root']['number']==hierarchy['parent_issue']
    result=assess_completion(snapshot['root'],snapshot['descendants'],hierarchy['children'])
    result.update({'observed_at':snapshot['observed_at'],'repository':snapshot['repository'],'root_issue':snapshot['root']['number'],'completed_descendants':sum(i['state']=='closed' and i.get('state_reason')=='completed' for i in snapshot['descendants']),'descendants':len(snapshot['descendants']),'limits':'GitHub state audit; individual scientific acceptance evidence remains in each issue.'})
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))
    if args.require_complete and result['status']!='complete':raise SystemExit(2)

if __name__=='__main__':main()
