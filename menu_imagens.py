import streamlit as st
import pypdf
from pathlib import Path
from utilidades import pegar_dados
from PIL import Image
import tempfile 

def exibir_menu_imagens():
    st.markdown(" # Imagens para PDF")
    st.write("Selecione as imagens para gerar um arquivo PDF com elas:")
    imagens=st.file_uploader(label="Selecione as imagens que irão para o arquivo PDF...",
                                 type=["png","jpg","jpeg"],
                                 accept_multiple_files=True
                                 )
    if imagens:
        botoes_desativados=False
    else:
        botoes_desativados=True
    clicou_processar= st.button("Clique para processar o arquivo PDF...",
                                use_container_width=True,disabled=botoes_desativados)
    if clicou_processar:
        pdf_gerado=gerar_arquivo_pdf_com_imagens(imagens=imagens)
        nome_arquivo="imagens.pdf"
        st.download_button("Clique para baixar o arquivo PDF resultante...",
                           type="primary",
                           data=pdf_gerado,
                           file_name=nome_arquivo,
                           mime="application/pdf",
                           use_container_width=True)
#gerar_arquivo_pdf_com_imagens:                         
def gerar_arquivo_pdf_com_imagens(imagens):
    imagens_pillow = []
    for imagem in imagens:
        dados_imagem = Image.open(imagem)
        imagens_pillow.append(dados_imagem)
    primeira_imagem = imagens_pillow[0]
    demais_imagens = imagens_pillow[1:]

    with tempfile.TemporaryDirectory() as tempdir:
        nome_arquivo = Path(tempdir) / 'temp.pdf'
        primeira_imagem.save(nome_arquivo, save_all=True, append_images=demais_imagens)
        pdf_imagens = pypdf.PdfReader(nome_arquivo)

    # Passar imagens para um novo PDF em branco, ajustando a dimensão e posicionamento
    escritor = pypdf.PdfWriter()
    for pagina in pdf_imagens.pages:
        pagina_em_branco = escritor.add_blank_page(
            width=pypdf.PaperSize.A4.width,
            height=pypdf.PaperSize.A4.height,
        )
        # Ajuste dimensões
        if pagina.mediabox.top > pagina.mediabox.right:  # Imagem está na vertical
            scale = pagina_em_branco.mediabox.top / pagina.mediabox.top * 0.9
        else:  # Imagem está na horizontal (ou é quadrada)
            scale = pagina_em_branco.mediabox.right / pagina.mediabox.right * 0.9
        # Ajuste posicionamento
        tx = (pagina_em_branco.mediabox.right - pagina.mediabox.right * scale) / 2
        ty = (pagina_em_branco.mediabox.top - pagina.mediabox.top * scale) / 2
        transformation = pypdf.Transformation().scale(scale).translate(tx=tx, ty=ty)
        pagina_em_branco.merge_transformed_page(pagina, transformation, over=True)
    dados_pdf = pegar_dados(escritor=escritor)
    return dados_pdf

