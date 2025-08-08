from datetime import datetime
from time import time
from firebase_admin_init import db
import pytz
from telegram_bot import send_telegram_reminder

IST = pytz.timezone('Asia/Kolkata')

def check_and_send_reminders():
    now = datetime.now(IST).strftime("%H:%M")
    users_ref = db.collection("users").stream()
    for user in users_ref:
        user_id = user.id
        meds = db.collection("users").document(user_id).collection("medicines").stream()
        for m in meds:
            med_data = m.to_dict()
            if med_data["time"] == now:
                send_telegram_reminder(user_id, med_data["medicine"])

                import time

if __name__ == "__main__":
    print("⏰ Reminder service started...")
    while True:
        check_and_send_reminders()
        time.sleep(60)  # Check every 1 minute
