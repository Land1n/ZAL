import flet as ft

import flet_core as ftc

from src.utils import BackButton,ClassicalFilledButton,ClassicalFrame

class WorkoutCreateView(ft.View):
    def __init__(self,page:ft.Page,workout_data:dict = {}):
        super().__init__()
        self.page = page
        self.workout_data = workout_data
        self.route = f'/workout/create'
        self.appbar = ft.AppBar(
            leading=BackButton(self.page),
            title=ft.Text('Создание тренировки'),
        )   

        self.controls = [
            ClassicalFrame(
                title='Тренировка',
                icon=ftc.icons.FITNESS_CENTER,
                obj=[
                    ft.TextField(label="Название тренировки"),
                    ft.TextField(label="Важные моменты тренировки тренировки"),
                    ft.Divider(),
                    ft.ExpansionTile(
                        title=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text("Список упражнений:",size=20),
                                ft.IconButton(icon="ADD",on_click=lambda _:self.page.go("/workout/create/exercise")),
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
        ]