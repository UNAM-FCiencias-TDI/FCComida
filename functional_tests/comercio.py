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

        self.browser.get('http://localhost:8000/comercio-registro/')

        titlebox = self.browser.find_element_by_id('id_nombre')
        titlebox.send_keys('el rey')
        titlebox = self.browser.find_element_by_id('id_mayor_precio')
        titlebox.clear()
        titlebox.send_keys('1.0')
        titlebox = self.browser.find_element_by_id('id_menor_precio')
        titlebox.clear()
        titlebox.send_keys('200.0')
        titlebox = self.browser.find_element_by_id('id_descripcion')
        titlebox.send_keys('Beban y olvidense de su necesidaad, y de su miseria no se acuerden mas')

        titlebox = self.browser.find_element_by_id('id_latitud')
        titlebox.clear()
        titlebox.send_keys('19.3249963')
        titlebox = self.browser.find_element_by_id('id_longitud')
        titlebox.clear()
        titlebox.send_keys('-99.1732381')

        placebox = self.browser.find_element_by_id('id_facultad')
        placebox.send_keys('Facultad de Ciencias')
        placebox.send_keys(Keys.ENTER)

        tracks = self.browser.find_element_by_id('aceptar')
        tracks.send_keys(Keys.ENTER)

if __name__ == '__main__':
    unittest.main()
