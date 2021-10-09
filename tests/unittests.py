# Make sure testwheel is installed before running tests
# Either build the wheel and install it, or run "pip install ." from the root of this project

import unittest
from testwheel import test_module

class TestMethods(unittest.TestCase):
    def test_fib(self):
        fib_seq = [test_module.fib(i) for i in range(1, 6)]
        self.assertListEqual(fib_seq, [1, 1, 2, 3, 5])

if __name__ == '__main__':
    unittest.main()
