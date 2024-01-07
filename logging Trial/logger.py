import logging


# logger = logging.getLogger(__name__) # gives file name when __name__
logger = logging.getLogger("SKLogger") # gives file name when __name__

"""
    5 levels in the logging
    info : Basic info of the running state of process
    debug : Used for debugging generally
    warning : This is not error but it is used when something happened  which should not happen but it does not affect the process
    critical : When there is some critical problem in the code (like heavy CPU utilization or process in deadlock something like that)
    error : As it says, when error occurs

"""


# Handlers
"""
    This will handle different stream for logging
"""

c_handler = logging.StreamHandler()  # This will add logs in console also
c_handler.setLevel(level=logging.INFO)  # This will set level to info

f_handler = logging.FileHandler(
    "app.log"
)  # while store the logs in app.log in append format
# f_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.INFO)


# Google how can we arrange logs format in different ways
c_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s")
f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s")

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)


# Adding handlers to logger object created on line 4
logger.addHandler(c_handler)
logger.addHandler(f_handler)
