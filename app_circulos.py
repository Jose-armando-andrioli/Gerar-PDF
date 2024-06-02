from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

nomes = ['José Armando','Bruno', 'Silvia']

# conversão de milimitros para pontos
def mm2p(milimetros):
    return milimetros / 0.352777



cnv = canvas.Canvas("Meu_pdf_circulos.pdf",pagesize=A4)  # Nome do arquivo a ser gerado

#cnv.drawString(mm2p(100), mm2p(150),"Teste de geração de PDF")  # Texto impresso no arquivo
cnv.circle(mm2p(100),mm2p(150),mm2p(10))

cnv.save()


