from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Iniciar el navegador Chrome
driver = webdriver.Chrome()

# Abrir la página de hovers
driver.get("https://the-internet.herokuapp.com/hovers")

# Encontrar las imágenes de usuario
user1 = driver.find_element("xpath", "//div[@class='example']//div[1]//img")
user2 = driver.find_element("xpath", "//div[@class='example']//div[2]//img")
user3 = driver.find_element("xpath", "//div[@class='example']//div[3]//img")

# Crear una acción de mouse en la imagen del primer usuario
hover = ActionChains(driver).move_to_element(user1)

# Ejecutar la acción de mouse
hover.perform()

# Verificar si se muestra el texto de información del usuario
assert driver.find_element("xpath","//div[@class='example']//div[1]//div").is_displayed()

# Crear una acción de mouse en la imagen del segundo usuario
hover = ActionChains(driver).move_to_element(user2)

# Ejecutar la acción de mouse
hover.perform()

# Verificar si se muestra el texto de información del usuario
assert driver.find_element("xpath","//div[@class='example']//div[2]//div").is_displayed()

# Crear una acción de mouse en la imagen del tercer usuario
hover = ActionChains(driver).move_to_element(user3)

# Ejecutar la acción de mouse
hover.perform()

# Verificar si se muestra el texto de información del usuario
assert driver.find_element("xpath","//div[@class='example']//div[3]//div").is_displayed()

# Cerrar el navegador
driver.quit()