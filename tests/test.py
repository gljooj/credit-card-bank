import os
import sys
import unittest
import subprocess

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
            print(f"Operation test: {n}")
            n = n + 1
            self.create_temp_file(test)
            in_file = open(here+'/tmp_operations/temp_operation_file', 'r')
            sys.stdin = in_file
            command = ['python3', here+"/../authorizator.py"]
            try:

                resultado = subprocess.run(command, stdin=in_file, capture_output=True, text=True)
                print(resultado.stdout)
                assert True
            except Exception as e:
                raise Exception(f"Fail to run test {n} error: {e}")
