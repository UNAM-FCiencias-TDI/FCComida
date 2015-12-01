# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def test_can_add_a_track(self):
        self.browser.get('http://localhost:8000/register')

        titlebox = self.browser.find_element_by_id('id_username')
        titlebox.send_keys('test')
        titlebox = self.browser.find_element_by_id('id_password')
        titlebox.send_keys('12345')
        titlebox = self.browser.find_element_by_id('id_password2')
        titlebox.send_keys('12345')
        titlebox = self.browser.find_element_by_id('id_email')
        titlebox.send_keys('test@mail.com')

        placebox = self.browser.find_element_by_id('id_facultad')
        placebox.send_keys('Facultad de Arquitectura')
        placebox.send_keys(Keys.ENTER)

        tracks_menu = self.browser.find_element_by_id('registrar')
        tracks_menu.send_keys(Keys.ENTER)

if __name__ == '__main__':
    unittest.main()
