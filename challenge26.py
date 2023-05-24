#!usr/bin/python3

import logging

# Set up the logger
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
        logging.info('Successfully read the file %s', filename)
        # Processing data...
        return data
    except FileNotFoundError:
        logging.error('Failed to open the file %s', filename)
    except Exception as e:
        logging.error('An unexpected error occurred: %s', str(e))

process_file('test.txt')

def process_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    # Processing data...
    return data
