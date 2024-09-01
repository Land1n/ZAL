import flet as ft

from src.database import DataBase

class RoundReadDataRow(ft.DataRow):
    def __init__(self,id:int,weight:int,repetitions:int,time:int):

        self.id = id

        self.weight_row = ft.Ref[ft.DataCell]()
        self.repetitions_row = ft.Ref[ft.DataCell]()
        self.time_row = ft.Ref[ft.DataCell]()

        self.cells = [
            ft.DataCell(ref=self.weight_row,content=ft.Text(weight+ " кг.")),
            ft.DataCell(ref=self.repetitions_row,content=ft.Text(repetitions)),
            ft.DataCell(ref=self.time_row,content=ft.Text(time+" мин.")),
        ]
        super().__init__(
            cells=self.cells,
            on_long_press=self.update_cell
        )

    def update_cell(self,e:ft.ControlEvent):
        print(DataBase(e=e).get_obj(self.id))

class RoundReadDataTable(ft.DataTable):
    def __init__(self,rows:list[RoundReadDataRow] = [],visible:bool=True):
        self.rows = rows
        super().__init__(
            visible=visible,
            rows=self.rows,
            columns=[
                ft.DataColumn(ft.Text("Вес"),numeric=True),
                ft.DataColumn(ft.Text("Повторения"),numeric=True),
                ft.DataColumn(ft.Text("Время отдыха"), numeric=True),
            ],
        )