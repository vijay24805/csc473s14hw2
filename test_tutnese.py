# test_Tutnese
# Author: Vijaya Kumar V

import unittest

class tutneseTesting(unittest.TestCase):
    
    @classmethod
    def setUp(self):

        """
       setUp is called before each test function execution.
        """

    @classmethod
    def tearDown(self):
	""" Function for cleaning up after tests:
        """



    def testencode(self):
      try:
         assert self == str
      except AssertionError,e:
         raise Exception('Not a valid argument')


    def testdecode(self):
      try:
         assert self != str
      except AssertionError, e:
         raise Exception("not a valid argument")

