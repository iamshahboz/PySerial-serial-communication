from radio_driver import RadioController
import logging

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s %(levelname)s]: %(message)s"
)



radio = RadioController()

def listen_to_incoming_message():
    radio.get_next_message()
    
    
    
if __name__ == "__main__":
    listen_to_incoming_message()