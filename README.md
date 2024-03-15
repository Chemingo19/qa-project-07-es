# Proyecto 7 Cohorte. José López

... *Clave de ingreso: 150806*

    En el siguiente proyecto de este sprint N° 7, estaremos automatizando
    la pagina Urban Routes, donde haremos una solicitud de un taxi en modo
    personal. Seguido a ésto se va a seleecionar la tarifa Comfort, en la
    cual se agragaran un numero telefonico con su respectivo codigo de 
    seguridad, luego agregaremos una tarjeta de donde se debitara el monto
    a pagar por el servicio; dejaremos un mensaje al contralor, pediremos 
    una manta y pañuelos, luego dos helados. Una vez realizado todo esto, 
    se solicitara el taxi y esperaremos que aparezca en pantalla el tiempo
    de espera, con los detalles del vehiculo y del conductor.

    A continuación se detallará los archivos existentes:
    
    1.- Archivo main.py es de donde se ejecutará todo el proyecto. En el 
        cual se encuentran las siguientes pruebas:

        1.1- # Test para cargar la pagina, rellenar los campos Desde y Hasta
            "def test_set_route(self):"
        1.2- # Test para seleccionar el modo personal y darle click al boton Pedir 
                un Taxi "def test_type_journey(self):"
        1.3- # Test para seleccionar la tarifa Comfort y desplazarce hasta le 
            sección de agregar telefono "def test_tariff_picker_show(self):"
        1.4- # Test para agragar numero de telefono
             "def test_number_phone_and_code(self):"
        1.5- # Test para agragar nuevo medio de pago a traves de tarjeta
             "def test_add_new_card(self):"
        1.6- # Test para agragar un mensaje al contralor y bajar hasta la seccion 
            de escoger manta y pañuelo "def test_message_comptroller(self):"
        1.7- # Test para seccionar manta y pañuelos
             "def test_trigger_picker_blanket_and_scarves(self):"
        1.8- # Test para agragar helados "def test_add_ices_picker(self):"
        1.9- # Test para darle click en solicitar taxi y ver el tiempo de espera del 
            mismo "def test_order_taxi_and_modal(self):"

    2.- Archivo data.py desde aca se llamaran la mayoria de las variables 
        declaradas, sean url, conectores, lozalizadores, entre otros. 
    3.- Archivo urban_routes_page.py desde aca ingresaremos las diferentes
        direcciones a traves de sus funciones.
    4.- Archivo type_journey.py a traves de él se escoge el modo de viaje 
        y el tipo de trasladoa usar.
    5.- Archivo tariff_pickers_shown.py en el mismo escogeremos la tarifa del
        viaje, se hará el llamado al archivo para ingresar el numero telefonico
        con su respectivo mensaje de confirmación, también agregaremos el 
        metodo de pago de preferencia, un mensaje para el contralor, algún
        servicio adicional y/o aperitivos. Indicando el tiempo de espera y 
        datos del conductor.
    5.1- Archivo number_phone_and_code.py es donde ingresaremos el numero de
         telefono con su respectivo codigo de confirmación.
    5.2- Archivo add_new_card.py es donde seleccionamos el medio de pago, 
         datos del numero de tarjeta y su codigo de seguridad.

## TECNOLOGIAS UTILIZADAS:
    Git, GitHub, Pycharm para Python, Selenium.

## LIBREARIAS UTILIZADAS:
    webdriver, By, expected_conditions, WebDriverWait, time, Pytest. La mayoria
    ya vienen por defecto al instalar Selenium.

## INSTALACIONES NECESARIAS:
#   Selenium:
    Se debe seguir los siguientes pasos: 
    1.- Instalar los driver segun el navedaro con el que se vaya a utilizar del 
    siguiente link: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/
    2.- Selecciona la versión del controlador que coincida con tu versión de navegador.
    3.- Para averiguar tu versión de Chrome, abre el navegador. Pega chrome:
    //settings/help en la barra de direcciones y presiona Enter. Verás la versión 
    de tu navegador en la nueva ventana.
    4.- Descomprime el archivo. Crea una carpeta llamada WebDriver/bin y guarda 
    el archivo allí.
    5.- Agrega la ruta a bin a la variable de entorno PATH. El algoritmo depende 
    del sistema operativo.
    6.- Abre el Panel de Control.
    7.- Ve a Sistema → Configuración avanzada del sistema → Variables de entorno.
    8.- Busca y edita la variable PATH agregando la ruta completa hacia la carpeta 
    bin que acabas de crear. Debería ser algo como C:\\WebDriver\\bin.
    9.- Abrir la Consola o Terminal Terminal desde las aplicaciones o usando el
    buscador de aplicaciones.
    10.- Ejecutar el Comando de Instalación "pip instal selenium" (sin las "")
    11.- Verifica la instalación con el comando "pip freeze" (sin las "")

## Pytest: 
    La instalación se realiza a traves de: PyCharm en Python Packages o travaes de 
    la terminal usando el comando "pip install pytest" (sin las ""), a traves de él, 
    se podran validar las funciones de manera unitaria que posean la plabra test.

    Esto permite ejecutar todos los archivos del proyecto que empiecen con la palabra 
    test (en este caso en el archivo main.py). Una vez encontrado el archivo ejecutaremos  
    desdel el boton "run" en la parte superior o desde la terminal con el comando 
    "pytest TestUrbanRoutes".