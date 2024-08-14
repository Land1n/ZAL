import flet as ft
import flet_core

from src.database import get_data_workouts

from src.workout.schemes import Workout
from src.workout.UI import ExerciseCard

from src.utils import BackButton, ClassicalFilledButton,ClassicalTextButton

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
        self.workout_data = {}

        self.appbar = ft.AppBar(
            leading=BackButton(self.page),
            title=ft.Text('Создание тренировки'),
        )   

        self.column_with_rounds = ft.Ref[ft.Column]()

        dlg = ft.AlertDialog(
            title=ft.Text("Добавить упражнение"),
            content=ft.Column(
                tight=True,
                scroll=ft.ScrollMode.ALWAYS,
                ref=self.column_with_rounds,
                controls=[
                    ft.TextField(label="Название упражнения"),
                    ft.Divider(),
                    ClassicalTextButton([ft.Icon('ADD'),ft.Text("Добавить подход")],on_click=self.add_round)
                ],
            ),
            actions=[
                ClassicalFilledButton(obj=[ft.Icon('ADD'),ft.Text("Добавить упражнение")],on_click=self.add_exercise)
            ],
            # on_dismiss=
        ) 

        self.controls = [
            ft.ListView(expand=1,
                controls=[
                    ft.Card(
                        content=ft.Container(
                            padding=10,
                            content=ft.Column(
                                controls=[
                                    ft.Text("Тренировка",size=25),
                                    ft.TextField(label="Название тренировки"),
                                    ft.TextField(label="Важные моменты тренировки тренировки"),
                                    ft.Divider(),
                                    ft.ExpansionTile(
                                        title=ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.Text("Список упражнений:",size=20),
                                                ft.IconButton(icon="ADD",on_click=lambda _:self.page.open(dlg)),
                                            ]
                                        ), 
                                        affinity=ft.TileAffinity.LEADING,
                                        maintain_state=True,
                                        controls=[
                                            ft.DataTable(
                                                columns=[
                                                    ft.DataColumn(ft.Text("Название")),
                                                    ft.DataColumn(ft.Text("Походы"),numeric=True),
                                                ],
                                            ),                                            
                                        ],
                                    ),
                                    ClassicalFilledButton("Создать тренировку")
                                ]
                            )
                        )
                    )
                ]
            ),
        ]
    def add_round(self,*arg):
        self.column_with_rounds.current.controls.insert(-1,
            ft.ListTile(
                title=ft.Row(
                    controls=[
                        ft.TextField(
                            label="Повторения",
                            label_style=ft.TextStyle(size=15),
                            width=100
                        ),
                        ft.TextField(
                            label="Вес",
                            width=100
                        ),
                        ft.TextField(
                            label="Время отдыха",
                            width=100
                        ),
                    ]
                )
            )
        )
        self.column_with_rounds.current.update()
        self.page.update()
    def add_exercise(self,*arg):
        pass