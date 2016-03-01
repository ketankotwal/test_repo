
from kazoo.client import KazooClient
from kazoo.recipe.watchers import ChildrenWatch
from kazoo.recipe.watchers import DataWatch
import time

class Test:
    
    global second_zk
    global nodepath
    nodepath = "/zookeeper/quota/test3"
    nodepath_hash = "/zookeeper/quota/test3_hash"
    second_zk = KazooClient(hosts='127.0.0.1:2181')
    second_zk.start()
    print "Connected to zookeeper 2.."


    @staticmethod
    def print_new_data(children, event):
        print '\n'
        print dir(children)
        print event
        
        if event != None:
            event.path
            
        print dir(event)
       # print event
       
    @staticmethod
    def data_watch(data, stat, event):
        print stat
        print event
        if event != None:
            print event.path


cw = ChildrenWatch(second_zk, nodepath, Test.print_new_data, True, True) 
dw = DataWatch(second_zk, nodepath, Test.data_watch)   
   
test = Test()

try:
    while True:
        print "Waiting for node changes.."
        time.sleep(10)
except KeyboardInterrupt:
    second_zk.stop()

print 'Done'