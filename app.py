import streamlit as st


st.header('Taulant')
name = st.text_input('Emri')
st.write('Emri juaj eshte ', name)
st.button('Contact')