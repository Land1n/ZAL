import flet as ft

from src.utils import ClassicalFilledButton

class RoundCreateAlertDialog(ft.AlertDialog):
    class RoundCreateAlertDialogTextField(ft.TextField):
        def __init__(self,ref:ft.Ref,label:str,required:bool=True):
            super().__init__(ref = ref)
            self.label = label
            self.input_filter = ft.NumbersOnlyInputFilter()
            self.max_length = 4

            if not required:
                self.prefix_icon=ft.icons.COLOR_LENS
        def on_change_text_field(self,e:ft.ControlEvent):
            e.control.error_text = ''
            e.control.update()
    def __init__(self,exercise_list=[]):
        title = "Добавить поход"
        

        self.text_field_repetitions = ft.Ref[ft.TextField]()
        self.text_field_weight = ft.Ref[ft.TextField]()
        self.text_field_time = ft.Ref[ft.TextField]()


        super().__init__(
            title=ft.Text(title),
            actions=[
                ClassicalFilledButton(
                    on_click=self.add_round,
                    obj=[
                        ft.Icon('ADD'),
                        ft.Text("Добавить упражнение")
                    ]
                )
            ],
            content=ft.Column(
                tight=True,
                controls=[
                    self.RoundCreateAlertDialogTextField(ref=self.text_field_repetitions,label="Количество повторений"),
                    self.RoundCreateAlertDialogTextField(ref=self.text_field_weight,label="Вес"),
                    self.RoundCreateAlertDialogTextField(ref=self.text_field_time,label="Время отдыха",)
                ]
            ),
        )
                    
    def add_round(self,e:ft.ControlEvent):
        def cheak_text_field(text_field:ft.TextField):
            if not text_field.value:
                text_field.error_text = "Обязательное поле для заполнения"
                text_field.update()
                return False 
            return True
        if all([cheak_text_field(self.text_field_repetitions.current), cheak_text_field(self.text_field_weight.current), cheak_text_field(self.text_field_time.current)]):
            self.page.close(e.control.parent)
            self.page.update()