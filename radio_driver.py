import serial
import time
from schemas import Car
import logging

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s %(levelname)s]: %(message)s"
)

baund_rate = 9600

class RadioController:
    
    mock = False # no radio connected, enables us to run anyway
    
    def __init__(self):
        try:
            self.connect_to_open_radio_port()
        except RuntimeError:
            print('Count not open port, mocking the radio')
            self.mock = True
    
    
    def connect_to_open_radio_port(self):
        for i in range(10):
            candidate_port_address = f'COM{i}'
            print(f'Trying {candidate_port_address}')
            try:
                self.radio_port = serial.Serial(
                    candidate_port_address, baund_rate, timeout=1
                )
                time.sleep(1)
                return
            except serial.SerialException as e:
                pass
        raise RuntimeError(
            "Can't find an open radio port, is there one plugged? Check it"
        )
    
    
    def send(self, msg: Car):
        if self.mock:
            return 
        serialized = serialize(data=msg)
        logger.info(f'[SEND] Radio message {serialized}')
        self.radio_port.write(serialized)
        
    def get_next_message(self) -> Car:
        if self.radio_port.in_waiting <=0:
            return None 
        deserialized = deserialize(data=msg)
        logger.info('Deserializing message...')
        logger.info(f'[RECEIVED] Radio message {deserialized}')
        
        
def serialize(data: Car)->bytes:
    '''
    Serializing the message
    '''
    ...
        
    
def deserialize(data:bytes) -> Car:
    '''
    Deserialize and get the message itself
    '''

        
            
            
            