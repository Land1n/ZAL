import flet as ft

from src.workout.schemes import Round 

from src.workout.ui.round_read_data_table import RoundReadDataTable,RoundReadDataRow

class RoundItem(ft.Row):
    def __init__(self, text:str,first_round:int,subtext=''):
        super().__init__(
            controls=[
                ft.Text(text,color="grey",size=13),
                ft.Card(
                    content=ft.Container(
                        content=ft.Text(f"{first_round}{subtext}",color="blue200",size=13),
                        padding=10,
                        bgcolor="grey900",
                        border_radius=10,
                        ),
                ),
            ]
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
                                ft.ResponsiveRow(
                                    # alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    controls=[
                                        RoundItem("Повторения:",first_round.repetitions),
                                        RoundItem("Вес:",first_round.weight," кг."),
                                        RoundItem("Время отдыха:",first_round.time," мин."),
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
                            controls=[RoundReadDataTable(rows=[RoundReadDataRow(**round) for round in rounds])],
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

