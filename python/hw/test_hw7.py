'''
Created on Mar 20, 2015

@author: Brian Borowski

CS115 - Hw 7 Test Script
'''
import unittest
import hw7

class Test(unittest.TestCase):

    def test01(self):
        self.assertEqual(hw7.TcToNum('10000000'), -128)
        self.assertEqual(hw7.TcToNum('10000001'), -127)
        self.assertEqual(hw7.TcToNum('11111111'), -1)
        self.assertEqual(hw7.TcToNum('00000000'), 0)
        self.assertEqual(hw7.TcToNum('00000001'), 1)
        self.assertEqual(hw7.TcToNum('01000000'), 64)
        self.assertEqual(hw7.TcToNum('01111110'), 126)
        self.assertEqual(hw7.TcToNum('01111111'), 127)

    def test02(self):
        self.assertEqual(hw7.NumToTc(128), 'Error')
        self.assertEqual(hw7.NumToTc(-129), 'Error')
        self.assertEqual(hw7.NumToTc(-128), '10000000')
        self.assertEqual(hw7.NumToTc(-127), '10000001')
        self.assertEqual(hw7.NumToTc(-1), '11111111')
        self.assertEqual(hw7.NumToTc(0), '00000000')
        self.assertEqual(hw7.NumToTc(1), '00000001')
        self.assertEqual(hw7.NumToTc(64), '01000000')
        self.assertEqual(hw7.NumToTc(126), '01111110')
        self.assertEqual(hw7.NumToTc(127), '01111111')
if __name__ == "__main__":
    unittest.main()
