import data
import main
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver

# Ingresa la dirección en el campo Desde
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    # Ingresa la dirección en el campo Hasta
    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

# Busca el punto de partida en el mapa
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

# Busca el punto de llegada
    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

# Agrupa las funciones y puedan ser llamadas desde el archivo main.py
    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.to_field))

