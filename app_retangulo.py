from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

nomes = ['José Armando','Bruno', 'Silvia']

# conversão de milimitros para pontos
def mm2p(milimetros):
    return milimetros / 0.352777



cnv = canvas.Canvas("Meu_pdf_retangolo.pdf",pagesize=A4)  # Nome do arquivo a ser gerado


cnv.rect(200,250,300,350)

cnv.save()


