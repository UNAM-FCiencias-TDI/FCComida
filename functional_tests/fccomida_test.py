# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

if __name__ == '__main__':
    unittest.main()
