import unittest
from zktest import *
from pyZookeeper import nodepath


class TEST_ZKTEST(unittest.TestCase):
    global zkTest
    global nodepath
    nodepath = "/zookeeper/quota/test"
    
    def setUp(self):
        zkTest = ZkTest()
    
    def test_read(self):
        self.assertTrue(zkTest.read(nodepath), "Successful Test")
        
    def test_write(self):
        self.assertTrue(zkTest.write_data("Some data"), "Successful Test")
