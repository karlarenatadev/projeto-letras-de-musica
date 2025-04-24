import requests
import streamlit as st

def buscar_letra(banda, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra
    
    
st.image("https://i.imgur.com/SmktDIH.png")
st.title("Letras de músicas")

banda = st.text_input("Digite o nome da banda ou artista:", key="banda")
musica = st.text_input("Digite o nome da música:", key="musica")
pesquisar = st.button("Pesquisar")

if pesquisar: 
    letra = buscar_letra(banda, musica)
    if letra:
        st.success("Letra encontrada!")
        st.text(letra)
    else:
        st.error("Erro ao buscar a letra. Verifique os dados e tente novamente.")