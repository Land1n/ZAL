from dataclasses import dataclass

from typing import Optional

@dataclass
class Round:
    id:int
    weight:int
    repetitions:str 
    time:int

@dataclass
class Exercises:
    id:int
    title:str
    annotation:Optional[str]
    rounds:list[Round] 

@dataclass
class Workout:
    id:int
    title:str
    subtitle:str
    annotation:Optional[str] 
    avatar_color:str
    exercises:list[Exercises] 