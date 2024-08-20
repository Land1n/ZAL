import flet as ft

from src.utils import BackButton,ClassicalTextButton,ClassicalFilledButton

from workout.ui.round_create_alert_dialog import RoundCreateAlertDialog

class ExerciseCreateView(ft.View):
    def __init__(self,page:ft.Page,exercise_data:dict = {}):
        super().__init__()
        self.page = page
        self.route = f'/workout/create/exercise'
        self.exercise_data = exercise_data
        self.appbar = ft.AppBar(
            leading=BackButton(self.page),
            title=ft.Text('Добавить упражнение'),
        )    
        self.round_list = []
        self.dlg = RoundCreateAlertDialog(self.round_list)

        self.controls = [
            ft.ListView(
                expand=1,
                spacing=5,
                controls=[
                    ft.TextField(label="Название упражнения"),
                    ft.TextField(
                        label="Заметки",
                        hint_text="Не обязательно",
                        multiline=True,
                        min_lines=1,
                        max_lines=3,
                    ),
                    ClassicalFilledButton([ft.Icon('ADD'),ft.Text("Добавить упражнение")],on_click=self.add_round),
                    ft.Divider(),

                    ClassicalTextButton([ft.Icon('ADD'),ft.Text("Добавить подход")],on_click=lambda _:self.page.open(self.dlg)),
                ]
            )
        ]        
    def add_round(self,*arg):
        print(self.exercise_list)