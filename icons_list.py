import flet as ft
import flet_core
import re

def main(page: ft.Page):

    def item_list(icons_name:str):
        return ft.ListTile(
                    leading=ft.Icon(icons_name),
                    title=ft.Text(icons_name),
                )

    def on_change(e):
        lv.controls.clear()
        try:
            for icon in flet_core.icons.icons_list:
                if any([re.search(f'{field.value}',icon) ,(not field.value)]):
                    lv.controls.append(item_list(icon))
            lv.update()
        except:
            lv.controls.clear()
            lv.update()
    lv = ft.ListView(expand=True, spacing=10)
    field=ft.TextField(hint_text='Название иконки',on_change=on_change)
    for icon in flet_core.icons.icons_list:
        lv.controls.append(item_list(icon))
    page.add(field)
    page.add(lv)

ft.app(main)