import streamlit as st
import pypdf
from pathlib import Path
from utilidades import pegar_dados

def exibir_menu_extrair():
    st.markdown(" # Extrair Página PDF")
    st.write("Escolha um arquivo PDF para extrair uma página:")
    arquivo_pdf=st.file_uploader(label="Selecione o arquivo PDF...",
                                 type="pdf",
                                 accept_multiple_files=False
                                 )
    if arquivo_pdf:
        botoes_desativados=False
    else:
        botoes_desativados=True

    numero_pagina= st.number_input("Página para extrair", min_value=1,disabled=botoes_desativados)
    clicou_processar= st.button("Clique para processar o arquivo PDF...",
                                use_container_width=True,disabled=botoes_desativados)
    if clicou_processar:
        dados_pdf=extrair_pagina_pdf(file=arquivo_pdf, number_page=numero_pagina)
        if dados_pdf is None:
            st.warning(f"PDF não possui página de número: {numero_pagina}")
            return
        nome_arquivo=f"{Path(arquivo_pdf.name).stem}_pg{numero_pagina:03d}.pdf"
        st.download_button("Clique para baixar o arquivo PDF...",
                           type="primary",
                           data=dados_pdf,
                           file_name=nome_arquivo,
                           mime="aplication/pdf",
                           use_container_width=True)
#Função de extrair página:                         
def extrair_pagina_pdf(file,number_page):
    leitura_arquivo=pypdf.PdfReader(file)
    try:
        pagina_arquivo=leitura_arquivo.pages[number_page-1]
    except IndexError:
        return None
    escritor_arquivo=pypdf.PdfWriter()
    escritor_arquivo.add_page(pagina_arquivo)
    dados_pdf=pegar_dados(escritor=escritor_arquivo)
    return dados_pdf