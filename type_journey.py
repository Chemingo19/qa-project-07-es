import time

import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Clase para seleccionar el modo y tipo de viaje
class TypeJourney:
    modo_personal = (By.XPATH, data.mode_journey)
    type_vehicle = (By.XPATH, data.type_vehicle)
    button_type = (By.XPATH, data.button_taxi)

    def __init__(self, driver):
        self.driver = driver

#  Genera click en el modo de viaje Personal
    def click_set_personal(self):
        self.driver.find_element(*self.modo_personal).click()

# Genera Click en el tipo de vehiculo taxi
    def click_type_vehicle(self):
        self.driver.find_element(*self.type_vehicle).click()

# Genera click en el boton pedir taxi
    def click_button_type(self):
        self.driver.find_element(*self.button_type).click()

    def go_to_taxi(self):
        self.click_set_personal()
        self.click_type_vehicle()
        self.click_button_type()

# Realiza una espera a que cargue el modo de vehiculo personal
    def wait_for_load_type_journey(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.modo_personal))
