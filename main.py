import data
from selenium import webdriver
from tariff_pickers_shown import TariffPickerShown
from urban_routes_page import UrbanRoutesPage
from type_journey import TypeJourney
from number_phone_and_code import NumberPhoneAndCode
from add_new_card import AddNewCard


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

# Test para cargar la pagina, rellenar los campos Desde y Hasta
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.wait_for_load_home_page()
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

# Test para seleccionar el modo personal y darle click al boton Pedir un Taxi
    def test_type_journey(self):
        type_journey = TypeJourney(self.driver)
        transport_mode = type_journey.check_trigger_click_personal()
        button_taxi = type_journey.check_trigger_click_button_type_taxi()
        type_journey.trigger_click_set_personal()
        type_journey.trigger_click_type_vehicle()
        type_journey.wait_for_load_type_journey()
        type_journey.trigger_click_button_type_taxi()
        assert transport_mode == 'Personal'
        assert button_taxi == 'Pedir un taxi'

# Test para seleccionar la tarifa Comfort y
    # desplazarce hasta le sección de agregar telefono
    def test_tariff_picker_show(self):
        tariff_pickers = TariffPickerShown(self.driver)
        select_tariff = tariff_pickers.check_select_tariff()
        tariff_pickers.wait_select_tariff()
        tariff_pickers.select_tariff()
        tariff_pickers.slide_view_zonal_of_date()
        assert select_tariff == 'Comfort'

# Test para agragar numero de telefono
    def test_number_phone_and_code(self):
        number_phone = NumberPhoneAndCode(self.driver)
        phone_number = data.phone_number
        number_phone.select_phone_camp()
        number_phone.add_phone_number_in_form()
        number_phone.trigger_button_next_add_phone()
        number_phone.add_code_confirmation()
        number_phone.trigger_click_button_code_confirmation()
        assert number_phone.check_number_in_form() == phone_number

# Test para agragar nuevo medio de pago a traves de tarjeta
    def test_add_new_card(self):
        new_card = AddNewCard(self.driver)
        new_card.trigger_click_payment_method_add_to_card()
        new_card.trigger_click_add_new_card()
        new_card.add_number_card_in_form()
        new_card.add_code_number_car_in_form()
        new_card.trigger_click_activate_button_add_card()
        new_card.trigger_click_button_add_card_in_form()
        new_card.trigger_closed_form_add_card()
        card_name = new_card.check_add_number_card_in_form()
        assert card_name == 'Tarjeta'

# Test para agragar un mensaje al contralor y
    # bajar hasta la seccion de escoger manta y pañuelo
    def test_message_comptroller(self):
        tariff_pickers = TariffPickerShown(self.driver)
        message_for_driver = data.message_for_driver
        tariff_pickers.add_messenger_comptroller()
        tariff_pickers.slide_view_zonal_of_date()
        tariff_pickers.wait_add_messenger_comptroller()
        assert tariff_pickers.check_messenger_comptroller() == message_for_driver

# Test para seccionar manta y pañuelos
    def test_trigger_picker_blanket_and_scarves(self):
        tariff_pickers = TariffPickerShown(self.driver)
        tariff_pickers.trigger_picker_blanket_and_scarves()
        blanket_and_scarves = tariff_pickers.check_trigger_picker_blanket_and_scarves()
        assert blanket_and_scarves == 'Manta y pañuelos'

# Test para agragar helados
    def test_add_ices_picker(self):
        tariff_pickers = TariffPickerShown(self.driver)
        tariff_pickers.add_ices_picker()
        add_ices = tariff_pickers.check_add_ices_picker()
        assert add_ices == '2'

# Test para darle click en solicitar taxi y ver el tiempo de espera del mismo
    def test_order_taxi_and_modal(self):
        tariff_pickers = TariffPickerShown(self.driver)
        wait_modal= UrbanRoutesPage.wait_order
        tariff_pickers.trigger_click_button_of_reserver()
        tariff_pickers.wait_messenger_modal()
        assert tariff_pickers.wait_order == wait_modal

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
