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
        self.rounds_table = RoundReadDataTable(rows=[])
        
        self.rounds_list = []
        
        self.dlg = RoundCreateAlertDialog()
        
        self.frame = ft.Ref[ClassicalFrame]()
        
        self.controls = [
            ClassicalFrame(
                ref = self.frame,
                obj=[                    
                    ft.TextField(
                        label="Название упражнения"
                    ),
                    ft.TextField(
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
                    ClassicalTextButton(
                        on_click=lambda _:self.page.open(self.dlg),
                        obj=[
                            ft.Icon('ADD'),
                            ft.Text("Добавить подход")
                        ]
                    ),
                ]
            ),
        ]     
        
    def add_round(self,e:ft.ControlEvent = None,round:Round = {}):
        if isinstance(round,dict):
            round = Round(**round)
        self.frame.current.obj.insert(-1,  self.rounds_table)
        self.frame.current.update()
        self.rounds_table.rows.append(RoundReadDataRow(round.id,round.weight,round.repetitions,round.time)) 
        self.rounds_table.update()
    def add_exercise(self,*arg):
        print(self.controls)
        print(self.rounds_list)