import json

from src.workout.schemes import Workout

def get_all_data() -> None:
    with open('assets/database.json', encoding='utf-8') as f:
        return json.load(f)

def get_last_id() -> int:
    with open('assets/database.json', encoding='utf-8') as f:
        data = json.load(f)
    return data["last_id"]

def update_last_id() -> None:
    data = get_all_data()
    data['last_id'] += 1
    with open("assets/database.json", "w",  encoding='utf-8') as file:
        json.dump(data, file)

def get_data_workouts(id:int = None) -> list:
    with open('assets/database.json', encoding='utf-8') as f:
        data = json.load(f)
        if isinstance(id,int):
            return [workout for workout in data["workouts"] if workout.get("id",-1) == id]
        return data["workouts"]

def add_data_workouts(workout:Workout={}) -> None:
    data = get_all_data()
    data["workouts"] += [workout]
    with open("assets/database.json", "w",  encoding='utf-8') as file:
        json.dump(data, file)