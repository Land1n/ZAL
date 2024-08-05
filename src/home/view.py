import flet as ft

from src.database import get_data_workouts

from src.workout.schemes import Workout
from src.workout.UI import WorkoutCard

class HomeView(ft.View):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page
        self.route = '/home'
        self.appbar = ft.AppBar(
            leading = ft.IconButton(icon=ft.icons.MENU, on_click=lambda _: self.page.open(self.drawer)),
            title = ft.Text("ZAL",size=30,font_family="Dimkin Regular"),
            center_title = True,
            actions = [ft.IconButton(icon=ft.icons.ADD, on_click=lambda _:self.page.go(f"/workout/create"),)]
        )    
        workouts = get_data_workouts()
        self.lv = ft.ListView(expand=1)
        self.controls = [self.lv]
        for workout in workouts:
            workout = Workout(**workout)
            self.lv.controls.append(WorkoutCard(workout.id,workout.title,workout.subtitle,workout.avatar_color))
