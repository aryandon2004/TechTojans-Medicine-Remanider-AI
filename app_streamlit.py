import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Initialize Firebase (only once)
if not firebase_admin._apps:
    cred = credentials.Certificate("TechTrojans/Medicine_Reminder_AI/techtrojans-firebase-adminsdk-fbsvc-074a01db49.json")  # Replace with your actual file
    firebase_admin.initialize_app(cred)
db = firestore.client()

st.set_page_config(page_title="💊 Medicine Reminder Assistant")
st.title("💊 Medicine Reminder AI Assistant")

st.markdown("Fill in your medicine schedule below:")

user_id = st.text_input("Enter your Telegram User ID", placeholder="e.g. 123456789")
medicine = st.text_input("Enter Medicine Name", placeholder="e.g. Crocin")

reminder_time = st.time_input("Reminder Time")

# Convert time to HH:MM string format
time_str = reminder_time.strftime("%H:%M")

if st.button("Add Reminder"):
    if not user_id or not medicine:
        st.error("❌ Please fill all fields.")
    else:
        try:
            # Save into Firestore: users/{user_id}/medicines/{auto_id}
            db.collection("users").document(user_id).collection("medicines").add({
                "medicine": medicine,
                "time": time_str
            })
            st.success(f"✅ Reminder for '{medicine}' at {time_str} added!")
        except Exception as e:
            st.error(f"Error: {e}")
