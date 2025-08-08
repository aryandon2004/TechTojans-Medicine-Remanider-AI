from reminder import check_and_send_reminders
from apscheduler.schedulers.background import BackgroundScheduler
from app import app

scheduler = BackgroundScheduler()
scheduler.add_job(func=check_and_send_reminders, trigger="interval", minutes=1)
scheduler.start()

if __name__ == "__main__":
    app.run(debug=True)