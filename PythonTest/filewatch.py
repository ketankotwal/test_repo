
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import logging
from zktest import ZkTest

class FileWatchHandler(FileSystemEventHandler):
    
    
    def on_modified(self, event):
        # FileSystemEventHandler.on_modified(self, event)
        print event
        
    def on_any_event(self, event):
        # FileSystemEventHandler.on_any_event(self, event)
        print event.event_type
        print event.is_directory
        print event.src_path
        contents = open(event.src_path, 'r').read()
        # print contents
        print "\n"
        print "Writing data to Zookeeper node..."
        ZkTest.write_data(contents)
        print "\nFinished writing data to node."
    
    def dispatch(self, event):
        # FileSystemEventHandler.dispatch(self, event)
        print "\n"
        print "------------------- START -----------------------"
        FileWatchHandler.on_any_event(self, event)
        print "------------------- END -----------------------"
        print "\n"
        
        
logging.basicConfig()
# path='E:/DEV_ENV/Tools/zookeeper/zookeeper-3.4.6/bin/test.txt';
path = '.';
observer = Observer()
eventHandler = FileWatchHandler()
observer.schedule(eventHandler, path, True)
observer.start()

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    observer.stop()

observer.join()
        
        
