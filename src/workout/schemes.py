from dataclasses import dataclass

from typing import Optional

from enum import Enum

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

class TypeClassicalButton(Enum):
    NORMAL = 0
    ERROR = 1

class TypeClassicalBanner(Enum):
    INFO = 0
    SUCCESSFUL = 1
    WARNING = 2
    ERROR = 3