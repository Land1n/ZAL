import flet as ft

from src.UI import WorkoutCard
from src.database import get_data_workouts
from src.schemes import Workout

class BaseView(ft.View):
    def view_pop(self,view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

class HomeView(BaseView):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page
        self.route = '/home'
        self.appbar = ft.AppBar(
            leading = ft.IconButton(icon=ft.icons.MENU, on_click=lambda _: self.page.open(self.drawer)),
            title = ft.Text("ZAL",size=30,font_family="Dimkin Regular"),
            center_title = True,
            actions = [ft.IconButton(icon=ft.icons.ADD)]
        )    
        workouts = get_data_workouts()
        for workout in workouts:
            workout = Workout(**workout)
            self.controls.append(WorkoutCard(workout.id,workout.title,workout.subtitle,workout.avatar_color))
class WorkoutView(BaseView):
    def __init__(self,page:ft.Page,id:int):
        super().__init__()
        self.page = page
        self.id = id
        self.appbar = ft.AppBar(
            leading=ft.IconButton(ft.icons.ARROW_BACK,on_click=self.view_pop),
            title=ft.Text('Тренировка'),
            # actions=[ft.IconButton(ft.icons.START)]
        )
        self.workout = Workout(**(get_data_workouts(self.id)[0]))
        self.controls = [
            ft.Text(self.workout.title,size=40),
            ft.Text(self.workout.subtitle),
            ft.Divider(),
            ft.Text("Список упражнений",size=30),

        ]
        if self.workout.annotation:
            self.controls.insert(2,ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.INFO),
                                title=ft.Text("Важные моменты"),
                                subtitle=ft.Text(self.workout.annotation),
                            ),
                        ]
                    ),
                    padding=10,
                )
            ))