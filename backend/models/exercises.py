from beanie import Document,Link
from typing import Optional, List

class ExerciseCategory(Document):
    name: str
    description: str

class Equipment(Document):
    name: str
    description: str

class Exercise(Document):
    name: str
    description : Optional[str] 
    # Связь с категорией упражнений
    category: Link[ExerciseCategory]
    # Список оборудования, необходимого для выполнения упражнения
    equipments: Optional[List[Link[Equipment]]]
    # Список подупражнений, если упражнение состоит из нескольких частей
    # sub_exercises: List[Link["Exercise"]] = []