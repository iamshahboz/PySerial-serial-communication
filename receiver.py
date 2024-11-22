from radio_driver import RadioController
import logging
import time

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s %(levelname)s]: %(message)s"
)



radio = RadioController()



def listen_to_incoming_message():
    logger.info("Listening for incoming messages...")
    try:
        while True:
            message = radio.get_next_message()
            if message:
                logger.info(f"Received message: {message}")
            time.sleep(0.1)  # Prevent tight looping
    except KeyboardInterrupt:
        logger.info("Stopped listening to incoming messages.")
    
    
    
if __name__ == "__main__":
    listen_to_incoming_message()