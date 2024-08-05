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
