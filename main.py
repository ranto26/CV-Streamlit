from content.constant import FIRST_NAME, LAST_NAME, TITRE, AGE, EMAIL, NUMBER, PLACE
from utils.fonctions import project_info, exp_info, skill_info, school_info
import streamlit as st

st.set_page_config(
    page_title=f"CV - {FIRST_NAME} {LAST_NAME}", page_icon=f"📄", layout="wide"
)

st.header(f"{FIRST_NAME} {LAST_NAME}", text_alignment="center")
st.subheader(TITRE, text_alignment="center")

gauche, centre, droite = st.columns(3)

with gauche:
    st.markdown(f"#### :birthday: {AGE} ans", text_alignment="center")

with centre:
    st.markdown(f"##### :email: {EMAIL}", text_alignment="center")
    st.markdown(f"##### :telephone_receiver: {NUMBER}", text_alignment="center")

with droite:
    st.markdown(f"#### :house: {PLACE}", text_alignment="center")

## Projets
st.header(":paperclip: Projets")
st.markdown(project_info())
st.divider()

st.header(":man_scientist: Expériences professionelles")
st.markdown(exp_info())
st.divider()

st.header(":toolbox: Compétences")
st.markdown(skill_info())
st.divider()

st.header(":school: Formations")
st.markdown(school_info())
