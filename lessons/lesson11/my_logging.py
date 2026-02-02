import logging

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='app.log',
    filemode='a'
)
logging.critical("\n\nLogging system initialized.\n")


if __name__ == "__main__":
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")