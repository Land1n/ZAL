import flet as ft

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
                        on_click=lambda _:self.page.go(f"/train/{self.id}"),
                    ),
                ]
            ),
            padding=10,
        )

class ExerciseCard(ft.Card):
    def __init__(self,id:int,title:str,annotation:str,round:int,weight:int,repetitions:int,time:int):
        super().__init__()
        self.content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        title=ft.Text(title,size=25),
                        subtitle=ft.Text(f"Подходы: {round}, Повторения: {repetitions},\nДоп. вес: {weight} кг. , Время отдыха: {time} мин.",color='grey'),
                        trailing=ft.PopupMenuButton(
                            icon=ft.icons.MORE_VERT,
                            items=[
                                ft.PopupMenuItem(text="Изменить"),
                                ft.PopupMenuItem(text="Удалить"),
                            ],
                        ),
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
                                rows=[
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text(weight)),
                                            ft.DataCell(ft.Text(repetitions)),
                                            ft.DataCell(ft.Text(time)),
                                        ],
                                    )
                                    for i in range(round)
                                ],
                            ),
                        ],
                    )
                ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=10,
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