student_data = {
    "id1": {"name": "Alex", "class": "X", "subject_integration": "history, geography"},
    "id2": {"name": "Jordan", "class": "X", "subject_integration": "history, geography"},
    "id3": {"name": "Alex", "class": "X", "subject_integration": "history, geography"},
    "id4": {"name": "Taylor", "class": "X", "subject_integration": "history, geography"},
    "id5": {"name": "Jordan", "class": "X", "subject_integration": "history, geography"},
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)