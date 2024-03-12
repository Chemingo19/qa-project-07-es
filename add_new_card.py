from selenium.webdriver.common.by import By
import data


class AddNewCard:
    click_payment_methodo = (By.CLASS_NAME, data.payment_methodo)
    click_add_card = (By.XPATH, data.add_card)
    add_number_card = (By.ID, data.id_number_card)
    add_code_number_card = (By.XPATH, data.id_card_code)
    click_plc = (By.CLASS_NAME, data.click_plc)
    click_button_add_card = (By.XPATH, data.button_add_card)
    click_button_closed = (By.XPATH, data.button_closed)

    def __init__(self, driver):
        self.driver = driver

    # Genera click en el campo Metodo de pago
    def click_payment_methodo_add_to_card(self):
        self.driver.find_element(*self.click_payment_methodo).click()

    # Genera click en el campo Agregar tarjeta
    def click_add_new_card(self):
        self.driver.find_element(*self.click_add_card).click()

    # Agregar el numero de tarjeta en el formulario
    def add_number_card_in_form(self):
        add_card_in_form = data.card_number
        self.driver.find_element(*self.add_number_card).send_keys(add_card_in_form)

    # Agregar el codigo de tarjeta en el formulario
    def add_code_number_car_in_form(self):
        add_code_card = data.card_code
        self.driver.find_element(*self.add_code_number_card).send_keys(add_code_card)

    # Generar click para activar boton de agregar tarjeta
    def click_plc_form(self):
        self.driver.find_element(*self.click_plc).click()

    # Click en el boton agragar tarjeta
    def click_button_add_card_in_form(self):
        self.driver.find_element(*self.click_button_add_card).click()

    # Cerrar formulario una vez tarjeta agregada
    def closed_form_add_card(self):
        self.driver.find_element(*self.click_button_closed).click()

    # Agrupa todas las funciones para que sean llamadas por el archivo tariff_pickers_shown.py
    def card_generate(self):
        self.click_payment_methodo_add_to_card()
        self.click_add_new_card()
        self.add_number_card_in_form()
        self.add_code_number_car_in_form()
        self.click_plc_form()
        self.click_button_add_card_in_form()
        self.closed_form_add_card()
