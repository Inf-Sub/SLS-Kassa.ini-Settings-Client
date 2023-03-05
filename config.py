import os
from datetime import datetime


max_number_len = 2
date = str(datetime.now().date())
year = datetime.today().year
month = f'{datetime.today().month:0{max_number_len}}'
day = f'{datetime.today().day:0{max_number_len}}'
script_path = os.path.dirname(os.path.realpath(__file__))


# info / debug / or empty
LOGGER_LEVEL = 'debug'
LOGGER_DIR = f'{script_path}/Logs/{year}/{month}/{day}'
LOGGER_FILE = f'{LOGGER_DIR}/Logs_{date}'
LOGGER_FORMAT = '%(name)s\t%(asctime)s\t%(levelname)s\t%(message)s'

SLSKASSA_CONFIG = r'c:\SoftLand Systems\SLS-Kacca\Kassa_W.INI'

SERVER_URL = 'http://SLS.TkYD.ru'
SERVER_PORT = 80
SERVER_URI = '/kassa/settings'


