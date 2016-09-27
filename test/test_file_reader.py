#! usr/bin/env python3

import os
import sys
import unittest

# Here we're moving the context into the parent folder
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

from application import file_reader

class TestFileOpen(unittest.TestCase):
    '''
    Test this function returns data from a file upload.
    '''

    def test(self):
        file_location = 'test/test_data.cells'
        data = file_reader.get_board_data(file_location)
        assert data[0][0] == '.'
        assert data[0][1] == 'O'
        assert data[1][0] == 'O'
        assert data[1][1] == '.'

if __name__ == '__main__':
    unittest.main()

