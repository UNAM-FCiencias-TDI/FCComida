# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def test_can_add_a_track(self):
        # Alicia visita la aplciación
        self.browser.get('http://localhost:8000')
        self.assertIn('Hola-FCComida', self.browser.title)

if __name__ == '__main__':
    unittest.main()
