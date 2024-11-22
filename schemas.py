from pydantic import BaseModel
from enum import Enum
from typing import Optional
import rsa


publicKey, privateKey = rsa.newkeys(512)



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
        separator = b'\xFF'  
        model_to_bytes = self.model.name.encode('utf-8')
        year_to_bytes = str(self.year).encode('utf-8')
        color_to_bytes = (self.color.value if self.color else "").encode('utf-8')
        price_to_bytes = f'{self.price:.2f}'.encode('utf-8')
        
        combined_data = separator.join([model_to_bytes, year_to_bytes, color_to_bytes, price_to_bytes])
        
        encrypt = rsa.encrypt(combined_data, publicKey)

        return encrypt
    
    
    @classmethod
    def from_bytes(cls, data: bytes):
        '''
        Convert bytes back to a Car object
        '''
        separator = b'\xFF'
        
        # Decrypt the data
        decrypted_data = rsa.decrypt(data, privateKey).decode('utf-8')
        
        # Split the decrypted data using the separator
        model_name, year_str, color_value, price_str = decrypted_data.split(separator.decode('utf-8'))
        
        # Parse the data back into appropriate types
        model = CarModel[model_name]  # Access Enum by name
        year = int(year_str)
        color = CarColour(color_value) if color_value else None  # Handle optional color
        price = float(price_str)
        
        # Return the Car instance
        return cls(model=model, year=year, color=color, price=price)