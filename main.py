import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from Funciones.funciones_test import Funciones_global
from Funciones.Page_factorial import Page_factorial
from pruebaTecnicaAPAP.Page_Login import Page_Login


tg = 2

class base_test(unittest.TestCase):

    def setUp(self):
        self.service = Service(executable_path="/path/to/chromedriver")
        self.driver = webdriver.Chrome(service=self.service)

    def test1(self):
        driver = self.driver
        f = Funciones_global(driver) ## inicializamos la funcion
        pg = Page_Login(driver)
        pg.Login_master(tg)


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()