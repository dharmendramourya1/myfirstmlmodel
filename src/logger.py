import logging
import os
import sys
from datetime import datetime
import execpetion
from execpetion import CustomException   # ✅ correct import

# Create dynamic log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs directory if not exists
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")

    try:
        a = 1 / 0  # This will cause ZeroDivisionError
    except Exception as e:
        logging.error("An exception occurred")
        raise CustomException(e, sys)
