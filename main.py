import flet as ft


class TrainingCard(ft.Card):
    def __init__(self,id:int,title:str,subtitle:str):
        super().__init__()
        self.id = id
        self.content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.CircleAvatar(content=ft.Text('В')),
                        title=ft.Text(title),
                        subtitle=ft.Text(subtitle),
                        trailing=ft.PopupMenuButton(
                            icon=ft.icons.MORE_VERT,
                            items=[
                                ft.PopupMenuItem(text="Изменить"),
                                ft.PopupMenuItem(text="Удалить"),
                            ],
                        ),
                    ),
                    ft.Row(
                        [ft.TextButton("Подробнее",on_click=lambda _:self.page.go(f"/train/{self.id}"))],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            height=125,
            padding=10,
        )

class HomeView(ft.View):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page
        self.route = '/home'
        self.drawer = ft.NavigationDrawer(
            selected_index=-1,
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="User",
                    icon_content=ft.CircleAvatar(
                        content=ft.Text('A'),
                    ),
                                    
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.SETTINGS),
                    label="Настройки",
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.SETTINGS),
                    label="Настройки",
                ),
            ],
        )
        self.appbar = ft.AppBar(
            leading = ft.IconButton(icon=ft.icons.MENU, on_click=lambda _: self.page.open(self.drawer)),
            title = ft.Text("ZAL"),
            center_title = True,
            actions = [ft.IconButton(icon=ft.icons.ADD)]
        )    
        self.controls = [
             ft.Column(
                [TrainingCard(i,str(i),'...') for i in range(1, 6)],
                scroll=ft.ScrollMode.HIDDEN,
                height = page.height*0.9
            )
        ]

class TrainingView(ft.View):
    def __init__(self,page:ft.Page,id:int):
        super().__init__()
        self.page = page
        self.id = id
        self.controls = [
                ft.Text(str(self.id))
                ]
        self.appbar = ft.AppBar(
            leading=ft.IconButton(ft.icons.ARROW_BACK,on_click=self.view_pop),
            title=ft.Text('Тренировка'),
            actions=[ft.IconButton(ft.icons.START)]
        )
    def view_pop(self,view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
class Router:
    def __init__(self,page:ft.Page):
        self.page = page
        self.home_view = HomeView(self.page)
    def route_change(self,route):
        self.page.views.clear()

        troute = ft.TemplateRoute(self.page.route)
        self.page.views.append(self.home_view)

        if troute.match("/train/:id"):
            self.page.views.append(TrainingView(self.page,troute.id))
        self.page.update()

    def view_pop(self,view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)




def main(page:ft.Page):
    page.title = 'ZAL'
    router = Router(page)

    # def resized(*arg):
    #     cl.height = page.height*0.9
    #     print( cl.height)
    #     cl.update()
    #     page.update()

    # # page.on_resized = resized

    page.on_route_change = router.route_change
    page.on_view_pop = router.view_pop

    page.go(page.route)



if __name__ == '__main__':
    ft.app(main)