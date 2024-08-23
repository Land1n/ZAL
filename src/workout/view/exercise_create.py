import flet as ft

from src.utils import BackButton,ClassicalTextButton,ClassicalFilledButton

from src.workout.ui.round_read_data_table import RoundReadDataTable,RoundReadDataRow 
from src.workout.ui.round_create_alert_dialog import RoundCreateAlertDialog

from src.utils import ClassicalFrame

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
        
        self.controls = [
            ClassicalFrame(
                ref = self.frame,
                obj=[                   
                    ft.Text("Упражнение",size=25,text_align=ft.TextAlign.START), 
                    ft.TextField(
                        ref=self.title_text_field,
                        label="Название упражнения",
                        max_lines=1,
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

    def add_round(self,e:ft.ControlEvent = None,round:Round = {},need_update:bool=True):
        if isinstance(round,dict):
            round = Round(**round)
        self.rounds_table.visible = True
        self.rounds_table.rows.append(RoundReadDataRow(round.id,round.weight,round.repetitions,round.time)) 
        if need_update:
            self.rounds_table.update()

    def add_exercise(self,*arg):
        ...