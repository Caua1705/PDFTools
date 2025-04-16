import streamlit as st
import pypdf
from utilidades import pegar_dados
from pathlib import Path

def exibir_menu_marca():
    st.markdown("# Adicionar marca d'água")
    st.write("Selecione um arquivo PDF e uma marca d'água nos seletores abaixo:")
    arquivo_pdf=st.file_uploader(label="Selecione o arquivo PDF",
                     type="pdf",
                     accept_multiple_files=False,
                     )
    arquivo_marca=st.file_uploader(label="Selecione o arquivo contendo a marca d'água:",
                     type="pdf",
                     accept_multiple_files=False,
                     )
    if arquivo_pdf and arquivo_marca:
        botao_desativado=False
    else:
        botao_desativado=True
    clicou_processar=st.button("Clique para processar o arquivo PDF...",use_container_width=True,disabled=botao_desativado)
    if clicou_processar:
        arquivo_completo=adicionar_marca(pdf=arquivo_pdf,marca=arquivo_marca)
        nome_arquivo=f"{Path(arquivo_pdf.name).stem}_marca.pdf"
        st.download_button("Clique para baixar o arquivo PDF resultante...",
                          file_name=nome_arquivo,
                          mime="application/pdf",
                          data=arquivo_completo,
                          type="primary",
                          use_container_width=True)

def adicionar_marca(pdf,marca):
    leitor_marca=pypdf.PdfReader(marca).pages[0]
    escritor_arquivo=pypdf.PdfWriter(clone_from=pdf)
    for pagina in escritor_arquivo.pages:
        escala_x= pagina.mediabox.width / leitor_marca.mediabox.width
        escala_y= pagina.mediabox.height / leitor_marca.mediabox.height
        transf= pypdf.Transformation().scale(escala_x,escala_y)
        pagina.merge_transformed_page(leitor_marca,transf,over=False)
    arquivo_completo=pegar_dados(escritor=escritor_arquivo)
    return arquivo_completo