import streamlit as st

st.title('Exemplo de Imagem no Streamlit')
radio_selecionado = st.radio('Selecione a variedade',["Setosa","Versicolor",'Virginica'],horizontal=True)
if radio_selecionado == 'Setosa':
   # Carregando e exibindo a imagem
   imagem_1 = 'setosa.png'
   st.image(imagem_1, width=300)
elif radio_selecionado == 'Versicolor':
   imagem_2 = 'versicolor.png'
   st.image(imagem_2, width=300)
else:
   'Virginica'
   imagem_3 = 'virginica.png'
   st.image(imagem_3, width=300)
