from flask_cors import CORS
from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from firebase_admin_init import db
import datetime

app = Flask(__name__)
CORS(app)
scheduler = BackgroundScheduler()
scheduler.start()

@app.route('/add_medicine', methods=['POST'])
def add_medicine():
    data = request.get_json()
    user_id = data.get('user_id')
    medicine = data.get('medicine')
    time = data.get('time')
    if not all([user_id, medicine, time]):
        return jsonify({"error": "Missing fields"}), 400
    db.collection("users").document(user_id).collection("medicines").add({
        "medicine": medicine,
        "time": time
    })
    return jsonify({"message": "Medicine added"}), 200

@app.route('/get_schedule/<user_id>', methods=['GET'])
def get_schedule(user_id):
    meds = db.collection("users").document(user_id).collection("medicines").stream()
    result = [{"id": m.id, **m.to_dict()} for m in meds]
    return jsonify(result)

@app.route('/', methods=['GET'])
def home():
    return "Medicine Reminder API is running!"


if __name__ == '__main__':
    app.run(debug=True)