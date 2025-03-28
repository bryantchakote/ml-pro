import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Visualisation", layout="wide")

st.title("Visualisation")

if "df" in st.session_state:
    df = st.session_state["df"]

    num = df.select_dtypes(include=["int", "float"]).columns

    if len(num) >= 2:
        x = st.selectbox("Sélectionner la colonne pour l'axe X", options=num)
        y = st.selectbox("Sélectionner la colonne pour l'axe Y", options=num)

        fig = px.scatter(df, x=x, y=y)

        st.plotly_chart(fig)
    else:
        st.warning("Le fichier CSV doit contenir au moins deux colonnes numériques")
else:
    st.error(
        "Aucun DataFrame trouvé. Veuillez charger un fichier CSV depuis la page d'Accueil"
    )
