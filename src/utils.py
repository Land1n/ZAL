import flet as ft

from functools import partial

def view_pop(page:ft.Page,*view):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)


class BackButton(ft.IconButton):
    def __init__(self,page:ft.Page):
        super().__init__(
            icon=ft.icons.ARROW_BACK,
            on_click=partial(view_pop,page),
        )


class ClassicalFilledButton(ft.CupertinoFilledButton):
    def __init__(self,obj=None,on_click=None) -> None:
        self.obj = []
        if isinstance(obj,str):
            self.obj += [ft.Text(obj)]
        elif isinstance(obj,list):
            self.obj = obj
        super().__init__(
            on_click=on_click,
            opacity_on_click=0.3,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=self.obj 
            )
        )


class ClassicalTextButton(ft.TextButton):
    def __init__(self,obj=None,on_click=None) -> None:
        self.obj = []
        if isinstance(obj,str):
            self.obj += [ft.Text(obj)]
        elif isinstance(obj,list):
            self.obj = obj
        super().__init__(
            on_click=on_click,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=self.obj 
            )
        )