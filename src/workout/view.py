import flet as ft
import flet_core

from src.database import get_data_workouts

from src.workout.schemes import Workout
from src.workout.UI import ExerciseCard

from src.utils import BackButton

class WorkoutReadView(ft.View):
    def __init__(self,page:ft.Page,id:int):
        super().__init__()
        self.page = page
        self.id = id
        self.appbar = ft.AppBar(
            leading=BackButton(self.page),
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
        self.appbar = ft.AppBar(
            leading=BackButton(self.page),
            title=ft.Text('Создание тренировки'),
        )   
        # self.workout = Workout()
        # self.workout.avatar_color = flet_core.colors.random_color()
        self.lv = ft.ListView(expand=1,height=200)
        self.controls = [
            ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Column(
                        controls=[
                            ft.TextField(label="Название тренировки"),
                            ft.TextField(label="Важные моменты тренировки тренировки"),
                            ft.Divider(),
                            ft.Text("Список упражнений:",size=20),      
                            self.lv,                     
                            ft.CupertinoFilledButton(
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[ft.Text("Создать тренировку")]
                                ),
                                opacity_on_click=0.3,
                                on_click=lambda e: print("CupertinoFilledButton clicked!"),
                            ),
                        ]
                    )
                )
            )
        ]