# https://docs.python.org/3/library/logger.html#logger.basicConfig

from logger import logger

# logger.warning('This is logged in a file : Called in the file')

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

def CreateError():
    logger.debug("Inside the function")

    try:
        a = 10
        b = 0
        c = 10 / 0
    except Exception as e:
        logger.error(f"Error in {CreateError.__name__} Function : {e}")

CreateError()


print(logger.getEffectiveLevel())