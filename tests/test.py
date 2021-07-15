import sys
import unittest
import os
from past.builtins import execfile
from tests.tmp_operations import test_operations

here = os.path.dirname(os.path.realpath(__file__))


class Tests(unittest.TestCase):
    @staticmethod
    def create_temp_file(temp_operation):
        f = open(here+'/tmp_operations/temp_operation_file', 'r+')
        f.seek(0)
        f.truncate()
        f.write(temp_operation)
        f.close()

    def test_authorize(self):
        n = 1
        for test in test_operations:
            print(n)
            n = n + 1
            self.create_temp_file(test)
            in_file = open(here+'/tmp_operations/temp_operation_file', 'r')
            sys.stdin = in_file
            execfile(here+"/../authorizator.py")
            in_file.close()
