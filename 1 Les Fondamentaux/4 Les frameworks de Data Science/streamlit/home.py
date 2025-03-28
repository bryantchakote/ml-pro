import streamlit as st
import pandas as pd

st.set_page_config(page_title="Accueil", page_icon=":house:", layout="wide")

st.title("Accueil")

if "compteur" not in st.session_state:
    st.session_state["compteur"] = 0

if st.button("Incrémenter"):
    st.session_state["compteur"] += 1

st.write(f"Valeur du compteur : {st.session_state["compteur"]}")


st.write("---")

compteur_sans_session = 0

if st.button("Incrémenter (sans session)"):
    compteur_sans_session += 1

st.write(f"Valeur du compteur (sans session): {compteur_sans_session}")

st.write("---")


st.subheader("Chargement de fichier CSV")

uploaded_file = st.file_uploader("Choisissez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state["df"] = df
    st.success("Fichier CSV chargé avec succès")
    st.write(df.head())
else:
    st.info("Veuillez charger un fichier CSV pour l'utiliser dans l'application")

# NO OK
