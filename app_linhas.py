import os 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# conversão de milimitros para pontos
def mm2p(milimetros):
    return milimetros / 0.352777



cnv = canvas.Canvas("Meu_pdf_linha.pdf",pagesize=A4)  # Nome do arquivo a ser gerado

#cnv.drawString(mm2p(100), mm2p(150),"Teste de geração de PDF")  # Texto impresso no arquivo
cnv.line(mm2p(100),mm2p(150),mm2p(120),mm2p(160))

print(os.path.basename(__file__))

cnv.save()


