import data
from urban_routes_page import UrbanRoutesPage


class AddNewCard:
    click_payment_method = UrbanRoutesPage.payment_methodo
    click_add_card = UrbanRoutesPage.add_card
    card_name = UrbanRoutesPage.card_name
    add_number_card = UrbanRoutesPage.id_number_card
    add_code_number_card = UrbanRoutesPage.card_code
    click_plc = UrbanRoutesPage.click_plc
    click_button_add_card = UrbanRoutesPage.button_add_card
    click_button_closed = UrbanRoutesPage.button_closed

    def __init__(self, driver):
        self.driver = driver

# Genera click en el campo Metodo de pago
    def trigger_click_payment_method_add_to_card(self):
        self.driver.find_element(*self.click_payment_method).click()

 # Genera click en el campo Agregar tarjeta
    def trigger_click_add_new_card(self):
        self.driver.find_element(*self.click_add_card).click()

# Agregar el numero de tarjeta en el formulario
    def add_number_card_in_form(self):
        add_card_in_form = data.card_number
        self.driver.find_element(*self.add_number_card).send_keys(add_card_in_form)

# Verifica que se haya agragado el metodo de pago correcto
    def check_add_number_card_in_form(self):
        return self.driver.find_element(*self.card_name).text

# Agregar el codigo de tarjeta en el formulario
    def add_code_number_car_in_form(self):
        add_code_card = data.card_code
        self.driver.find_element(*self.add_code_number_card).send_keys(add_code_card)

# Generar click para activar boton de agregar tarjeta
    def trigger_click_activate_button_add_card(self):
        self.driver.find_element(*self.click_plc).click()

# Click en el boton agragar tarjeta
    def trigger_click_button_add_card_in_form(self):
        self.driver.find_element(*self.click_button_add_card).click()

# Cerrar formulario una vez tarjeta agregada
    def trigger_closed_form_add_card(self):
        self.driver.find_element(*self.click_button_closed).click()

