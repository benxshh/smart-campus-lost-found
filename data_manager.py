import json

def save_data(items):
    with open("data.json", "w") as file:
        json.dump(items, file, indent=4)

def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return[]

    except json.JSONDecodeError:
        return[]