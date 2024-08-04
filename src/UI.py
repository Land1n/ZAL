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