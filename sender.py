from schemas import Car, CarColour, CarModel
from radio_driver import RadioController
from pydantic import BaseModel



class RadioMsg(BaseModel):
    '''
    not implemented
    '''
    pass


message = Car(model=CarModel.TOYOTA, year=2012, color=CarColour.BLACK, price=8000)
# initialize RadioController class
radio = RadioController()
radio.send(msg=message)
