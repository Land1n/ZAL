import flet as ft

class RoundReadDataRow(ft.DataRow):
    def __init__(self,id:int,weight:int,repetitions:int,time:int):

        self.weight = ft.Ref[ft.DataCell]()
        self.repetitions = ft.Ref[ft.DataCell]()
        self.time = ft.Ref[ft.DataCell]()

        self.cells = [
            ft.DataCell(ref=self.weight,content=ft.Text(weight)),
            ft.DataCell(ref=self.repetitions,content=ft.Text(repetitions)),
            ft.DataCell(ref=self.time,content=ft.Text(time)),
        ]
        super().__init__(cells=self.cells)

class RoundReadDataTable(ft.DataTable):
    def __init__(self,rows:list[RoundReadDataRow] = []):
        self.rows = rows
        
        super().__init__(
            columns=[
                ft.DataColumn(ft.Text("Вес"),numeric=True),
                ft.DataColumn(ft.Text("Повторения"),numeric=True),
                ft.DataColumn(ft.Text("Время отдыха"), numeric=True),
            ],
            rows=self.rows
        )
