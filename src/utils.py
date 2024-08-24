import flet as ft
import flet_core

from functools import partial

from src.workout.schemes import TypeClassicalBanner,TypeClassicalButton

from time import sleep

from typing import Callable

def view_pop(page:ft.Page,*view):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)


def on_change_text_field(e:ft.ControlEvent=None,func:Callable=None,*func_arg):
    e.control.error_text = ""
    e.control.update()
    if isinstance(func,Callable):
        func(*func_arg)

class BackButton(ft.IconButton):
    def __init__(self,page:ft.Page):
        super().__init__(
            icon=ft.icons.ARROW_BACK,
            on_click=partial(view_pop,page),
        )


class ClassicalButton:
    obj = []
    def change_btn_style(self,type:TypeClassicalButton=TypeClassicalButton.NORMAL,e:ft.ControlEvent=None):
        for control in self.obj:
            if type == TypeClassicalButton.NORMAL:
                control.color = ""
            elif type == TypeClassicalButton.ERROR:
                control.color = "red200"
            control.update()

class ClassicalFilledButton(ft.CupertinoFilledButton,ClassicalButton):
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


class ClassicalTextButton(ft.TextButton,ClassicalButton):
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

    
class ClassicalBanner(ft.Banner):
    def __init__(self,text:str,type:TypeClassicalBanner = TypeClassicalBanner.INFO,ref:ft.Ref=None):
        bgcolor = None
        color = None
        leading = None

        if type == TypeClassicalBanner.INFO:
            bgcolor = "blue100"
            color = "blue"
            leading = "INFO"
        
        elif type == TypeClassicalBanner.SUCCESSFUL:
            bgcolor = "green100"
            color = "green"
            leading = "DONE_ALL"

        elif type == TypeClassicalBanner.WARNING:
            bgcolor = "amber100"
            color = "amber"
            leading = "WARNING"
        
        elif type == TypeClassicalBanner.ERROR:
            bgcolor = "red100"
            color = "red"
            leading = "ERROR"

        super().__init__(
            bgcolor=bgcolor,
            leading=ft.Icon(name=leading,color=color),
            content=ft.Text(
                value=text,
                color=color,
            ),          
            actions=[
                ft.TextButton(text="Закрыть", style=ft.ButtonStyle(color=color), on_click=self.close_banner),
            ],
            on_visible=self.on_visible_banner,
        )
    def on_visible_banner(self,e:ft.ControlEvent=None):
        sleep(2)
        self.open = False
        self.update()

    def close_banner(self,e:ft.ControlEvent=None):
        e.control.page.close(e.control.parent)