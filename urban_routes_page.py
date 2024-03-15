from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # VARIABLES PARA ARCHIVO type_jorney.py
    mode_journey = (By.XPATH, '//div[@class="mode" and text()="Personal"]')
    type_vehicle = (By.CSS_SELECTOR, 'img[src="/static/media/taxi-active.b0be3054.svg"]')
    button_taxi = (By.XPATH, '//button[@class="button round"]')

    # Localizadores del archivo tariff_pickers_shown.py
    button_comfort = (By.XPATH, '//div[@class="tcard"]/div[@class="tcard-title" and text()="Comfort"]')
    id_messenger_taxi = (By.ID, 'comment')
    label_view = (By.CLASS_NAME, 'r-sw-label')
    label_blanket_and_scarves = (By.CSS_SELECTOR, '.slider')
    label_blanket_and_scarves_ = (By.XPATH, '//div[@class="r-sw-label" and text()="Manta y pañuelos"]')
    css_ice = (By.CSS_SELECTOR, '.counter-plus')
    check_css_ice = (By.XPATH, '//div[@class="counter-value" and text()=2]')
    button_reserver = (By.CLASS_NAME, 'smart-button-main')
    wait_order = (By.XPATH, '//div[@class="order-btn-rating"]')


    # Lozalizadores del archibo number_and_code.py
    phone_camp = (By.CLASS_NAME, 'np-text')
    id_phone = (By.ID, 'phone')
    button_next = (By.XPATH, '//button[@type="submit" and @class="button full" and text()="Siguiente"]')
    id_code_phone_number = (By.ID, 'code')
    button_confirmation = (By.XPATH, '//button[@type="submit" and @class="button full" and text()="Confirmar"]')

    # Localizadores del archivo add_new_card.py
    payment_methodo = (By.CLASS_NAME, 'pp-text')
    card_name = (By.CLASS_NAME, 'pp-value-text')
    add_card = (By. XPATH, '//div[@class="pp-title" and text()="Agregar tarjeta"]')
    id_number_card = (By.ID, 'number')
    card_code = (By.XPATH, '//div[@class="card-code-input"]/input[@name="code"]')
    click_plc = (By.CLASS_NAME, 'plc')
    button_add_card = (By.XPATH, '//button[@class="button full" and text()="Agregar"]')
    button_closed = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')

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

