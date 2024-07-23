import flet as ft


class TrainCard(ft.Card):
    def __init__(self,title:str,subtitle:str):
        super().__init__()
        self.margin = 0
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
                        [ft.TextButton("Начать тренировка")],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            height=125,
            padding=10,
        )
    
    @property
    def card_height(self):
        return self.content.height

class MyAppBar(ft.AppBar):
    def __init__(self,page:ft.Page,drawer = None):
        super().__init__()
        self.page = page
        self.leading=ft.IconButton(icon=ft.icons.MENU,on_click=self.open_drawer)
        self.title=ft.Text("ZAL")
        self.center_title=True
        self.actions=[ft.IconButton(icon=ft.icons.ADD) ]
        if drawer != None:
            self._drawer = drawer
        else:
            self._drawer = None
        
    
    def open_drawer(self,e):
        if self._drawer != None:
            self.page.open(self._drawer)
        else:
            print(f"{self.drawer=}")
        return None
    @property
    def drawer(self):
        if self._drawer != None:
            return self._drawer
        return None

    @drawer.setter
    def drawer(self,drawer):
        self._drawer = drawer



def main(page:ft.Page):
    page.title = 'ZAL'




    drawer = ft.NavigationDrawer(
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
    
    page.appbar = MyAppBar(page,drawer)
    cl = ft.Column(
        scroll=ft.ScrollMode.HIDDEN,
        height = page.height*0.9
    )
    def resized(*arg):
        cl.height = page.height*0.9
        print( cl.height)
        cl.update()
        page.update()

    
    page.on_resized = resized
    for i in range(1, 7):
        w = TrainCard(str(i),'...')
        cl.controls.append(w)

    page.add(cl)



if __name__ == '__main__':
    ft.app(main)