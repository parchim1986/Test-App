
import streamlit as st
import gspread
from google.oauth2 import service_account
from datetime import datetime

st.set_page_config(page_title="Google Sheets Test", page_icon="📄")
st.title("🔁 Test: Kann die App auf deine Google Tabelle schreiben?")

name = st.text_input("Dein Name")
email = st.text_input("Deine E-Mail")
phone = st.text_input("Deine Telefonnummer")

if st.button("Test absenden") and name and email and phone:
    try:
        creds_dict = st.secrets["gcp"]
        credentials = service_account.Credentials.from_service_account_info(creds_dict)
        client = gspread.Client(auth=credentials)
        client.session = gspread.httpsession.HTTPSession(credentials)
        sheet = client.open("Fitness Leads").sheet1
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")
        sheet.append_row([name, email, phone, timestamp])
        st.success("✅ Es hat geklappt! Daten wurden gespeichert.")
    except Exception as e:
        st.error(f"❌ Fehler beim Speichern: {e}")
