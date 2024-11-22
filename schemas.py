from pydantic import BaseModel
from enum import Enum
from typing import Optional 



# Enum class for Car models
class CarModel(Enum):
    TOYOTA = 1
    FORD = 2
    BMW = 3 
    NISSAN = 4
    HYUNDAI = 5 
    MERCEDES = 6
    
    
# Enum class for Car color   
class CarColour(Enum):
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
    
    def to_bytes(self):
        '''
        Convert the data of the class to bytes
        '''
        bytes_list = []
        model_to_bytes = self.model.name.encode('utf-8')
        year_to_bytes = str(self.year).encode('utf-8')
        color_to_bytes = self.color.value.encode('utf-8')
        price_to_bytes = str(self.price).encode('utf-8')
        bytes_list.extend(model_to_bytes)
        bytes_list.extend(year_to_bytes)
        bytes_list.extend(color_to_bytes)
        bytes_list.extend(price_to_bytes)
        return bytes_list
    
