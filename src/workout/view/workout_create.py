import flet as ft

import flet_core as ftc

from src.utils import BackButton,ClassicalFilledButton,ClassicalTextButton,ClassicalFrame

from src.workout.ui.exercise_read_data_table import ExerciseReadDataTable,ExerciseReadDataRow

from src.workout.schemes import Exercises, TypeClassicalBanner,TypeClassicalButton

from src.utils import ClassicalBanner,on_change_text_field,view_pop

from src.database import DataBase

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
        
        self.title_text_field = ft.Ref[ft.TextField]()
        self.annotation_text_field = ft.Ref[ft.TextField]()

        self.exercise_list = []
        self.exercise_data_table = ExerciseReadDataTable(rows=[],visible=False)

        self.exercise_add_btn = ft.Ref[ClassicalTextButton]()

        self.controls = [
            ClassicalFrame(
                title='Тренировка',
                icon=ftc.icons.FITNESS_CENTER,
                obj=[
                    ft.TextField(
                        ref=self.title_text_field,
                        label="Название тренировки",
                        hint_text="Обязательно",
                        on_change=lambda e:on_change_text_field(e,self.exercise_add_btn.current.change_btn_style,TypeClassicalButton.NORMAL)
                    ),
                    ft.TextField(
                        ref=self.annotation_text_field,
                        label="Важные моменты тренировки тренировки",
                        hint_text="Не обязательно",
                        ),
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
        self.exercise_data_table.rows.append(ExerciseReadDataRow(exercise.id,exercise.title,exercise.annotation,exercise.rounds)) 
        if need_update:
            self.exercise_data_table.update()

    def add_workout(self,e:ft.ControlEvent=None):
        if not self.title_text_field.current.value:
            self.title_text_field.current.error_text = "Обязательное поле для заполнения"
            self.title_text_field.current.update()
 
        if not self.exercise_list:
            self.exercise_add_btn.current.change_btn_style(type=TypeClassicalButton.ERROR)
            self.page.open(ClassicalBanner("Нужно добавить хотя бы одно упражнение",type=TypeClassicalBanner.ERROR))

        if all([self.title_text_field.current.value, self.exercise_list]):
            database = DataBase(page=self.page)
            workout = {
                "id":int(database.get_last_id()),
                "title": self.title_text_field.current.value,
                "annotation":self.annotation_text_field.current.value,
                "subtitle":"",
                "avatar_color": "red700",
                "exercises":self.exercise_list
            }
            database.set_data_workouts(workout)
            self.page.open(ClassicalBanner(f"Тренировка ( {self.title_text_field.current.value} ) успешно добавлена",type=TypeClassicalBanner.SUCCESSFUL))
            self.page.views[-2].add_workout(workout=workout,need_update=False)
            view_pop(self.page)
