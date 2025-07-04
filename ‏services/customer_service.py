def add_customer(data, db_path):
    import json, os
    customers = []
    if os.path.exists(db_path):
        with open(db_path, "r", encoding="utf-8") as f:
            customers = json.load(f)
    customers.append(data)
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(customers, f, ensure_ascii=False, indent=2)
