"""Validacao tecnica: nunca gera dados de participantes ou medidas de aprendizagem."""
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'validation'

def run(args, cwd=ROOT):
    result=subprocess.run(args,cwd=cwd,text=True,encoding='utf-8',capture_output=True)
    print(result.stdout,end='')
    print(result.stderr,end='',file=sys.stderr)
    if result.returncode: raise subprocess.CalledProcessError(result.returncode,args)
    return result.stdout+result.stderr

def main():
    OUT.mkdir(exist_ok=True)
    if not shutil.which('javac') or not shutil.which('java'):
        raise SystemExit('JDK com javac/java necessario; nenhum software sera instalado pelo script.')
    compiler=run(['javac','-version']).strip()
    runtime=run(['java','-version']).strip()
    tests=run([sys.executable,'-m','unittest','-v','test_generator'],ROOT/'prototype')
    generated=OUT/'generated'
    if generated.exists():shutil.rmtree(generated)
    generated.mkdir()
    run([sys.executable,'prototype/generate.py','prototype/model.json',str(generated/'BankAccount.java')])
    run(['javac','--release','17','-encoding','UTF-8','-d',str(generated/'classes'),str(generated/'BankAccount.java')])
    classes=OUT/'classes'
    if classes.exists():shutil.rmtree(classes)
    classes.mkdir()
    sources=sorted((ROOT/'prototype/src').glob('*.java'))
    compile_log=run(['javac','--release','17','-encoding','UTF-8','-d',str(classes),*[str(p) for p in sources]])
    test_log=run(['java','-Djava.awt.headless=true','-cp',str(classes),'LabChecks',str(ROOT/'prototype/src/BankAccount.java'),str(OUT)])
    result=json.loads((OUT/'technical-results.json').read_text())
    result.update({
        'timestamp_utc':datetime.now(timezone.utc).isoformat(),
        'compiler':compiler,'runtime':runtime,'os':platform.platform(),
        'generator_tests':5,
        'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        'limits':['No participants','No learning effects measured','Offscreen UI only','Restricted fixture, not full IDE'],
    })
    (OUT/'technical-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    (OUT/'test-log.txt').write_text(tests+'\n'+compile_log+'\n'+test_log,encoding='utf-8')
    (OUT/'README.md').write_text('# Resultados tecnicos\n\nExecucao de testes deterministas e renderizacao fora da tela. Zero participantes.\nNao sao resultados de aprendizagem, piloto educacional ou usabilidade.\n',encoding='utf-8')
    print(json.dumps({'status':'pass','java_checks':result['checks'],'generator_tests':5,'participants':0}))

if __name__=='__main__':main()
