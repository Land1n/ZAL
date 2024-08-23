import flet as ft

import flet_core

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
    def __init__(self,visible=True,obj=None,on_click=None,ref:ft.Ref=None) -> None:
        self.obj = []
        if isinstance(obj,str):
            self.obj += [ft.Text(obj)]
        elif isinstance(obj,list):
            self.obj = obj
        super().__init__(
            ref=ref,
            visible=visible,
            on_click=on_click,
            opacity_on_click=0.3,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=self.obj 
            )
        )


class ClassicalTextButton(ft.TextButton):
    def __init__(self,visible=True,obj=None,on_click=None,ref:ft.Ref=None) -> None:
        self.obj = []
        if isinstance(obj,str):
            self.obj += [ft.Text(obj)]
        elif isinstance(obj,list):
            self.obj = obj
        super().__init__(
            ref=ref,
            visible=visible,
            on_click=on_click,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=self.obj 
            )
        )

class ClassicalFrame(ft.ListView):
    def __init__(self,obj:list,title:str="",icon:str=flet_core.icons.CIRCLE_OUTLINED,ref:ft.Ref=None):
        super().__init__(ref=ref)
        self.obj = obj
        self.title = title
        self.icon = icon

        visible=False
        if self.title:
            visible=True

        self.controls = [
            ft.ListView(
                expand=1,
                spacing=5,
                controls=[
                    ft.Card(
                        content=ft.Container(
                            padding=10,                            
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Row(
                                        visible=visible,
                                        controls=[ft.Icon(self.icon),ft.Text(self.title,size=25)]
                                    ),
                                    *self.obj
                                ]
                            )
                        )
                    )
                ]
            )
        ]

    