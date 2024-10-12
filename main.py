import streamlit as st

# Setting page layout to wide
st.set_page_config(layout="wide", page_title="Rolox Letter", page_icon="images/rolox.png")

col3, col4 = st.columns([2,4])

with col3:
    st.image("images/rolox.png", caption="Rolox")

with col4:
    with open("letter.txt", 'r', encoding="utf-8") as file:
        carta = file.read()
    st.info(carta)




