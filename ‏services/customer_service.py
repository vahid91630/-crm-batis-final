import json
import os

DATA_FILE = "data/customers.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def handle_customer_message(message, user_id):
    data = load_data()
    if any(c["user_id"] == user_id for c in data):
        return "✅ شما قبلاً ثبت شدید"
    data.append({"user_id": user_id, "message": message})
    save_data(data)
    return "✅ اطلاعات شما با موفقیت ثبت شد"
