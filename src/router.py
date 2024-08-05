import flet as ft

from src.view import HomeView

from src.workout.view import WorkoutView

class Router:
    def __init__(self,page:ft.Page):
        self.page = page
        self.home_view = HomeView(self.page)
    def route_change(self,route):
        self.page.views.clear()

        troute = ft.TemplateRoute(self.page.route)
        self.page.views.append(self.home_view)

        if troute.match("/train/:id"):
            self.page.views.append(WorkoutView(self.page,troute.id))
        self.page.update()