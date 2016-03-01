
from kazoo.client import KazooClient
import logging
import time

class ZkTest:
    
    global zk
    #logging.basicConfig()
    zk = KazooClient(hosts='127.0.0.1:2181')
    zk.start()
    
    
    def __init__(self):
        print "INIT()"
    
    @staticmethod    
    def read(nodePath):
        data, stat = zk.get(nodePath)
        print("Version: %s" % (stat.version))
        print("Data: %s" % (data.decode("utf-8")))
    
    @staticmethod    
    @zk.DataWatch("/zookeeper/quota/test2")
    def print_new_data(data, stat):
        print '\n'
        print data   
        print stat.version
        #print stat.mtime
        
    @staticmethod
    def write_data(new_data):
        zk.set("/zookeeper/quota/test2", new_data)
        print "Updated new data"


    
zktest = ZkTest()
ZkTest.write_data("Dummy data")
ZkTest.read('/zookeeper/quota/test2')
#zktest.read('/zookeeper/quota/test2')

#while True:
#    time.sleep(2)
    
#zk.stop()
    
    
