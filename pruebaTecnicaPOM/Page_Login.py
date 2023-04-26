import time
import unittest
import json
import os.path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Funciones.funciones_test import Funciones_global

t = 2

class Page_Login():

    def __init__(self, driver):
        self.driver = driver

    def Login_master(self, t):
        driver = self.driver
        f = Funciones_global(driver)
        f.Navegar("https://the-internet.herokuapp.com/login", 3)
       # path = os.path.abspath("../userpass.json")
        #with open(path, "r") as fp:
        #    obj = json.load(fp)
            #f.texto_xpath_valida("//*[@id='username']", obj['username'], t)
        f.texto_xpath_valida("//*[@id='username']", "tomsmith", t)
        f.texto_xpath_valida("//input[@id='password']","SuperSecretPassword!", t)
        f.clic_xpath_valida("//button[@class='radius']", t)
        f.assert_login_success(t)
        f.clic_xpath_valida("//a[@href='/logout']", t)



    def test_login_invalid_credentials(self, t):
     #   """Verificar que se muestre un mensaje de error al iniciar sesión con credenciales inválidas"""
        driver = self.driver
        self.Login_master(t)
        er = Funciones_global(driver)
        er.texto_xpath_valida("bobo", "macaranera", t )
        er.assert_login_failure(t)


