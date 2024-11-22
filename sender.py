from schemas import Car, CarColour, CarModel
from radio_driver import RadioController
from pydantic import BaseModel



class RadioMsg(BaseModel):
    '''
    not implemented
    '''
    pass

radio = RadioController()


def send_message():
    message = Car(model=CarModel.TOYOTA, year=2012, color=CarColour.BLACK, price=8000)
    radio.send(msg=message)
    




if __name__ == "__main__":
    send_message()
