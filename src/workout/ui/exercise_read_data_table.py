import flet as ft

from typing import Optional

from src.workout.schemes import Round

class ExerciseReadDataRow(ft.DataRow):
    def __init__(self,id:int,title:str,annotation:str,rounds:list[Round]):

        self.title_row = ft.Ref[ft.DataCell]()
        self.annotation_row = ft.Ref[ft.DataCell]()
        self.rounds_row = ft.Ref[ft.DataCell]()


        self.cells = [
            ft.DataCell(ref=self.title_row,content=ft.Text(value=title)),
            ft.DataCell(ref=self.annotation_row,content=ft.Text("Да" if annotation else "Нет")),
            ft.DataCell(ref=self.rounds_row,content=ft.Text(f"{len(rounds)}")),
        ]
        super().__init__(
            cells=self.cells,
            on_long_press=lambda _: print(
                self.title_row.current.content.value,
                self.annotation_row.current.content.value,
                self.rounds_row.current.content.value,              
            )
        )

class ExerciseReadDataTable(ft.DataTable):
    def __init__(self,rows:list[ExerciseReadDataRow] = [],visible:bool=True):
        self.rows = rows
        super().__init__(
            visible=visible,
            rows=self.rows,
            columns=[
                ft.DataColumn(ft.Text("Название")),
                ft.DataColumn(ft.Text("Аннотация")),
                ft.DataColumn(ft.Text("Походы"), numeric=True),
            ],
        )