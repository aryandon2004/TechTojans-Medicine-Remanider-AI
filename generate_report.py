import pandas as pd
import matplotlib.pyplot as plt
from firebase_admin_init import db

def generate_report(user_id):
    logs_ref = db.collection("users").document(user_id).collection("logs").stream()
    data = [log.to_dict() for log in logs_ref]
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    report = df.groupby(['date', 'confirmation']).size().unstack(fill_value=0)
    report.plot(kind='bar', stacked=True)
    plt.title('Monthly Medicine Compliance')
    plt.xlabel('Date')
    plt.ylabel('Doses')
    plt.savefig(f"report_{user_id}.png")