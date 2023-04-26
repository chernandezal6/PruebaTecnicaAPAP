import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Iniciar el navegador Chrome
driver = webdriver.Chrome()

# Abrir la página de inicio de sesión
driver.get("https://the-internet.herokuapp.com/login")

# Encontrar los campos de entrada de usuario y contraseña
username_input = driver.find_element("id", "username")
password_input = driver.find_element("id", "password")

# Ingresar el nombre de usuario y la contraseña en los campos correspondientes
username_input.send_keys("tomsmith")
password_input.send_keys("SuperSecretPassword!")
time.sleep(2)

# Enviar el formulario de inicio de sesión
password_input.send_keys(Keys.ENTER)
time.sleep(2)

# Esperar a que se cargue la página de inicio de sesión
driver.implicitly_wait(10)

# Verificar que se ha iniciado sesión correctamente
assert "secure" in driver.current_url

# Cerrar el navegador
driver.quit()