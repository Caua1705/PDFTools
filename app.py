import streamlit as st
from streamlit_option_menu import option_menu
import menu_extrair
import menu_combinar
import menu_marca
import menu_imagens

st.set_page_config(page_title="PDFTools",page_icon=":page_facing_up:",layout="wide")

_,col2,_=st.columns(3)
with col2:
    st.title("PDFTools")
    st.markdown("### Escolha a opção desejada abaixo:")
entradas_menu={
"Extrair Página": "file-earmark-pdf-fill",
"Combinar PDFs": "plus-square-fill",
"Adicionar marca d água": "droplet-fill",
"Imagens para PDF": "file-earmark-richtext-fill",
}
escolha=option_menu(
menu_title=None,
orientation="horizontal",
options=list(entradas_menu.keys()),
icons=list(entradas_menu.values()),
default_index=0
)
_,col2,_=st.columns(3)
with col2:
    match (escolha):
        case "Extrair Página":
            menu_extrair.exibir_menu_extrair()
        case "Combinar PDFs":
            menu_combinar.exibir_menu_combinar()
        case "Adicionar marca d água":
            menu_marca.exibir_menu_marca()
        case "Imagens para PDF":
            menu_imagens.exibir_menu_imagens()
        case _:
            st.warning("Implementar Página")
