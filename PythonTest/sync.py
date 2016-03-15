from kazoo.client import KazooClient
import hashlib
from pamconstants import PAMConstants

class PySync:
    
    global zk
    
    zk = KazooClient(hosts=PAMConstants.ZK_CONN_URL)
    zk.start()
    print "Connected to Zookeeper"
    
    
    @staticmethod
    def generate_hash(cleartext):
        hashlib_obj = hashlib.sha256()
        hashlib_obj.update(cleartext)
        hashed_data = hashlib_obj.hexdigest()
        return hashed_data
    
    @staticmethod
    def get_file_content_and_hash(filepath):
        file_contents = open(filepath, PAMConstants.FILEMODE_READ).read()
        file_contents_hash = PySync.generate_hash(file_contents)
        return file_contents, file_contents_hash

        
pathlistfile = open(PAMConstants.FILELIST, PAMConstants.FILEMODE_READ)
pathlist = pathlistfile.read().splitlines()
print "Files to sync.."    
print ', '.join(pathlist)
print '\n'
print 'Starting sync..'
    
    
for path in pathlist:
    nodepath = PAMConstants.ZK_BASEPATH + path
    print "Processing node - " + nodepath
    if zk.exists(nodepath) != None:
        file_contents, file_contents_hash = PySync.get_file_content_and_hash('.' + path)
        zk.set(nodepath, file_contents_hash)
    else:
        zk.create(nodepath, path, None, False, False, True)

print "Done"
    
