
from kazoo.client import KazooClient
import logging
from loggers import *

class ZkWriteData:
    
    global zk, logger
    logging.basicConfig()
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    #streamhandler = logging.StreamHandler()
    #streamhandler.setFormatter(formatter)
    
    filehandler = logging.FileHandler('zk.log', mode='a')
    filehandler.setFormatter(formatter)
    
    logger = logging.getLogger()
    
    #logger.addHandler(streamhandler)
    logger.addHandler(filehandler)
    
    logger.setLevel(logging.DEBUG)
    
    zk = KazooClient(hosts='127.0.0.1:2181')
    zk.start()
        
    

    def read(self, nodePath):
        data, stat = zk.get(nodePath)
        logger.info("Version: %s" % (stat.version))
        logger.info("Data: %s" % (data.decode("utf-8")))

        #print("Version: %s" % (stat.version))
        #print("Data: %s" % (data.decode("utf-8")))


zkwritedata = ZkWriteData()
zkwritedata.read('/zookeeper/quota/test2')
    