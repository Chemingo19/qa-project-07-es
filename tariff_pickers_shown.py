import time
from number_phone_and_code import NumberPhoneAndCode
from add_new_card import AddNewCard
import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TariffPickerShown:
    tariff_car = (By.XPATH, data.button_comfort)
    taxi_id_messenger = (By.ID, data.id_messenger_taxi)
    view_label = (By.CLASS_NAME, data.label_view)
    manta = (By.CSS_SELECTOR, data.label_manta_panuelos)
    add_ice = (By.CSS_SELECTOR, data.css_ice)
    click_button_reservar = (By.CLASS_NAME, data.button_reservar)
    add_time_sleep = (By.CLASS_NAME, data.time_sleep)

    def __init__(self, driver):
        self.driver = driver

# Seleciona la tarifa Confort
    def select_tariff(self):
        self.driver.find_element(*self.tariff_car).click()
        time.sleep(1)

# Deslizar hasta la sección del ingreso del numero telefonico, metodo de pago y mensaje al conductor
    def view_zonal_of_date(self):
        element = self.driver.find_element(*self.taxi_id_messenger)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)

# Realiza llamado del archivo para agregar numero de telefono con su codigo de seguridad
    def call_file_number_phone_and_code(self):
        call_file_number_phone = NumberPhoneAndCode(self.driver)
        call_file_number_phone.add_phone_number()

# Realiza llamado del archivo para agregar nueva tarjeta
    def call_file_add_new_card(self):
        call_add_new_card = AddNewCard(self.driver)
        call_add_new_card.card_generate()

# Ingresar mensaje para el controlador
    def messenger_controlator(self):
        self.driver.find_element(*self.taxi_id_messenger).send_keys(data.message_for_driver)
        time.sleep(1)

# Deslizar hasta la sección del Requisitos del pedido
    def view_zonal_of_date_2(self):
        element = self.driver.find_element(*self.view_label)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)

# Genera click para seleccionar la opcion de requisitos y pedidos manta y pañuelos
    def req_picker_manta(self):
        self.driver.find_element(*self.manta).click()

# Seleccionar la cantidad de helados
    def add_ices_picker(self):
        number_clicks_add = self.driver.find_element(*self.add_ice)
        add_clicks = 2
        for number_clicks in range(add_clicks):
            number_clicks_add.click()
            time.sleep(1)

# Generar click en el boton para reservar un taxi despues de haber ingresado los datos requeridos
    def click_button_of_reservar(self):
        self.driver.find_element(*self.click_button_reservar).click()
        time.sleep(45)

# Agrupa todas las funciones para que sean llamado por el archivo principal main.py
    def order_completed(self):
        self.select_tariff()
        self.view_zonal_of_date()
        self.call_file_number_phone_and_code()
        self.call_file_add_new_card()
        self.messenger_controlator()
        self.view_zonal_of_date_2()
        self.req_picker_manta()
        self.add_ices_picker()
        self.click_button_of_reservar()

    def wait_for_tariff_pickers_shown(self):
        WebDriverWait(self.driver, 50).until(expected_conditions.visibility_of_element_located(self.add_time_sleep))