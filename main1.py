import json

# TODO решите задачу
def task() -> float:
    file = "input.json"
    with open(file) as f:
        json_data = json.load(f)
        result = sum([item["score"] * item["weight"] for item in json_data])

    return round(result, 3)

print(task())
