import json

def get_data_workouts(id:int = None) -> list:
    with open('assets/database.json', encoding='utf-8') as f:
        workouts = json.load(f)
        if isinstance(id,int):
            return [workout for workout in workouts if workout.get("id",-1) == id]
        return workouts