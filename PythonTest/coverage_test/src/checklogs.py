
from loggers import *

def check_logging():
    basiclogger = get_basic_logger()
    eventlogger = get_event_logger()
    
    basiclogger.info("Basic log 1")
    basiclogger.error("Basic log 2")
    
    eventlogger.info("Event log 1")
    eventlogger.error("Event log 2")
    
    return True