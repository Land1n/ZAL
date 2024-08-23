import flet as ft

from src.utils import ClassicalFilledButton

from src.workout.schemes import Round

from src.database import get_last_id,update_last_id

class RoundCreateAlertDialog(ft.AlertDialog):

    class RoundCreateAlertDialogTextField(ft.TextField):

        class NumbersAndDotInputFilter(ft.InputFilter):
            def __init__(self):
                super().__init__(regex_string=r"[0-9,.]")

        def __init__(self,ref:ft.Ref,label:str,required:bool=True):
            super().__init__(ref = ref)
            self.label = label
            self.input_filter = self.NumbersAndDotInputFilter()
            self.max_length = 5

            if not required:
                self.prefix_icon=ft.icons.COLOR_LENS
        def on_change_text_field(self,e:ft.ControlEvent):
            e.control.error_text = ''
            e.control.update()

    def __init__(self,round_data:Round = {}):
        title = "Добавить поход"
        
        self.round_data = round_data

        self.text_field_repetitions = ft.Ref[ft.TextField]()
        self.text_field_weight = ft.Ref[ft.TextField]()
        self.text_field_time = ft.Ref[ft.TextField]()

        if self.round_data: 
            self.text_field_repetitions.current.value = self.round_data.repetitions
            self.text_field_weight.current.value = self.round_data.weight
            self.text_field_time.current.value = self.round_data.time

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
                    self.RoundCreateAlertDialogTextField(ref=self.text_field_weight,label="Вес"),
                    self.RoundCreateAlertDialogTextField(ref=self.text_field_repetitions,label="Количество повторений"),
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

        rounds_list = e.control.page.views[-1].rounds_list

        if all([cheak_text_field(self.text_field_repetitions.current), cheak_text_field(self.text_field_weight.current), cheak_text_field(self.text_field_time.current)]):
            rounds_list += [
                {
                    "id": get_last_id(),
                    "weight":self.text_field_weight.current.value,
                    "repetitions":self.text_field_repetitions.current.value,
                    "time":self.text_field_time.current.value
                }
            ]

            update_last_id()
            self.page.close(e.control.parent)
            e.control.page.views[-1].change_round_btn(0)
            e.control.page.views[-1].add_round(round=rounds_list[-1])
            self.page.update()
