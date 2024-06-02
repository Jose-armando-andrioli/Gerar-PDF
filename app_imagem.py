from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

nomes = ['José Armando','Bruno', 'Silvia']

# conversão de milimitros para pontos
def mm2p(milimetros):
    return milimetros / 0.352777



cnv = canvas.Canvas("Meu_pdf_imagem.pdf",pagesize=A4)  # Nome do arquivo a ser gerado

#cnv.drawString(mm2p(100), mm2p(150),"Teste de geração de PDF")  # Texto impresso no arquivo
cnv.drawImage("Silvia Eu Laurinha.jpg", 50,400,300,300  )

cnv.save()


