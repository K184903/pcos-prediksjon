import streamlit as st
import pandas as pd
from src.predict import prediker

st.set_page_config(
    page_title="PMOS-prediksjon",
)

st.title("PMOS prediksjon")

prevensjon = st.selectbox(
    "Bruker du hormonell prevensjon (p-piller, p-stav, hormonspiral, p-sprøyte el)?",
    [" ", "Nei, ikke på minst 3 måneder", "Ja, eller har sluttet for under 3 måneder siden"]
)
if prevensjon == " ":
    st.stop()

if prevensjon.startswith("Ja"):
    st.info(
        "For å kunne vurdere om du kan ha PMOS må du ha vært uten hormonell prevensjon"
        "i minst 3 måneder. Prevensjon kan skjule eller endre symptomene dine. Snakk med "
        "lege hvis du har symptomer. "
    )
    st.stop()

alder = st.number_input("Alder", min_value=10, max_value=100, value=None, step=1)

if alder is None:
    st.stop()

if alder < 19:
     st.info(
         "Vi kan ikke vurdere om du har PMOS om du er under 19 år, siden syklusen ikke har "
         "stabilisert seg enda. Har du symptomer, anbefaler vi at du snakker med en lege. "
     )
     st.stop();


st.write(
    "Svar på følgende spørsmål og få svar om du burde se en lege om PMOS. "
    "Dette er en anbefaling ikke medisinsk råd "
)

with st.form("pcos_form"):

    bmi = st.number_input(
        "BMI", value=None
    )

    syklus = st.selectbox(
        "Har du uregelmessig syklus?",
        [" ", "Ja", "Nei"],
    )

    blodningsdager = st.number_input(
        "Hvor mange dager varer blødningen din vanligvis?", value=None
    )

    vektokning = st.selectbox(
        "Har du opplevd vektøkning i det siste",
        [" ", "Ja", "Nei"]
    )

    hoervekst = st.selectbox(
        "Har du hatt økt hårvekst på steder som ansikt, bryst, mage eller rygg?",
        [" ", "Ja", "Nei"],
    )

    hudpartier = st.selectbox(
        "Har du fått enkelte hudpartier som har blitt mørkere?",
        [" ", "Ja", "Nei"],
    )
    hoertap = st.selectbox(
        "Har du opplevd hårtap i det siste??",
        [" ", "Ja", "Nei"],
    )

    akne = st.selectbox(
        "Har du opplevd mer akne/kviser i det siste?",
        [" ", "Ja", "Nei"],
    )

    trening = st.selectbox(
        "Trener du regelmessig?",
        [" ", "Ja", "Nei"]
    )
    submitted = st.form_submit_button("Send inn")

if submitted:
    alle_select = [syklus, vektokning, hoervekst, hudpartier, hoertap, akne, trening]
    alle_tall = [bmi, blodningsdager]
    if any(v == " " for v in alle_select) or any(v is None for v in alle_tall):
        st.warning("Vennligst fyll inn alle spørsmålene")
    else:
        svar = {
            "alder" : alder,
            "bmi" : bmi,
            "syklus": syklus,
            "blodningsdager": blodningsdager,
            "vektokning": vektokning,
            "hoervekst": hoervekst,
            "hudpartier": hudpartier,
            "hoertap": hoertap,
            "akne": akne,
            "trening": trening,
        }
        lys = prediker(svar)

        if lys == "rødt":
            st.error("🔴 Du bør vudere å kontakte lege.")
        elif lys == "gult":
            st.warning("🟡 Usikkert. Det kan være lurt å snakke med lege hvis du er bekymret.")
        else:
            st.success("🟢 Lite som tyder på PCOS. Kontakt lege hvis du likevel har symptomer. ")
        st.caption("Dette er en anbefaling, ikke medisinsk råd")