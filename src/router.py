import flet as ft

from repath import match

from src.home.view.home import HomeView

from src.workout.view.exercise_create import ExerciseCreateView

from src.workout.view.workout_create import WorkoutCreateView
from src.workout.view.workout_read import WorkoutReadView
 
class RoutersDict:
    def __init__(self,routers:dict = {}):
        self.routers = routers
    def __getitem__(self, route):
        if view:=self.routers.get(route,False):
            return view
        if any(key:=r for r in self.routers.keys() if (value := match(r,route))):
            return self.routers.get(key,False)
        return None


class Router:
    def __init__(self,page:ft.Page):
        self.page = page
        self.routes = RoutersDict({
            "/home": HomeView,
            "/workout/:id": WorkoutReadView,
            "/workout/create": WorkoutCreateView,
            "/workout/create/exercise": ExerciseCreateView,
        })

    def route_change(self,route):
        if not [view for view in self.page.views if view.route == route.route]:
            self.page.views.append(self.routes[route.route](self.page))
        self.page.update()