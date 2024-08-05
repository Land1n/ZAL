import flet as ft

from src.workout.schemes import Round 

class WorkoutCard(ft.Card):
    def __init__(self,id:int,title:str,subtitle:str,avatar_color:str):
        super().__init__()
        self.id = id
        self.content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.CircleAvatar(content=ft.Text(title[0]),bgcolor=avatar_color),
                        title=ft.Text(title),
                        subtitle=ft.Text(subtitle),
                        trailing=ft.PopupMenuButton(
                            icon=ft.icons.MORE_VERT,
                            items=[
                                ft.PopupMenuItem(text="Изменить"),
                                ft.PopupMenuItem(text="Удалить"),
                            ],
                        ),
                        on_click=lambda _:self.page.go(f"/workout/{self.id}"),
                    ),
                ]
            ),
            padding=10,
        )

class ExerciseCard(ft.Card):
    def __init__(self,id:int,title:str,annotation:str,rounds:Round):
        super().__init__()
        first_round = Round(**rounds[0])
        self.content=ft.Container(
            padding=10,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.ListTile(
                        title=ft.Text(title,size=25),
                        trailing=ft.PopupMenuButton(
                            icon=ft.icons.MORE_VERT,
                            items=[
                                ft.PopupMenuItem(text="Изменить"),
                                ft.PopupMenuItem(text="Удалить"),
                            ],
                        ),
                    ),
                    # ft.Divider(),
                    ft.Container(
                        padding=ft.Padding(20,0,0,0),    
                        content=ft.Column(
                            controls=[
                                ft.Text("Первый поход",size=15),
                                ft.Row(
                                    controls=[
                                        ft.Text("Повторения:",color="grey"),
                                        ft.Card(
                                            content=ft.Container(
                                                content=ft.Text(first_round.repetitions,color="blue200"),
                                                padding=10,
                                                bgcolor="grey900",
                                                border_radius=10)
                                            ),
                                        ft.Text("Доп. вес:",color="grey"),
                                        ft.Card(
                                            content=ft.Container(
                                                content=ft.Text(f"{first_round.weight} кг.",color="blue200"),
                                                padding=10,
                                                bgcolor="grey900",
                                                border_radius=10)
                                            ),
                                        ft.Text("Время отдыха:",color="grey"),
                                        ft.Card(
                                            content=ft.Container(
                                                content=ft.Text(f"{first_round.time} мин.",color="blue200"),
                                                padding=10,
                                                bgcolor="grey900",
                                                border_radius=10)
                                            ),                                            
                                        ]
                                ),
                            ]
                        )
                    ),
                    ft.Divider(),
                    ft.ExpansionTile(
                            title=ft.Text("Полная тренировка"),
                            subtitle=ft.Text("Информация представлена в таблице",color="grey"),
                            leading=ft.Icon(ft.icons.WORK),
                            affinity=ft.TileAffinity.PLATFORM,
                            maintain_state=True,
                            controls=[ft.DataTable(
                                columns=[
                                    ft.DataColumn(ft.Text("Вес"), numeric=True),
                                    ft.DataColumn(ft.Text("Повторения"), numeric=True),
                                    ft.DataColumn(ft.Text("Время отдыха"), numeric=True),
                                ],
                                rows=[RoundDataRow(**round) for round in rounds],
                            ),
                        ],
                    )
                ],
            ),
        )
        if annotation != "":
            self.content.content.controls += [ft.ExpansionTile(
                            title=ft.Text("Важные моменты"),
                            subtitle=ft.Text("Техника выполнения",color="grey"),
                            leading=ft.Icon(ft.icons.INFO),
                            affinity=ft.TileAffinity.PLATFORM,
                            maintain_state=True,
                            controls=[ft.ListTile(title=ft.Text(annotation))],
                        )]

class RoundDataRow(ft.DataRow):
    def __init__(self,id:int,weight:int,repetitions:int,time:int):
        
        self.cells = [
            ft.DataCell(ft.Text(weight)),
            ft.DataCell(ft.Text(repetitions)),
            ft.DataCell(ft.Text(time)),
        ]
        super().__init__(cells=self.cells)
