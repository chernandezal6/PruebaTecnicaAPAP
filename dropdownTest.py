import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Iniciar el navegador Chrome
driver = webdriver.Chrome()

# Abrir la página de dropdown
driver.get("https://the-internet.herokuapp.com/dropdown")

# Encontrar el elemento select y crear un objeto Select
select_element = driver.find_element("id", "dropdown")
dropdown = Select(select_element)

# Seleccionar la opción "Option 1"
dropdown.select_by_value("1")
time.sleep(3)

# Verificar que se haya seleccionado la opción correcta
assert dropdown.first_selected_option.text == "Option 1"

# Seleccionar la opción "Option 2"
dropdown.select_by_value("2")

# Verificar que se haya seleccionado la opción correcta
assert dropdown.first_selected_option.text == "Option 2"

# Cerrar el navegador
driver.quit()