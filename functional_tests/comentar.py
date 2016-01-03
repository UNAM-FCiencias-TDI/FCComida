# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def test_can_add_a_track(self):

        self.browser.get('http://localhost:8000/login')

        titlebox = self.browser.find_element_by_id('id_user')
        titlebox.send_keys('test')
        titlebox = self.browser.find_element_by_id('id_pass')
        titlebox.send_keys('12345')

        tracks_menu = self.browser.find_element_by_id('entrar')
        tracks_menu.send_keys(Keys.ENTER)

        self.browser.implicitly_wait(3)

        self.browser.get('http://localhost:8000/comercio/1/')

        titlebox = self.browser.find_element_by_name('comentario')
        titlebox.send_keys('bebed dijo el rey')

        tracks = self.browser.find_element_by_xpath('/html/body/article[2]/center/form[1]/button[1]')
        tracks.send_keys(Keys.ENTER)

if __name__ == '__main__':
    unittest.main()
