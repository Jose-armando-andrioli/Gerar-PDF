from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

nomes = ['José Armando','Bruno', 'Silvia']

# conversão de milimitros para pontos
def mm2p(milimetros):
    return milimetros / 0.352777

eixo = 290

cnv = canvas.Canvas("Meu_pdf_texto.pdf",pagesize=A4)  # Nome do arquivo a ser gerado
for nome in nomes:
    cnv.drawString(mm2p(20), mm2p(eixo),nome) # Texto impresso no arquivo
    eixo -= 10  # Inicio de cima para baixo

cnv.save()


