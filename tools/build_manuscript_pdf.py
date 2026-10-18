"""Render a readable preliminary manuscript; not a journal/ABNT template."""
from pathlib import Path
import html
import re
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle,getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,KeepTogether

ROOT=Path(__file__).resolve().parents[1]

def main():
    fonts=Path('/usr/share/fonts/truetype/dejavu')
    for name,file in [('Body','DejaVuSerif.ttf'),('BodyBold','DejaVuSerif-Bold.ttf')]:
        pdfmetrics.registerFont(TTFont(name,str(fonts/file)))
    pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='Body',boldItalic='BodyBold')
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='PaperBody',fontName='Body',fontSize=10.3,leading=15.2,spaceAfter=8,alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='PaperTitle',fontName='BodyBold',fontSize=17,leading=22,spaceAfter=15,textColor=colors.HexColor('#17354B')))
    styles.add(ParagraphStyle(name='PaperHead',fontName='BodyBold',fontSize=12,leading=17,spaceBefore=13,spaceAfter=8,keepWithNext=True,textColor=colors.HexColor('#17354B')))
    styles.add(ParagraphStyle(name='PaperSmall',fontName='Body',fontSize=8.6,leading=12,spaceAfter=6))
    def inline(text):
        text=html.escape(text.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-'))
        return re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',text)
    lines=(ROOT/'paper/manuscrito.md').read_text(encoding='utf-8').splitlines()
    story=[];i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        if line.startswith('# '):story.append(Paragraph(inline(line[2:]),styles['PaperTitle']));i+=1;continue
        if line.startswith('## '):story.append(Paragraph(inline(line[3:]),styles['PaperHead']));i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=[cell.strip() for cell in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?',cell) for cell in row):rows.append(row)
                i+=1
            data=[[Paragraph(inline(cell),styles['PaperSmall']) for cell in row] for row in rows]
            table=Table(data,colWidths=[155,171,155],repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E8EFF4')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),0.7,colors.HexColor('#7293A8')),('LINEBELOW',(0,1),(-1,-1),0.25,colors.HexColor('#CEDAE1')),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
            story.extend([table,Spacer(1,8)]);continue
        paragraph=[line];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|')):paragraph.append(lines[i].strip());i+=1
        story.append(Paragraph(inline(' '.join(paragraph)),styles['PaperBody']))
    out=ROOT/'paper/manuscrito-preliminar.pdf'
    def footer(canvas,doc):
        canvas.saveState();canvas.setFont('Body',7.8);canvas.setFillColor(colors.HexColor('#536875'))
        canvas.drawString(57,30,'Versao preliminar - sem avaliacao educacional - nao submetido')
        canvas.drawRightString(A4[0]-57,30,str(doc.page));canvas.restoreState()
    doc=SimpleDocTemplate(str(out),pagesize=A4,rightMargin=57,leftMargin=57,topMargin=48,bottomMargin=51,title='Correspondencias UML, Java e estado: manuscrito preliminar',author='Autoria a confirmar')
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    print(out)

if __name__=='__main__':main()
