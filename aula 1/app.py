import streamlit as st

st.title('CALCULADORA')

n1 = st.number_input('numero:')
n2 = st.number_input('numero:', value = 0.0)

soma, sub, div, mult = st.columns(4)
if  st.button('Soma'):
    calcular   =  n1  + n2 
    st.success(calcular)
elif st.button('subtração'):    
    calcular   =  n1  - n2 
    st.success(calcular)    
elif st.button('Divisão'):    
    calcular   =  n1  / n2 
    st.success(calcular)       
elif st.button('Multiplicação'):    
    calcular   =  n1  * n2 
    st.success(calcular)    


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------


st.title('desafio 1: o cartão de visitas digital')

st.header('cartão de visita')

st.text('isso é um texto em streamlit')

st.markdown('isso é um paragrafo de comentario')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.title('desafio 2: formulario de cadastro de usuario')

st.text_input('nome')

st.number_input('idade')

st.checkbox('termos de uso')

if  st.button('enviar'):
    st.success('')
    st.success('')
    st.success('')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import streamlit as st 

st.title('Desafio 3: Seletor de Cursos')

st.selectbox('escolha um curso',('Python', 'Web'),)
st.multiselect('escolha uma tecnologia',
['HTML', 'CSS', 'SQL', 'Git'],)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.title('Desafio 4: Visualizador de Planilhas alternativo')

st.dataframe
st.table


    


