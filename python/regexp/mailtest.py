__author__ = 'nightblues'
import sys
sys.path.append('..')
from regexp.mailchecker import *
import unittest

class TestMailCheck(unittest.TestCase):

    def testFirstCond(self):
        self.assertTrue(check_mail('qwerty@localhost'))
        self.assertFalse(check_mail('qwerty.localhost'))

    def testSecondCond(self):
        self.assertTrue(check_mail('qwerty@loc'))
        self.assertTrue(check_mail('qwerty@'+'localhost'*28))
        self.assertFalse(check_mail('qwerty@'+'localhost'*29))
        self.assertTrue(check_mail('qwerty@local.host.ru'))
        self.assertFalse(check_mail('qwerty@.local.host.ru'))

    def testThirdCond(self):
        self.assertTrue(check_mail('qwerty@local-host.ru'))
        self.assertFalse(check_mail('qwerty@local.-host.ru'))

    def testFourthCond(self):
        self.assertTrue(check_mail('qwe.rty@localhost'))
        self.assertFalse(check_mail('qwerty'*22+'@localhost'))

    def testFifthCond(self):
        self.assertFalse(check_mail('qwe..rty@localhost'))

    def testSixthCond(self):
        self.assertTrue(check_mail('qw"e.r"ty@localhost'))
        self.assertFalse(check_mail('qw"e.rty@localhost'))

    def testSeventhCond(self):
        self.assertTrue(check_mail('qw"!,:"ty@localhost'))
        self.assertFalse(check_mail('qw!,:ty@localhost'))


if __name__=="__main__":
    unittest.main()