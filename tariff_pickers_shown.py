import data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urban_routes_page import UrbanRoutesPage


class TariffPickerShown:
    tariff_car = UrbanRoutesPage.button_comfort
    taxi_id_messenger = UrbanRoutesPage.id_messenger_taxi
    view_label = UrbanRoutesPage.label_view
    card_name = UrbanRoutesPage.card_name
    blanket_and_scarves = UrbanRoutesPage.label_blanket_and_scarves
    blanket_and_scarves_ = UrbanRoutesPage.label_blanket_and_scarves_
    add_ice = UrbanRoutesPage.css_ice
    check_css_ice = UrbanRoutesPage.check_css_ice
    click_button_reserver = UrbanRoutesPage.button_reserver
    wait_order = UrbanRoutesPage.wait_order

    def __init__(self, driver):
        self.driver = driver

# Seleciona la tarifa Confort
    def select_tariff(self):
        self.driver.find_element(*self.tariff_car).click()

# Verifica que la tarifa seleccionada sea la correcta
    def check_select_tariff(self):
        return self.driver.find_element(*self.tariff_car).text

# Espera a que se muestre mensaje en el modal
    def wait_select_tariff(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(self.tariff_car))

    # Deslizar hasta la sección del ingreso del numero telefonico, metodo de pago y mensaje al conductor
    def slide_view_zonal_of_date(self):
        element = self.driver.find_element(*self.taxi_id_messenger)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

# Ingresar mensaje para el controlador
    def add_messenger_comptroller(self):
        self.driver.find_element(*self.taxi_id_messenger).send_keys(data.message_for_driver)

# Verifica el mensaje enviado al contralor
    def check_messenger_comptroller(self):
        return self.driver.find_element(*self.taxi_id_messenger).get_property('value')

# Espera a que se muestre mensaje en el contralor
    def wait_add_messenger_comptroller(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.taxi_id_messenger))

# Deslizar hasta la sección del Requisitos del pedido
    def slide_view_zonal_of_date_2(self):
        element = self.driver.find_element(*self.view_label)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

# Genera click para seleccionar la opcion de requisitos y pedidos manta y pañuelos
    def trigger_picker_blanket_and_scarves(self):
        self.driver.find_element(*self.blanket_and_scarves).click()

# Verifica que se haya escogido la manta y pañuelo
    def check_trigger_picker_blanket_and_scarves(self):
        return self.driver.find_element(*self.blanket_and_scarves_).text

    # Seleccionar la cantidad de helados
    def add_ices_picker(self):
        number_clicks_add = self.driver.find_element(*self.add_ice)
        add_clicks = 2
        for number_clicks in range(add_clicks):
            number_clicks_add.click()

# Verifica que se haya escogido la manta y pañuelo
    def check_add_ices_picker(self):
        return self.driver.find_element(*self.check_css_ice).text

# Generar click en el boton para reservar un taxi despues de haber ingresado los datos requeridos
    def trigger_click_button_of_reserver(self):
        self.driver.find_element(*self.click_button_reserver).click()

# Espera a que se muestre mensaje en el modal
    def wait_messenger_modal(self):
        WebDriverWait(self.driver, 35).until(expected_conditions.visibility_of_element_located(self.wait_order))
