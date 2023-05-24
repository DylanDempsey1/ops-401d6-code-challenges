import logging
from logging.handlers import RotatingFileHandler

# Define the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Define a RotatingFileHandler that will log to a file called 'my_log.log', 
# with a max size of 5MB and keep up to 5 backup files
handler = RotatingFileHandler('my_log.log', maxBytes=5*1024*1024, backupCount=5)

# Add a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Now you can use the logger to log messages
logger.info('This is an example log message')
