from firebase_admin_init import db
from datetime import datetime

def log_response(user_id, medicine, confirmation):
    today = datetime.now().strftime("%Y-%m-%d")
    db.collection("users").document(user_id).collection("logs").add({
        "medicine": medicine,
        "confirmation": confirmation,
        "date": today
    })