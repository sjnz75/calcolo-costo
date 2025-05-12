import streamlit as st

st.set_page_config(page_title="Costo Orario Poltrona", page_icon="🦷")

st.title("🦷 Calcolo Costo Orario della Poltrona - Studio Odontoiatrico")

# Sezione: Attività clinica
st.header("🕒 Attività Clinica")
ore_giornaliere = st.number_input("Ore produttive al giorno per poltrona", min_value=1, value=1)
giorni_mese = st.number_input("Giorni lavorativi al mese", min_value=1, value=1)
poltrone = st.number_input("Numero di poltrone attive", min_value=1, value=1)

# Calcolo ore totali
ore_mese = ore_giornaliere * giorni_mese
st.info(f"📆 Ore produttive totali al mese per poltrona: **{ore_mese} ore**")

# Sezione: Costi mensili
st.header("📦 Costi Fissi e Operativi Mensili")
affitto = st.number_input("Affitto (€)", min_value=0, value=0)
stipendi = st.number_input("Stipendi + contributi (€)", min_value=0, value=0)
utenze = st.number_input("Utenze (€)", min_value=0, value=0)
leasing = st.number_input("Leasing / attrezzature (€)", min_value=0, value=0)
software = st.number_input("Software gestionale (€)", min_value=0, value=0)
commercialista = st.number_input("Commercialista (€)", min_value=0, value=0)
pulizie = st.number_input("Pulizie (€)", min_value=0, value=0)
assicurazioni = st.number_input("Assicurazioni (€)", min_value=0, value=0)
manutenzione = st.number_input("Manutenzione (€)", min_value=0, value=0)
sicurezza = st.number_input("Sicurezza / DVR / corsi (€)", min_value=0, value=0)
marketing = st.number_input("Marketing / pubblicità (€)", min_value=0, value=0)
altro1 = st.number_input("Altro costo 1 (€)", min_value=0, value=0)
altro2 = st.number_input("Altro costo 2 (€)", min_value=0, value=0)

# Calcolo totale costi
totale_costi = sum([
    affitto, stipendi, utenze, leasing, software, commercialista,
    pulizie, assicurazioni, manutenzione, sicurezza, marketing,
    altro1, altro2
])

# Output costo totale mensile
st.header("📊 Risultati")

st.success(f"📦 Totale costi mensili dello studio: **€{totale_costi:.2f}**")

# Calcolo costo orario
if ore_mese > 0 and poltrone > 0:
    costo_orario = totale_costi / (ore_mese * poltrone)
    st.success(f"💶 Costo orario per poltrona: **€{costo_orario:.2f}**")
else:
    st.warning("⚠️ Inserisci valori validi per ore e numero di poltrone.")
