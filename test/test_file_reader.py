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
    Test this function returns a trained mnb classifier.
    We'll test this against data we've trained.
    '''

    def test(self):
        file_location = 'test_data.txt'
        data = file_reader.get_board_data(file_location)
        assert data[0][0] == 0
        assert data[0][1] == 1
        assert data[1][0] == 1
        assert data[1][1] == 0

if __name__ == '__main__':
    unittest.main()

