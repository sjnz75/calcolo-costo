import streamlit as st

st.set_page_config(page_title="Costo Mensile Poltrona", page_icon="🦷")

st.title("🦷 Calcolo Costo Mensile della Poltrona - Studio Odontoiatrico")

st.header("📦 Costi Fissi e Operativi Mensili")
affitto = st.number_input("Affitto (€)", min_value=0, value=0)
stipendi = st.number_input("Stipendi + contributi (€)", min_value=0, value=0)
utenze = st.number_input("Utenze (€)", min_value=0, value=0)
leasing = st.number_input("Leasing / rate attrezzature (€)", min_value=0, value=0)
software = st.number_input("Software gestionale (€)", min_value=0, value=0)
commercialista = st.number_input("Commercialista (€)", min_value=0, value=0)
pulizie = st.number_input("Pulizie (€)", min_value=0, value=0)
assicurazioni = st.number_input("Assicurazioni (€)", min_value=0, value=0)
manutenzione = st.number_input("Manutenzione ordinaria (€)", min_value=0, value=0)
sicurezza = st.number_input("Sicurezza / DVR / corsi (€)", min_value=0, value=0)
marketing = st.number_input("Marketing / pubblicità (€)", min_value=0, value=0)

# Costi personalizzati
st.header("🧾 Altri Costi Personalizzati")
altro1 = st.number_input("Altro costo 1 (€)", min_value=0, value=0)
altro2 = st.number_input("Altro costo 2 (€)", min_value=0, value=0)

# Numero di poltrone
st.header("🦷 Numero di Poltrone Attive")
poltrone = st.number_input("Numero di poltrone attive", min_value=1, value=1)

# Calcolo costo mensile per poltrona
totale_costi = sum([
    affitto, stipendi, utenze, leasing, software, commercialista,
    pulizie, assicurazioni, manutenzione, sicurezza, marketing,
    altro1, altro2
])

costo_mensile_per_poltrona = totale_costi / poltrone

st.success(f"💶 Costo mensile per poltrona: **€{costo_mensile_per_poltrona:.2f}**")
