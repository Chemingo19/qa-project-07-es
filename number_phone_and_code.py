from selenium.webdriver.common.by import By
import data
import main


class NumberPhoneAndCode:
    click_phone_camp = (By.CLASS_NAME, data.phone_camp)
    click_id_phone = (By.ID, data.id_phone)
    click_button_next = (By.XPATH, data.button_next)
    add_code = (By.ID, data.id_code_phone_number)
    click_button_confirmation = (By.XPATH, data.button_confirmation)

    def __init__(self, driver):
        self.driver = driver

# Seleciona el campo ingresar telefono
    def select_phone_camp(self):
        self.driver.find_element(*self.click_phone_camp).click()

# Agregar el numero telefonico
    def add_phone_number_in_form(self):
        add_phone = data.phone_number
        self.driver.find_element(*self.click_id_phone).send_keys(add_phone)

# Genera click en el boton siguiente del formulario agragar telefono
    def button_next_add_phone(self):
        self.driver.find_element(*self.click_button_next).click()

# Ingresa el codigo de confirmación del numero telefonico
    def code_confirmation(self):
        code_phone = main.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.add_code).send_keys(code_phone)

# Genera click en el boton confirmar despues de ingresar el codigo de confirmación
    def click_button_code_confirmation(self):
        self.driver.find_element(*self.click_button_confirmation).click()

# Agrupa todas las funciones del archivo y sean llamadas por el archivo tariff_pickers_shown.py
    def add_phone_number(self):
        self.select_phone_camp()
        self.add_phone_number_in_form()
        self.button_next_add_phone()
        self.code_confirmation()
        self.click_button_code_confirmation()