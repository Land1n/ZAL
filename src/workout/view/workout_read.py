import flet as ft

from repath import match

from src.database import DataBase
from src.utils import BackButton
from src.workout.UI import ExerciseCard

from src.workout.schemes import Workout

class WorkoutReadView(ft.View):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page
        self.id = int(match("/workout/:id",self.page.route).groupdict()["id"])
        self.route = f'/workout/{self.id}'
        self.appbar = ft.AppBar(
            leading=BackButton(self.page),
            title=ft.Text('Тренировка'),
        )
        database = DataBase(page=self.page)
        self.workout = Workout(**(database.get_data_workouts(self.id)[0]))
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