
import logging 


def get_basic_logger():
    
    logger = logging.getLogger('basic_logger') 
    
    logger.setLevel(logging.DEBUG)
    
    filehandler = logging.FileHandler('basic.log', mode='a')
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    filehandler.setFormatter(formatter)
    
    logger.addHandler(filehandler)
    
    return logger


def get_event_logger():
    
    logger = logging.getLogger('event_logger') 
    
    logger.setLevel(logging.DEBUG)
    
    filehandler = logging.FileHandler('event.log')
    streamhandler = logging.StreamHandler()
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    filehandler.setFormatter(formatter)
    
    logger.addHandler(filehandler)
    logger.addHandler(streamhandler)
    
    return logger


def get_audit_logger():
    
    logger = logging.getLogger('event_logger') 
    
    logger.setLevel(logging.DEBUG)
    
    filehandler = logging.FileHandler('event.log')
    streamhandler = logging.StreamHandler()
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    filehandler.setFormatter(formatter)
    
    logger.addHandler(filehandler)
    logger.addHandler(streamhandler)
    
    return logger


def get_error_logger():
    
    logger = logging.getLogger('event_logger') 
    
    logger.setLevel(logging.DEBUG)
    
    filehandler = logging.FileHandler('event.log')
    streamhandler = logging.StreamHandler()
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    filehandler.setFormatter(formatter)
    
    logger.addHandler(filehandler)
    logger.addHandler(streamhandler)
    
    return logger
