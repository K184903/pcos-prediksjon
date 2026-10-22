import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PCOS-prediksjon",
)

st.title("PCOS prediksjon")

st.write(
    "Svar på følgende spørsmål og få svar om du burde se en lege om PCOS"
    "Dette er en anbefaling ikke medisinsk råd "
)

with st.form("pcos_form"):
    alder = st.number_input(
        "Alder"
    )

    bmi = st.number_input(
        "BMI"
    )

    syklus = st.selectbox(
        "Har du uregelmessig syklus?",
        [" ", "Ja", "Nei" ,"usikker"],
    )

    syklusens_lengde = st.number_input(
        "Hvor lenge varer en normal syklus for deg"
    )

    vektokning = st.selectbox(
        "Har du opplevd vektøkning i det siste",
        [" ","Ja", "Nei", "usikker"]
    )

    hoervekst = st.selectbox(
        "Har du hatt økt hårvekst på steder som ansikt, bryst, mage eller rygg?",
        [" ", "Ja", "Nei" ,"usikker"],
    )

    hudpartier = st.selectbox(
        "Har du fått enkelte hudpartier som har blitt mørkere?",
        [" ", "Ja", "Nei" ,"usikker"],
    )
    hoertap = st.selectbox(
        "Har du opplevd hårtap i det siste??",
        [" ", "Ja", "Nei" ,"usikker"],
    )

    akne = st.selectbox(
        "Har du opplevd mer akne/kviser i det siste?",
        [" ", "Ja", "Nei" ,"usikker"],
    )
    fastfood = st.selectbox(
        "Hvor ofte spiser du fastfood",
        [" ", "Ofte", "Sjeldent", "Aldri"]
    )

    trening = st.selectbox(
        "hvor ofte trener du?",
        [" ", "Hver dag", "flere ganger i uken", "Et par ganger i uken", "Sjeldnere", "Aldri"]
    )



    submitted = st.form_submit_button("Send inn")

if submitted:
    if syklus == " ":
        st.warning("Vennligst fyll inn alle spørsmålene")
    else:
        st.success("Skjemaet sendt inn!")