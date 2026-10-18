"""Gerador estrutural restrito: corpos sao preenchidos pelo programador."""
import argparse
import json
import re
from pathlib import Path

KEYWORDS = set('abstract assert boolean break byte case catch char class const continue default do double else enum extends final finally float for goto if implements import instanceof int interface long native new package private protected public return short static strictfp super switch synchronized this throw throws transient try void volatile while true false null record var yield sealed permits non-sealed'.split())
TYPES = {'BigDecimal', 'String', 'int', 'long', 'boolean', 'void'}

def identifier(value):
    if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z_$][A-Za-z0-9_$]*', value) or value in KEYWORDS:
        raise ValueError('Identificador Java invalido')
    return value

def typename(value, allow_void=False):
    if value not in TYPES or (value == 'void' and not allow_void):
        raise ValueError('Tipo fora do subconjunto')
    return value

def parameters(items):
    seen=set()
    values=[]
    for item in items:
        name=identifier(item['name'])
        if name in seen: raise ValueError('Parametro duplicado')
        seen.add(name)
        values.append(typename(item['type'])+' '+name)
    return ', '.join(values)

def generate(model):
    name=identifier(model['class'])
    lines=['import java.math.BigDecimal;', '', 'public final class '+name+' {']
    fields=set()
    for attribute in model['attributes']:
        field=identifier(attribute['name'])
        if field in fields: raise ValueError('Atributo duplicado')
        fields.add(field)
        visibility=attribute['visibility']
        if visibility not in {'private','public','protected'}: raise ValueError('Visibilidade invalida')
        lines.append('    '+visibility+' '+typename(attribute['type'])+' '+field+';')
    lines+=['', '    public '+name+'('+parameters(model['constructor'])+') {', '        throw new UnsupportedOperationException("TODO: implementar construtor");', '    }']
    methods=set()
    for method in model['methods']:
        member=identifier(method['name'])
        if member in methods: raise ValueError('Sobrecarga/duplicacao fora do subconjunto')
        methods.add(member)
        lines+=['', '    public '+typename(method['return'],True)+' '+member+'('+parameters(method['parameters'])+') {', '        throw new UnsupportedOperationException("TODO: implementar metodo");', '    }']
    return '\n'.join(lines+['}', ''])

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('model',type=Path)
    parser.add_argument('output',type=Path)
    args=parser.parse_args()
    model=json.loads(args.model.read_text(encoding='utf-8'))
    output=generate(model)
    if args.output.name != model['class']+'.java': raise ValueError('Nome do arquivo difere da classe')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x',encoding='utf-8') as file: file.write(output)

if __name__=='__main__': main()
