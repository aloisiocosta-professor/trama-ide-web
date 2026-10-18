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
    d.styles['Normal'].paragraph_format.keep_together = True
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
    para(sections['objetivo_geral'])
    marked('1.1.2 Objetivos Específicos',3)
    for paragraph in sections['objetivos_especificos']: para(paragraph)
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
    def records_table(rows):
        # Own observations and administrative records are not bibliographic arguments.
        table=d.add_table(rows=0, cols=2)
        table.autofit=False
        table.columns[0].width=Cm(3.3)
        table.columns[1].width=Cm(13.7)
        table.style='Table Grid'
        for label,value in rows:
            cells=table.add_row().cells
            for cell,text in zip(cells,[label,value]):
                cell.text=text
                for p in cell.paragraphs:
                    p.alignment=WD_ALIGN_PARAGRAPH.LEFT
                    p.paragraph_format.space_after=Pt(4)
                    p.paragraph_format.line_spacing=1.5
            for r in cells[0].paragraphs[0].runs: r.bold=True
            trPr=table.rows[-1]._tr.get_or_add_trPr()
            trPr.append(OxmlElement('w:cantSplit'))
        return table
    records_table([
        ('Natureza', 'Registros próprios de testes de software, com contas fictícias e sem participantes. Os números não representam estudantes.'),
        ('Versão inicial', 'Execução 39083293325; commit 5cf946e5a77439c3c41759536c006d6d8a2e3810. Aprovadas 28 verificações Java e cinco testes Python do gerador. Evidências: docs/research/evidence/ci-5cf946/.'),
        ('Versão posterior', 'Execução 39104951676; commit 89a84aa3132eb6c369a2dfe7ff2057716fe4b0df. Aprovadas nove verificações de interface e exportação. Evidências: docs/research/evidence/ci-89a84a/. São versões distintas.'),
        ('Cenários', 'Depósito de 25 sobre 100: saldo 125; outra conta mantém 20. Também foram conferidos dois nomes para a mesma conta e recusas de operações. O conjunto é restrito aos casos testados.'),
        ('Reprodução', 'Comando: python tools/build_research.py. Requisitos: JDK 17, Python e xvfb-run em Linux. Orientações interativas e limites: prototype/README.md. Ambiente remoto identificado nos logs preservados.'),
        ('Localização', 'Repositório: https://github.com/aloisiocosta-professor/trama-ide-web/tree/docs/research-bootstrap . Execuções disponíveis na aba Actions pelos números acima.'),
        ('Autoria e apoio', 'Houve assistência de inteligência artificial na organização textual e nos materiais. Conferência, compreensão e responsabilidade pela entrega cabem aos autores, observadas as regras da escola.')
    ])
    page();marked('ANEXOS')
    records_table([
        ('Modelo', 'A estrutura foi orientada pelo modelo enviado, preservado como paper/modelo-entrega-original.docx.'),
        ('Fontes externas', 'Os PDFs dos artigos não foram incorporados ao trabalho. A versão efetivamente consultada está identificada nas referências e no registro de leitura.'),
        ('Identificação', 'Escola, curso específico, alunos, professor e cidade aguardam confirmação. Este arquivo é uma versão para revisão.')
    ])
    d.core_properties.title=TITLE
    d.core_properties.author=''
    d.core_properties.subject='Projeto Integrador'
    d.core_properties.comments=''
    out=ROOT/'paper/projeto-integrador-versao-revisao.docx'
    d.save(out)
    return out

if __name__=='__main__': print(build())
