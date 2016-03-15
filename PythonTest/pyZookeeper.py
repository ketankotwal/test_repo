from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import logging
from kazoo.client import KazooClient
import hashlib

class PyZookeeper(FileSystemEventHandler):
    
    global first_zk
    global nodepath, nodepath_hash

    @staticmethod
    def write_data(new_data):
        first_zk.ensure_path(nodepath)
        first_zk.set(nodepath, new_data)
        print "Updated node data"
        
    @staticmethod
    def write_hash(hashedData):
        first_zk.ensure_path(nodepath_hash)
        first_zk.set(nodepath_hash, hashedData)
        print "Updated hash"
    
    @staticmethod
    def generate_hash(cleartext):
        hashlib_obj = hashlib.sha256()
        hashlib_obj.update(cleartext)
        hashedData = hashlib_obj.hexdigest()
        return hashedData

    def on_any_event(self, event):
        # FileSystemEventHandler.on_any_event(self, event)
        print event.event_type
        print event.is_directory
        print event.src_path
        contents = open(event.src_path, 'r').read()
        hashedContents = PyZookeeper.generate_hash(contents)
        print "Hash :"
        print hashedContents
        # print contents
        print "\n"
        print "Writing data & hash to Zookeeper node..."
        PyZookeeper.write_hash(hashedContents)
        PyZookeeper.write_data(contents)
        print "\nFinished writing data & hash to node."
    
    def dispatch(self, event):
        # FileSystemEventHandler.dispatch(self, event)
        print "\n"
        print "------------------- START -----------------------"
        PyZookeeper.on_any_event(self, event)
        print "------------------- END -----------------------"
        print "\n"
    
   

print "Starting execution.."

nodepath = "/zookeeper/quota/test3"
nodepath_hash = "/zookeeper/quota/test3_hash"
        
logging.basicConfig()
first_zk = KazooClient(hosts='127.0.0.1:2181')
first_zk.start()
print "Connected to zookeeper 1.."

path = './source/src.txt';
observer = Observer()
eventHandler = PyZookeeper()
observer.schedule(eventHandler, path, True)
observer.start()

print "Added watcher for file.."
    
try:
    while True:
        print "Waiting for file changes.."
        time.sleep(10)
except KeyboardInterrupt:
    first_zk.stop()

