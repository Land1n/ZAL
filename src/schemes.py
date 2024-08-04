from dataclasses import dataclass

@dataclass
class Exercises:
    id:int
    title:str
    annotation:str
    round:int 
    weight:int
    repetitions:str 
    time:int

@dataclass
class Workout:
    id:int
    title:str
    subtitle:str
    annotation:str 
    avatar_color:str
    exercises:list[Exercises] 