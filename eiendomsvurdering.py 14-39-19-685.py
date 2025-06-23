eiendomsvurdering.pyimport streamlit as st

st.set_page_config(page_title="Eiendomsvurdering", layout="centered")

st.title("🔍 Eiendomsvurdering – Prototype")

st.markdown("Fyll inn nøkkeltall for prosjektet ditt, og se automatisk vurdering.")

# Input
col1, col2 = st.columns(2)

with col1:
    eiendom = st.text_input("Prosjektnavn / adresse", "Eksempel – Horten")
    kjopspris = st.number_input("Kjøpspris (kr)", value=5_150_000, step=100_000)
    enheter = st.number_input("Antall boenheter", value=5)
    manedlig_leie = st.number_input("Total månedlig leie (kr)", value=78_800, step=1000)
    oppussing = st.number_input("Oppussingskostnader (kr)", value=2_000_000, step=100_000)
    ny_verdi = st.number_input("Estimert ny verdi etter tiltak (kr)", value=13_500_000, step=100_000)

with col2:
    kommuneavgift = st.number_input("Årlige kommunale avgifter (kr)", value=36_456, step=1000)
    drift = st.number_input("Andre driftskostnader/år (kr)", value=15_000, step=1000)
    rente = st.number_input("Rente (%)", value=5.5, step=0.1)
    lanebelop = st.number_input("Lånebeløp (kr)", value=6_500_000, step=100_000)
    eierform = st.selectbox("Eierform", ["AS", "Privat"])

# Beregninger
arlig_leie = manedlig_leie * 12
kostnader = kommuneavgift + drift
netto_inntekt = arlig_leie - kostnader
renteutgift = lanebelop * (rente / 100)
kontantstrom = netto_inntekt - renteutgift
yield_brutto = (arlig_leie / kjopspris) * 100
yield_netto = (netto_inntekt / kjopspris) * 100
belaaning_75 = ny_verdi * 0.75
totalkostnad = kjopspris + oppussing
egenkapitalbehov = totalkostnad - belaaning_75

# Vurdering
if yield_brutto >= 10:
    vurdering = "🟢 KJØR!"
elif yield_brutto >= 6:
    vurdering = "🟡 VURDER"
else:
    vurdering = "🔴 DROP"

# Output
st.markdown("---")
st.subheader(f"Resultater for: {eiendom}")
st.write(f"**Brutto yield:** {yield_brutto:.2f} %")
st.write(f"**Netto yield:** {yield_netto:.2f} %")
st.write(f"**Kontantstrøm etter renter:** {kontantstrom:,.0f} kr/år")
st.write(f"**Egenkapitalbehov:** {egenkapitalbehov:,.0f} kr")
st.write(f"**Vurdering:** {vurdering}")

st.markdown("---")
st.caption("Versjon 1 – laget med Streamlit")
import streamlit as st

st.set_page_config(page_title="Eiendomsvurdering", layout="centered")

st.title("🔍 Eiendomsvurdering – Prototype")

st.markdown("Fyll inn nøkkeltall for prosjektet ditt, og se automatisk vurdering.")

# Input
col1, col2 = st.columns(2)

with col1:
    eiendom = st.text_input("Prosjektnavn / adresse", "Eksempel – Horten")
    kjopspris = st.number_input("Kjøpspris (kr)", value=5_150_000, step=100_000)
    enheter = st.number_input("Antall boenheter", value=5)
    manedlig_leie = st.number_input("Total månedlig leie (kr)", value=78_800, step=1000)
    oppussing = st.number_input("Oppussingskostnader (kr)", value=2_000_000, step=100_000)
    ny_verdi = st.number_input("Estimert ny verdi etter tiltak (kr)", value=13_500_000, step=100_000)

with col2:
    kommuneavgift = st.number_input("Årlige kommunale avgifter (kr)", value=36_456, step=1000)
    drift = st.number_input("Andre driftskostnader/år (kr)", value=15_000, step=1000)
    rente = st.number_input("Rente (%)", value=5.5, step=0.1)
    lanebelop = st.number_input("Lånebeløp (kr)", value=6_500_000, step=100_000)
    eierform = st.selectbox("Eierform", ["AS", "Privat"])

# Beregninger
arlig_leie = manedlig_leie * 12
kostnader = kommuneavgift + drift
netto_inntekt = arlig_leie - kostnader
renteutgift = lanebelop * (rente / 100)
kontantstrom = netto_inntekt - renteutgift
yield_brutto = (arlig_leie / kjopspris) * 100
yield_netto = (netto_inntekt / kjopspris) * 100
belaaning_75 = ny_verdi * 0.75
totalkostnad = kjopspris + oppussing
egenkapitalbehov = totalkostnad - belaaning_75

# Vurdering
if yield_brutto >= 10:
    vurdering = "🟢 KJØR!"
elif yield_brutto >= 6:
    vurdering = "🟡 VURDER"
else:
    vurdering = "🔴 DROP"

# Output
st.markdown("---")
st.subheader(f"Resultater for: {eiendom}")
st.write(f"**Brutto yield:** {yield_brutto:.2f} %")
st.write(f"**Netto yield:** {yield_netto:.2f} %")
st.write(f"**Kontantstrøm etter renter:** {kontantstrom:,.0f} kr/år")
st.write(f"**Egenkapitalbehov:** {egenkapitalbehov:,.0f} kr")
st.write(f"**Vurdering:** {vurdering}")

st.markdown("---")
st.caption("Versjon 1 – laget med Streamlit")

