import flet as ft

from src.home.view import HomeView

from src.workout.view import WorkoutReadView,WorkoutCreateView

class Router:
    def __init__(self,page:ft.Page):
        self.page = page
        self.home_view = HomeView(self.page)
    def route_change(self,route):
        self.page.views.clear()

        troute = ft.TemplateRoute(self.page.route)
        self.page.views.append(self.home_view)

        if troute.match("/workout/:id"):
            self.page.views.append(WorkoutReadView(self.page,troute.id))
        if troute.match("/workout/create"):
            self.page.views.append(WorkoutCreateView(self.page))    
        self.page.update()