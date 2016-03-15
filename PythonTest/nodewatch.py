import time
from kazoo.client import KazooClient
import hashlib
from kazoo.recipe.watchers import DataWatch

class NodeWatch:
    
    global second_zk
    global nodepath, nodepath_hash
    global nodewatch
    
    # nodewatch = NodeWatch()
    nodepath = "/zookeeper/quota/test3"
    nodepath_hash = "/zookeeper/quota/test3_hash"
    second_zk = KazooClient(hosts='127.0.0.1:2182')
    second_zk.start()
    print "Connected to zookeeper 2.."

    @staticmethod
    def generate_hash(cleartext):
        hashlib_obj = hashlib.sha256()
        hashlib_obj.update(cleartext)
        hashedData = hashlib_obj.hexdigest()
        return hashedData


    @staticmethod   
    def compare_hash(cleartext):
        hashedData = NodeWatch.generate_hash(cleartext)
        nodeHash, stat = second_zk.get(nodepath_hash)
        print "Current hash : " + hashedData
        print "Node hash : " + nodeHash
        if hashedData == nodeHash:
            print "Hashes match"
            return True
        else:
            print "Hashes do not match"
            return False
        
    
    @staticmethod    
    def print_new_data(data, stat):
        print '\n'
        print data        
        # NodeWatch.compare_hash(data)
        time.sleep(5)
        print "Writing to dest file..."
        newfile = open('destination/dest.txt', 'w')
        newfile.write(data)
        newfile.close()
        
        localfile = open('destination/dest.txt', 'r')
        localfilecontents = localfile.read()
        localfile.close()
        
        result = NodeWatch.compare_hash(localfilecontents)
            
        if result:
            print "Files successfully synced !"
        else:
            print "Error syncing files !"
        # print stat.version
        # print stat.mtime

print "Starting execution.."

dw = DataWatch(second_zk, nodepath, NodeWatch.print_new_data)    
nodewatch = NodeWatch()

try:
    while True:
        print "Waiting for node changes.."
        time.sleep(10)
except KeyboardInterrupt:
    second_zk.stop()

