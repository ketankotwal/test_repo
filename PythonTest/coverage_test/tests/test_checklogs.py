import unittest
from coverage_test.src.checklogs import *

class TestCheckLogs(unittest.TestCase):
    
    def test_checklogs(self):
        self.assertTrue(check_logging(), "test failed")

#if __name__ == "__main__":
#    unittest.main()