from pydantic import BaseModel
from enum import IntEnum
from typing import Optional 


# Enum class for Car models
class CarModel(IntEnum):
    TOYOTA = 1
    FORD = 2
    BMW = 3 
    NISSAN = 4
    HYUNDAI = 5 
    MERCEDES = 6
    
    
# Enum class for Car color   
class CarColour(IntEnum):
    RED = "Red"
    BLUE = "Blue"
    BLACK = "Black"
    WHITE = "White"
    SILVER = "Silver"
    GREY = "Grey"
    GREEN = "Green"
    YELLOW = "Yellow"
    ORANGE = "Orange"
    BROWN = "Brown"
    GOLD = "Gold"
    PURPLE = "Purple"


class Car(BaseModel):
    model: CarModel
    year: int
    color: Optional[CarColour]
    price: float