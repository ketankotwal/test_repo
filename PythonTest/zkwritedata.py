
from kazoo.client import KazooClient
import logging
import time

class ZkWriteData:
    
    global zk
    logging.basicConfig()
    zk = KazooClient(hosts='127.0.0.1:2181')
    zk.start()