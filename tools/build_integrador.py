"""Build the course deliverable from the supplied model and existing evidence.

Uses python-docx. Identity fields are deliberately unresolved until confirmed.
"""
from pathlib import Path
import json
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
TITLE = 'Ferramenta visual para acompanhar objetos em programas Java'

def build():
    sections = json.loads((ROOT/'paper/secoes-abcd.json').read_text())
    d = Document()
    sec = d.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.top_margin = sec.bottom_margin = sec.left_margin = sec.right_margin = Cm(2)
    for name in ['Normal', 'Title', 'Heading 1', 'Heading 2', 'Heading 3']:
        st = d.styles[name]
        st.font.name = 'Arial'
        st.font.size = Pt(12)
        st.font.color.rgb = RGBColor(0, 0, 0)
        st.paragraph_format.line_spacing = 1.5
        st.paragraph_format.space_after = Pt(6)
    d.styles['Normal'].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    for st in d.styles:
        for border in st.element.xpath('.//w:pBdr'):
            border.getparent().remove(border)
    for name in ['Heading 1', 'Heading 2', 'Heading 3']:
        d.styles[name].font.bold = True
        d.styles[name].paragraph_format.keep_with_next = True
        d.styles[name].paragraph_format.space_before = Pt(12)
    pending_page = False
    def apply_page(p):
        nonlocal pending_page
        if pending_page:
            p.paragraph_format.page_break_before = True
            pending_page = False
        return p
    def para(t='', style=None):
        return apply_page(d.add_paragraph(t, style))
    def centered(t, before=0, bold=False, style=None):
        p=para(t,style);p.alignment=WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before=Pt(before)
        if not style:
            for r in p.runs: r.bold=bold
        return p
    def head(t,level=1):
        p=apply_page(d.add_heading(t,level));p.alignment=WD_ALIGN_PARAGRAPH.LEFT
        return p
    def page():
        nonlocal pending_page
        pending_page = True
    centered('ESCOLA [NOME A CONFIRMAR]',40,True)
    centered('CURSO TÉCNICO EM [NOME A CONFIRMAR]',0,True)
    centered('PROJETO INTEGRADOR',0,True)
    centered(TITLE.upper(),150,style='Title')
    centered('[CIDADE A CONFIRMAR]\nOUTUBRO DE 2026',205)
    page()
    centered('ALUNOS [NOMES A CONFIRMAR]',40,True)
    centered('PROFESSOR [NOME A CONFIRMAR]',0,True)
    centered(TITLE.upper(),150,style='Title')
    centered('[CIDADE A CONFIRMAR]\nOUTUBRO DE 2026',225)
    page()
    centered('SUMÁRIO',0,True)
    toc = [
        ('1 INTRODUÇÃO','intro'),('1.1 OBJETIVOS','obj'),
        ('1.1.1 Objetivo Geral','geral'),('1.1.2 Objetivos Específicos','especificos'),
        ('1.2 METODOLOGIA','metodo'),('2 REFERENCIAL TEÓRICO','teoria'),
        ('3 CONSIDERAÇÕES FINAIS','fim'),('4 REFERÊNCIAS','refs'),
        ('APÊNDICE A Verificação técnica do demonstrador','apendice'),('ANEXOS','anexos')]
    page_numbers = dict(zip([mark for _,mark in toc], [4,4,4,4,5,6,8,9,10,11]))
    pagination = ROOT/'paper/paginacao-integrador.json'
    if pagination.exists(): page_numbers.update(json.loads(pagination.read_text())['pages'])
    for label,mark in toc:
        p=para(label+'\t');p.alignment=WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.tab_stops.add_tab_stop(Cm(17), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        f=OxmlElement('w:fldSimple');f.set(qn('w:instr'),'PAGEREF '+mark+' \\h')
        r=OxmlElement('w:r');t=OxmlElement('w:t');t.text=str(page_numbers[mark]);r.append(t);f.append(r);p._p.append(f)
    marks={label:mark for label,mark in toc}
    count=0
    def marked(t,level=1):
        nonlocal count
        p=head(t,level);count+=1
        b=OxmlElement('w:bookmarkStart');b.set(qn('w:id'),str(count));b.set(qn('w:name'),marks[t])
        e=OxmlElement('w:bookmarkEnd');e.set(qn('w:id'),str(count));p._p.insert(0,b);p._p.append(e)
    page();marked('1 INTRODUÇÃO')
    for paragraph in sections['introducao']: para(paragraph)
    marked('1.1 OBJETIVOS',2)
    marked('1.1.1 Objetivo Geral',3)
    para('Desenvolver e verificar uma ferramenta visual que mostre como as instruções de um programa Java alteram os dados de contas de exemplo.')
    marked('1.1.2 Objetivos Específicos',3)
    para('Relacionar estudos recentes sobre diagramas e visualização de programas às escolhas da ferramenta.')
    para('Implementar e testar situações de alteração e compartilhamento de dados, registrando os resultados e os limites observados.')
    marked('1.2 METODOLOGIA',2)
    for paragraph in sections['metodologia']: para(paragraph)
    page();marked('2 REFERENCIAL TEÓRICO')
    for subsection in sections['referencial']:
        head(subsection['titulo'],2)
        for paragraph in subsection['paragrafos']: para(paragraph)
    page();marked('3 CONSIDERAÇÕES FINAIS')
    for paragraph in sections['consideracoes']: para(paragraph)
    page();marked('4 REFERÊNCIAS')
    references=json.loads((ROOT/'paper/referencias-integrador.json').read_text())
    for item in references:
        p=para(item['reference']);p.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.LEFT
    page();marked('APÊNDICE A Verificação técnica do demonstrador')
    para('O demonstrador está em prototype/ no repositório aloisiocosta-professor/trama-ide-web. Os testes usam dados de exemplo, sem registros de pessoas participantes. Os números abaixo representam verificações de software, não quantidade de estudantes.')
    head('Cenários e resultados',2)
    para('A execução inicial 39083293325 do GitHub Actions corresponde ao commit 5cf946e5a77439c3c41759536c006d6d8a2e3810. Nela passaram 28 verificações Java e cinco testes Python do gerador. A execução 39104951676 corresponde ao commit 89a84aa3132eb6c369a2dfe7ff2057716fe4b0df e acrescenta nove verificações gráficas de janela, controles, legibilidade, respostas e exportação. Os dois conjuntos são evidências de versões diferentes, preservadas separadamente.')
    para('O cenário principal cria duas contas, seleciona uma delas, registra uma previsão e executa um depósito de 25 sobre um saldo inicial de 100. O saldo dessa conta passa a 125, enquanto a outra instância mantém seu saldo de 20. Os testes também conferem alias e rejeições; o cenário principal não representa todos os comportamentos possíveis.')
    head('Como conferir as evidências',2)
    para('O comando python tools/build_research.py requer JDK 17, Python e xvfb-run para as verificações gráficas em Linux. Os logs, resultados e imagens das execuções citadas estão em docs/research/evidence/ci-5cf946/ e docs/research/evidence/ci-89a84a/. O README do protótipo documenta execução interativa e limitações. A compilação foi verificada no ambiente remoto descrito nos logs.')
    para('Repositório: https://github.com/aloisiocosta-professor/trama-ide-web/tree/docs/research-bootstrap . Execuções: https://github.com/aloisiocosta-professor/trama-ide-web/actions/runs/39083293325 e https://github.com/aloisiocosta-professor/trama-ide-web/actions/runs/39104951676 .')
    para('Houve assistência de inteligência artificial na organização textual e no desenvolvimento dos materiais. Cabe aos autores conferir fontes, compreender o funcionamento, revisar o texto e assumir responsabilidade pela entrega. A forma de declaração deve observar as regras da escola.')
    page();marked('ANEXOS')
    para('Não foram incorporados documentos de terceiros ao corpo desta versão. O modelo institucional enviado orientou a estrutura e a formatação. As fontes bibliográficas utilizadas estão identificadas nas referências; seus textos integrais não foram reproduzidos.')
    d.core_properties.title=TITLE
    d.core_properties.author=''
    d.core_properties.subject='Projeto Integrador'
    d.core_properties.comments=''
    out=ROOT/'paper/projeto-integrador-versao-revisao.docx'
    d.save(out)
    return out

if __name__=='__main__': print(build())
