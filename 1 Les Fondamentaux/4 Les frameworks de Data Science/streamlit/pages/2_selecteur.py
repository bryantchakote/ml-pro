import streamlit as st

st.set_page_config(page_title="Sélection", layout="wide")

st.title("Sélection")

if "selection" not in st.session_state:
    st.session_state["selection"] = []

st.subheader("Sélection actuelle")

selection_placeholder = st.empty()

st.subheader("Ajouter une option")

option = st.selectbox(
    "Choisissez une option à ajouter",
    ["A", "B", "C"],
    key="add_selectbox",
)

if st.button("Ajouter à la sélection", key="add_button"):
    if option not in st.session_state["selection"]:
        st.session_state["selection"].append(option)
        st.success(f"Option {option} ajoutée à la sélection")
    else:
        st.warning(f"Option {option} est déjà dans la sélection")

st.subheader("Supprimer une option")

if st.session_state["selection"]:
    remove_option = st.selectbox(
        "Choisissez une option à supprimer",
        st.session_state["selection"],
        key="remove_selectbox",
    )

    if st.button("Supprimer de la sélection", key="remove_button"):
        st.session_state["selection"].remove(remove_option)
        st.success(f"Option {remove_option} supprimée de la sélection")
else:
    st.info(f"Aucune option à supprimer")

if st.session_state["selection"]:
    selection_placeholder.write(st.session_state["selection"])
else:
    selection_placeholder.write("Aucune option sélectionnée.")
