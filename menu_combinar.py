import streamlit as st
import pypdf
from utilidades import pegar_dados

def exibir_menu_combinar():
    st.markdown(" # Combinar PDFs")
    st.write("Selecione 2 ou mais arquivos PDF para combinar:")
    arquivos_pdf=st.file_uploader(label="Selecione os arquivos PDF para combinar...",
                                 type="pdf",
                                 accept_multiple_files=True
                                 )
    
    if arquivos_pdf:
        botoes_desativados=False
    else:
        botoes_desativados=True

    clicou_processar= st.button("Clique para processar o arquivo PDF...",
                                use_container_width=True,disabled=botoes_desativados)
    if clicou_processar:       
        arquivo_combinado=combinar_pdfs(arquivos=arquivos_pdf)
        nome_arquivo="combinado.pdf"
        st.download_button("Clique para baixar o PDF resultante...",
                           type="primary",
                           data=arquivo_combinado,
                           file_name=nome_arquivo,
                           mime="aplication/pdf",
                           use_container_width=True)

def combinar_pdfs(arquivos):
    escritor_arquivo_combinado=pypdf.PdfWriter()
    for arquivo in arquivos:
        leitura_pdfs=pypdf.PdfReader(arquivo)
        for pagina in leitura_pdfs.pages:
            escritor_arquivo_combinado.add_page(pagina)
    arquivo_combinado=pegar_dados(escritor=escritor_arquivo_combinado)
    return arquivo_combinado
