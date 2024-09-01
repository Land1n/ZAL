import flet as ft

class DataBase:
    def __init__(self,e:ft.ControlEvent=None,page:ft.Page=None) -> None:
        
        self.__client_storage = None

        if isinstance(e,ft.ControlEvent):
            self.__client_storage = e.control.page.client_storage
        elif isinstance(page,ft.Page):
            self.__client_storage = page.client_storage
        else:
            assert "Not found Client Storage"

        if not self.__client_storage.contains_key("last_id"):
            self.__client_storage.set("last_id",0)
        if not self.__client_storage.contains_key("workouts"):
            self.__client_storage.set("workouts",[])

    def get_last_id(self) -> int:
        last_id = self.__client_storage.get('last_id')
        self.__client_storage.set("last_id",last_id+1)
        return last_id

    def get_data_workouts(self,id:int = None) -> list:
        if isinstance(id,int):
            return [workout for workout in self.__client_storage.get('workouts') if workout.get("id",-1) == id]
        return self.__client_storage.get('workouts')

    def set_data_workouts(self,workout={}) -> None:
        workouts = self.__client_storage.get('workouts')
        workouts += [workout]
        self.__client_storage.set("workouts",workouts)

    def get_obj(self,id:int):
        workouts = self.__client_storage.get("workouts")
        for workout in workouts:
            if workout["id"] == id:
                return workout
            for exercise in workout["exercises"]:
                if exercise["id"] == id:
                    return exercise
                for round in exercise["rounds"]:
                    if round["id"] == id:
                        return round
        else:
            return None

    def clear(self):
        self.__client_storage.clear()