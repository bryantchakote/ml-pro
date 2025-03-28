import streamlit as st

st.set_page_config(page_title="Reset", layout="wide")

st.title("Reset")

if st.button("Réinitialiser le compteur"):
    st.session_state["compteur"] = 0
    st.success("Le compteur a été réinitialisé")

if st.button("Réinitialiser le sélection"):
    st.session_state["selection"] = []
    st.success("La sélection a été réinitialisée")
