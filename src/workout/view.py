import flet as ft

from src.view import view_pop
from src.database import get_data_workouts

from src.workout.schemes import Workout
from src.workout.UI import ExerciseCard

from functools import partial

class WorkoutReadView(ft.View):
    def __init__(self,page:ft.Page,id:int):
        super().__init__()
        self.page = page
        self.id = id
        self.appbar = ft.AppBar(
            leading=ft.IconButton(ft.icons.ARROW_BACK,on_click=partial(view_pop,self.page)),
            title=ft.Text('Тренировка'),
        )
        self.workout = Workout(**(get_data_workouts(self.id)[0]))
        self.controls = [
            ft.Text(self.workout.title,size=40),
            ft.Text(self.workout.subtitle,color="grey"),
            ft.Divider(),
            ft.Text("Список упражнений",size=30),

        ]
        self.lv = ft.ListView(expand=1)
        self.controls.append(self.lv)
        self.lv.controls += [ExerciseCard(**exercise) for exercise in self.workout.exercises]

        if self.workout.annotation:
            self.controls.insert(2,ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.INFO),
                                title=ft.Text("Важные моменты"),
                                subtitle=ft.Text(self.workout.annotation),
                            ),
                        ]
                    ),
                    padding=10,
                )
            ))

class WorkoutCreateView(ft.View):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page