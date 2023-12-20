import streamlit as st

st.title('Exemplo de Imagem no Streamlit')
radio_selecionado = st.radio('Selecione a variedade',["Setosa","Versicolor",'Virginica'],horizontal=True)
if radio_selecionado == 'Setosa':
   # Carregando e exibindo a imagem
   imagem = 'aula-05/setosa.png'
   st.image(imagem, width=300)