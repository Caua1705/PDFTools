import tempfile
from pathlib import Path

#Criando um diretorio temporario,escrevendo o arquivo recebido nesse diretório e 
#lendo o arquivo no diretório
def pegar_dados(escritor):
    with tempfile.TemporaryDirectory() as diretorio_temporario:     
        diretorio_temporario_pdf= Path(diretorio_temporario) / "arquivo_temporario.pdf"
        escritor.write(diretorio_temporario_pdf)
        with open(diretorio_temporario_pdf, mode="rb") as output_pdf:
            pdf_data=output_pdf.read()
    return pdf_data