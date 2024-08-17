import flet as ft

from src.utils import BackButton, ClassicalFilledButton,ClassicalTextButton

from src.workout.UI import RoundItem

class ExerciseCreateView(ft.View):
    class ExerciseAlertDialog(ft.AlertDialog):
        def __init__(self,lv:ft.Ref[ft.ListView],round_data:dict={}):
            title = "Добавить поход"
            
            self.lv = lv

            self.text_field_repetitions = ft.Ref[ft.TextField]()
            self.text_field_weight = ft.Ref[ft.TextField]()
            self.text_field_time = ft.Ref[ft.TextField]()


            super().__init__(
                title=ft.Text(title),
                actions=[
                    ClassicalFilledButton(
                        on_click=self.add_exercise,
                        obj=[
                            ft.Icon('ADD'),
                            ft.Text("Добавить упражнение")
                        ]
                    )
                ],
                content=ft.Column(
                    tight=True,
                    controls=[
                        ft.TextField(
                            ref=self.text_field_repetitions,
                            label="Количество повторений",
                            input_filter=ft.NumbersOnlyInputFilter(),
                            on_change=self.on_change_text_field,
                            max_length=4
                        ),
                        ft.TextField(
                            ref=self.text_field_weight,
                            label="Вес",
                            input_filter=ft.NumbersOnlyInputFilter(),
                            on_change=self.on_change_text_field,
                            max_length=4
                        ),
                        ft.TextField(
                            ref=self.text_field_time,
                            label="Время отдыха",
                            input_filter=ft.NumbersOnlyInputFilter(),
                            on_change=self.on_change_text_field,
                            max_length=4
                        ),
                    ]
                ),
            )
                     
        def on_change_text_field(self,e:ft.ControlEvent):
            e.control.error_text = ''
            e.control.update()

        def add_exercise(self,e:ft.ControlEvent):
            def cheak_text_field(text_field:ft.TextField):
                if not text_field.value:
                    text_field.error_text = "Обязательное поле для заполнения"
                    text_field.update()
                    return False 
                return True
            
            if all([cheak_text_field(self.text_field_repetitions.current), cheak_text_field(self.text_field_weight.current), cheak_text_field(self.text_field_time.current)]):
                self.page.close(e.control.parent)
                self.lv.current.controls.insert(-1,ft.ListTile(
                    title=ft.Row(
                        controls=[
                            RoundItem("Повторения:",self.text_field_repetitions.current.value),
                            RoundItem("Вес:",self.text_field_weight.current.value," кг."),
                            RoundItem("Время отдыха:",self.text_field_time.current.value," мин."),
                        ]
                    ),
                    trailing=ft.PopupMenuButton(
                        icon=ft.icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="Изменить"),
                            ft.PopupMenuItem(text="Удалить"),
                        ],
                    )
                ))
                self.lv.current.update()
                self.page.update()

    def __init__(self,page:ft.Page,exercise_data:dict = {}) -> None:
        super().__init__()
        self.page = page
        self.route = f'/workout/create/exercise'
        self.exercise_data = exercise_data
        self.appbar = ft.AppBar(
            leading=BackButton(self.page),
            title=ft.Text('Добавить упражнение'),
        )    
        self.lv = ft.Ref[ft.ListView]()

        self.dlg = self.ExerciseAlertDialog(self.lv)

        self.controls = [
            ft.ListView(
                ref=self.lv,
                expand=1,
                controls=[
                    ft.TextField(label="Название упражнения"),
                    ft.Divider(),
                    ClassicalTextButton([ft.Icon('ADD'),ft.Text("Добавить подход")],on_click=lambda _:self.page.open(self.dlg)),
                ]
            )
        ]        
    def add_round(self,*arg):
        ...