import flet as ft

from src.database import DataBase

from src.workout.schemes import Workout

from src.workout.ui.workout_read_card import WorkoutReadCard

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
        database = DataBase(page=self.page)

        workouts = database.get_data_workouts()
        
        self.lv = ft.ListView(
            expand=1,
            # controls=[
            #     ft.Column(
            #         alignment=ft.MainAxisAlignment.CENTER,
            #         horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            #         controls=[
            #             ft.Text("")
            #         ]
            #     )
            # ]
        )
        self.controls = [self.lv]
        for workout in workouts:
            self.add_workout(workout,need_update=False)

    def add_workout(self,workout:Workout = {},need_update=True):
        if isinstance(workout,dict):
            workout = Workout(**workout) 
        self.lv.controls.append(WorkoutReadCard(workout.id,workout.title,workout.subtitle,workout.avatar_color))
        if need_update:
            self.lv.update()