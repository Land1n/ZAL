import flet as ft
from repath import match
# from 

class RoutersDict:
    def __init__(self,routers:dict = {}):
        self.routers = routers
    def __getitem__(self, route):
        if key:=self.routers.get(route,False):
            return key
        if any(key:=r for r in self.routers.keys() if (value := match(r,route))):
            return key
        return None
    def get(self,key):
        return self.__getitem__(key)

d = RoutersDict({
    'w/:id':"12",
    "w/create":'123123123   123w'
})
print(d["w/1"])