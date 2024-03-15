import data
from helpers import retrieve_phone_code
from urban_routes_page import UrbanRoutesPage


class NumberPhoneAndCode:
    click_phone_camp = UrbanRoutesPage.phone_camp
    click_id_phone = UrbanRoutesPage.id_phone
    click_button_next = UrbanRoutesPage.button_next
    add_code = UrbanRoutesPage.id_code_phone_number
    click_button_confirmation = UrbanRoutesPage.button_confirmation

    def __init__(self, driver):
        self.driver = driver

# Seleciona el campo ingresar telefono
    def select_phone_camp(self):
        self.driver.find_element(*self.click_phone_camp).click()

# Agregar el numero telefonico
    def add_phone_number_in_form(self):
        add_phone = data.phone_number
        self.driver.find_element(*self.click_id_phone).send_keys(add_phone)

# Verifica cual fue el numero de telefono ingresado
    def check_number_in_form(self):
        return self.driver.find_element(*self.click_id_phone).get_property('value')

# Genera click en el boton siguiente del formulario agragar telefono
    def trigger_button_next_add_phone(self):
        self.driver.find_element(*self.click_button_next).click()

# Ingresa el codigo de confirmación del numero telefonico
    def add_code_confirmation(self):
        code_phone = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.add_code).send_keys(code_phone)

# Genera click en el boton confirmar despues de ingresar el codigo de confirmación
    def trigger_click_button_code_confirmation(self):
        self.driver.find_element(*self.click_button_confirmation).click()
