import json

def get_data_workouts(id:int = None) -> list:
    with open('assets/database.json', encoding='utf-8') as f:
        data = json.load(f)
        if isinstance(id,int):
            return [workout for workout in data["workouts"] if workout.get("id",-1) == id]
        return data["workouts"]


def get_id_for_obj() -> int:
    with open('assets/database.json', encoding='utf-8') as f:
        data = json.load(f)
        return data["last_id"]
