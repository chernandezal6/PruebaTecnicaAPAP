import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Iniciar el navegador Chrome
driver = webdriver.Chrome()

# Abrir la página de entrada numérica
driver.get("https://the-internet.herokuapp.com/inputs")

# Buscar el campo de entrada numérica
numero_input = driver.find_element("xpath", "//input[contains(@type,'number')]")


# Insertar un valor numérico en el campo
numero_input.send_keys("1234")
time.sleep(3)

# Obtener el valor actual del campo de entrada numérica
valor_actual = numero_input.get_attribute("value")

# Incrementar el valor del campo de entrada numérica utilizando la tecla de flecha hacia arriba
numero_input.send_keys(Keys.ARROW_UP)
time.sleep(3)

# Esperar a que el valor se actualice y obtener el nuevo valor del campo de entrada numérica
driver.implicitly_wait(10)
Nuevo_valor = numero_input.get_attribute("value")

time.sleep(3)
# Verificar que el valor se ha incrementado en 1
assert int(Nuevo_valor) == int(valor_actual) + 1

# Decrementar el valor del campo de entrada numérica utilizando la tecla de flecha hacia abajo
numero_input.send_keys(Keys.ARROW_DOWN)

# Esperamos 10 seg para que el valor se actualice y nos muestre el nuevo valor del campo de entrada numérica
driver.implicitly_wait(10)
Nuevo_valor = numero_input.get_attribute("value")
time.sleep(3)

# Verificar que el valor se ha decrementado en 1
assert int(Nuevo_valor) == int(valor_actual)

# Cerrar el navegador
driver.quit()
