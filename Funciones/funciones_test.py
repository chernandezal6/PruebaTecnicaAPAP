import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Funciones_global():
    def __init__(self, driver):
        self.driver = driver

    ERROR_MESSAGE = ("xpath", "//*[@id='flash-messages']")
    LOGIN_BUTTON = ("xpath", "(//font[contains(.,'Acceso')])[2]")

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    ## Abrimos pagina a navegar
    def Navegar(self, Url, Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Pagina login abierta: " + str(Url))
        t = time.sleep(Tiempo)
        return t

    ## funcion para validar texto, valores numericos
    def texto_xpath_valida(self, xpath, texto, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("xpath", xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element("xpath", xpath)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo el usuario {} ".format(texto))
            t = time.sleep(Tiempo)

            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento ==> " + xpath)
        ## funcion para validar texto, valores numericos

    def texto_xpath_valida(self, id, texto, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("xpath", xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element("id", id)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo el usuario {} ".format(texto))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento ==> " + id)

    ## Funcion Mouse Click
    def clic_xpath_valida(self, xpath, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("xpath", xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element("xpath", xpath)
            val.click()
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento ==> " + xpath)

    # Assertions
    def assert_login_success(self, t):
        """Verificar que el mensaje de éxito de inicio de sesión se muestre"""
        assert "You logged into a secure area!" in WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text


    def assert_login_failure(self, t):
        """Verificar que el mensaje de error de inicio de sesión se muestre"""
        assert "El usuario es invalido!" in WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text
        assert "El password es invalido!" in WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text


