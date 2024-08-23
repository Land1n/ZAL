import flet as ft

import flet_core as ftc

from src.utils import BackButton,ClassicalFilledButton,ClassicalTextButton,ClassicalFrame

from src.workout.ui.exercise_read_data_table import ExerciseReadDataTable,ExerciseReadDataRow

from src.workout.schemes import Exercises

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


        self.exercise_list = []
        self.exercise_data_table = ExerciseReadDataTable(rows=[],visible=False)

        self.exercise_add_btn = ft.Ref[ClassicalTextButton]()

        self.controls = [
            ClassicalFrame(
                title='Тренировка',
                icon=ftc.icons.FITNESS_CENTER,
                obj=[
                    ft.TextField(label="Название тренировки"),
                    ft.TextField(label="Важные моменты тренировки тренировки"),
                    ClassicalFilledButton(obj="Создать тренировку",on_click=self.add_workout),
                    ft.Divider(),
                    self.exercise_data_table,
                    ClassicalTextButton(
                        ref=self.exercise_add_btn,
                        visible=False,
                        on_click=lambda _:self.page.go("/workout/create/exercise"),
                        obj=[
                            ft.Icon('ADD'),
                            ft.Text("Добавить упражнение")
                        ]   
                    )                                        
                ]
            )
        ]
        if not self.exercise_list:
            self.exercise_add_btn.current.visible = True
        elif self.exercise_list:
            for exercise in self.exercise_list:
                self.add_exercise(exercise=exercise,need_update=False)

    def add_exercise(self,e:ft.ControlEvent=None,exercise:Exercises={},need_update=True):
        if isinstance(exercise,dict):
            exercise = Exercises(**exercise)
        self.exercise_data_table.visible = True
        self.exercise_add_btn.current.visible = False
        self.exercise_data_table.rows.append(ExerciseReadDataRow(exercise.id,exercise.title,exercise.annotation,exercise.rounds)) 
        if need_update:
            self.exercise_data_table.update()

    def add_workout(self,e:ft.ControlEvent=None):
        ...