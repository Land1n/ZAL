import flet as ft

import flet_core as ftc

from src.utils import BackButton,ClassicalTextButton,ClassicalFilledButton

from src.workout.ui.round_read_data_table import RoundReadDataTable,RoundReadDataRow 
from src.workout.ui.round_create_alert_dialog import RoundCreateAlertDialog

from src.utils import ClassicalFrame,view_pop

from src.workout.schemes import Round



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
        
        self.frame = ft.Ref[ClassicalFrame]()
        
        self.title_text_field = ft.Ref[ft.TextField]()
        self.annotation_text_field = ft.Ref[ft.TextField]()
        self.rounds_list = []
        
        self.rounds_table = RoundReadDataTable(rows=[],visible=False)
        self.dlg = RoundCreateAlertDialog()
        
        self.banner = ft.Banner(
            bgcolor="red100",
            leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color='red', size=40),            content=ft.Text(
                value="Чтобы добавить упражение нужно добавить хотя бы один поход.",
                color="red",
            ),
            actions=[
                ft.TextButton(text="Закрыть",style=ft.ButtonStyle(color="red"),on_click=self.close_banner),
            ],
        )


        self.controls = [
            ClassicalFrame(
                ref = self.frame,
                icon = ftc.icons.FITNESS_CENTER,
                title="Упражнение",
                obj=[                   
                    ft.TextField(
                        ref=self.title_text_field,
                        label="Название упражнения",
                        max_lines=1,
                        on_change=self.on_change_title_text_field,
                    ),
                    ft.TextField(
                        ref=self.annotation_text_field,
                        label="Заметки",
                        hint_text="Не обязательно",
                        multiline=True,
                        min_lines=1,
                        max_lines=3,
                    ),
                    ClassicalFilledButton(
                        on_click=self.add_exercise,
                        obj=[
                            ft.Icon("ADD"),
                            ft.Text("Добавить упражнение")
                        ],
                    ),
                    ft.Divider(),
                    self.rounds_table,
                    ClassicalTextButton(
                        on_click=lambda _:self.page.open(self.dlg),
                        obj=[
                            ft.Icon('ADD'),
                            ft.Text("Добавить подход")
                        ]
                    )
                ]
            )
        ]     
        
        if self.rounds_list:
            for round in self.rounds_list:
                self.add_round(round=round,need_update=False)

    def on_change_title_text_field(self,e):
        self.title_text_field.current.error_text = ""
        self.title_text_field.current.update()

    def close_banner(self,e:ft.ControlEvent = None):
        self.page.close(self.banner)

    def add_round(self,e:ft.ControlEvent = None,round:Round = {},need_update:bool=True):
        if isinstance(round,dict):
            round = Round(**round)
        self.rounds_table.visible = True
        self.rounds_table.rows.append(RoundReadDataRow(round.id,round.weight,round.repetitions,round.time)) 
        if need_update:
            self.rounds_table.update()

    def add_exercise(self,*arg):
        if not self.title_text_field.current.value:
            self.title_text_field.current.error_text = "Обязательное поле для заполнения"
            self.title_text_field.current.update()
 
        if not self.rounds_list:
            self.page.open(self.banner)

        if all([self.title_text_field.current.value, self.rounds_list]):
            self.close_banner()
            view_pop(self.page)
            