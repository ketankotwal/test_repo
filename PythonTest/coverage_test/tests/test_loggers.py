import unittest
from coverage_test.src.loggers import *


class TestLoggers(unittest.TestCase):
    
    def test_basic_logger(self):
        self.assertIsNotNone(get_basic_logger(), "test basic logger")
        
    def test_event_logger(self):
        self.assertIsNotNone(get_event_logger(), "test event logger")

    def test_audit_logger(self):
        self.assertIsNotNone(get_audit_logger(), "test audit logger")
        
    def test_error_logger(self):
        self.assertIsNotNone(get_error_logger(), "test error logger")        

if __name__ == "__main__":
    unittest.main()