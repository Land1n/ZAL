import flet as ft

import flet_core as ftc

from src.utils import BackButton,ClassicalTextButton,ClassicalFilledButton

from src.workout.ui.round_read_data_table import RoundReadDataTable,RoundReadDataRow 
from src.workout.ui.round_create_alert_dialog import RoundCreateAlertDialog

from src.utils import ClassicalFrame,view_pop

from src.workout.schemes import Round

from src.database import get_last_id,update_last_id

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
        
        self.round_btn = ft.Ref[ClassicalTextButton]()

        self.title_text_field = ft.Ref[ft.TextField]()
        self.annotation_text_field = ft.Ref[ft.TextField]()
        self.rounds_list = []
        
        self.rounds_table = RoundReadDataTable(rows=[],visible=False)
        self.dlg = RoundCreateAlertDialog()

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
                        ref=self.round_btn,
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

    def change_round_btn(self,type:int,e:ft.ControlEvent=None):
        for control in self.round_btn.current.content.controls:
            if type == 0:
                control.color = ""
            elif type == -1:
                control.color = "red100"
            control.update()
        self.round_btn.current.update()

    def on_change_title_text_field(self,e):
        self.title_text_field.current.error_text = ""
        self.title_text_field.current.update()
        self.change_round_btn(0)

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
            self.change_round_btn(-1)

        if all([self.title_text_field.current.value, self.rounds_list]):
            exercise_list = self.page.views[-2].exercise_list
            exercise_list += [{
                "id":get_last_id(),
                "title": self.title_text_field.current.value,
                "annotation":self.annotation_text_field.current.value,
                "rounds":self.rounds_list
            }]
            update_last_id()
            self.page.views[-2].add_exercise(exercise=exercise_list[-1],need_update=False)
            view_pop(self.page)

