import streamlit as st

st.set_page_config(page_title="Résumé", layout="wide")

st.title("Résumé")

st.subheader("Valeur du compteur")

if "compteur" in st.session_state:
    st.write(f'Le compteur est à : {st.session_state["compteur"]}')
else:
    st.write("Le compteur n'a pas encore été initialisé")

st.subheader("Sélection d'options")

if "selection" in st.session_state and st.session_state["selection"]:
    st.write(
        f'Vous avez sélectionné les options suivantes : {st.session_state["selection"]}'
    )
else:
    st.write("Aucune option n'a été sélectionnée")
