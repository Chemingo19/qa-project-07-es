from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urban_routes_page import UrbanRoutesPage


# Clase para seleccionar el modo y tipo de viaje
class TypeJourney:
    mode_personal = UrbanRoutesPage.mode_journey
    type_vehicle = UrbanRoutesPage.type_vehicle
    button_type = UrbanRoutesPage.button_taxi

    def __init__(self, driver):
        self.driver = driver

#  Genera click en el modo de viaje Personal
    def trigger_click_set_personal(self):
        self.driver.find_element(*self.mode_personal).click()

# Verifica el texto del modo de viaje a seleccionar
    def check_trigger_click_personal(self):
        return self.driver.find_element(*self.mode_personal).text

# Realiza una espera a que cargue el modo de vehiculo personal
    def wait_for_load_button_type_taxi(self):
            WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.button_type))

    # Genera Click en el tipo de vehiculo taxi
    def trigger_click_type_vehicle(self):
        self.driver.find_element(*self.type_vehicle).click()

# Genera click en el boton pedir taxi
    def trigger_click_button_type_taxi(self):
        self.driver.find_element(*self.button_type).click()

# Verifica el texto del boton para pedir un taxi
    def check_trigger_click_button_type_taxi(self):
        return self.driver.find_element(*self.button_type).text

# Realiza una espera a que cargue el modo de vehiculo personal
    def wait_for_load_type_journey(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.button_type))
