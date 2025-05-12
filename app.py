import streamlit as st

st.set_page_config(page_title="Costo Orario Poltrona", page_icon="🦷", layout="centered")

# Titolo principale
st.title("🦷 Costo Orario della Poltrona Odontoiatrica")

st.markdown("""
Calcola il **costo reale per ogni ora** in cui una poltrona dello studio è attiva.
Inserisci i tuoi **costi fissi e operativi mensili**, le ore lavorative e il numero di poltrone: otterrai un dato essenziale per definire i prezzi minimi delle prestazioni, valutare la redditività e capire se lo studio è economicamente sostenibile.
""")

st.divider()

# Sezione: Attività clinica
st.subheader("1️⃣ Attività Clinica")
col1, col2 = st.columns(2)
with col1:
    ore_giornaliere = st.number_input("Ore lavorative per poltrona al giorno", min_value=1, value=1)
with col2:
    giorni_mese = st.number_input("Giorni lavorativi al mese", min_value=1, value=1)

poltrone = st.number_input("Numero di poltrone attive", min_value=1, value=1)

ore_mese = ore_giornaliere * giorni_mese
st.info(f"📆 **Ore totali mese per poltrona:** {ore_mese} ore")

st.divider()

# Sezione: Costi mensili
st.subheader("2️⃣ Costi Mensili Fissi e Operativi")
with st.expander("🔽 Inserisci i tuoi costi mensili (anche stimati)"):
    affitto = st.number_input("Affitto (€)", min_value=0, value=0)
    stipendi = st.number_input("Stipendi + contributi (€)", min_value=0, value=0)
    utenze = st.number_input("Utenze (luce, acqua, internet) (€)", min_value=0, value=0)
    leasing = st.number_input("Leasing / rate attrezzature (€)", min_value=0, value=0)
    software = st.number_input("Software gestionale (€)", min_value=0, value=0)
    commercialista = st.number_input("Commercialista (€)", min_value=0, value=0)
    pulizie = st.number_input("Pulizie (€)", min_value=0, value=0)
    assicurazioni = st.number_input("Assicurazioni studio (€)", min_value=0, value=0)
    manutenzione = st.number_input("Manutenzione impianti/riuniti (€)", min_value=0, value=0)
    sicurezza = st.number_input("Sicurezza / DVR / corsi (€)", min_value=0, value=0)
    marketing = st.number_input("Marketing / pubblicità (€)", min_value=0, value=0)
    altro1 = st.number_input("Altro costo 1 (€)", min_value=0, value=0)
    altro2 = st.number_input("Altro costo 2 (€)", min_value=0, value=0)

# Calcolo costi totali
totale_costi = sum([
    affitto, stipendi, utenze, leasing, software, commercialista,
    pulizie, assicurazioni, manutenzione, sicurezza, marketing,
    altro1, altro2
])

st.divider()

# Sezione: Risultati
st.subheader("📊 Risultati Finali")

st.write(f"📦 **Totale costi mensili dello studio**: €{totale_costi:.2f}")

if ore_mese > 0 and poltrone > 0:
    costo_orario = totale_costi / (ore_mese * poltrone)
    st.success(f"💶 **Costo orario per singola poltrona attiva**: €{costo_orario:.2f}")
else:
    st.warning("⚠️ Inserisci valori validi per ore mensili e numero di poltrone.")
