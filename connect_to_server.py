import requests
import json
from exceptions import CantGetJsonFromServer
from set_logger_settings import *

py_logger.debug(f"Loading module {__name__}...")


def srv_request(payload, headers: dict = {'content-type': 'application/json'}) -> dict:
    url = f'{config.SERVER_URL}:{config.SERVER_PORT}{config.SERVER_URI}'
    response = requests.get(url, params=payload, headers=headers)
    if response.status_code == requests.codes.ok:
        try:
            response = response.json()
        except json.decoder.JSONDecodeError:
            if __name__ == '__main__':
                exit(f"Error: Received data not in JSON format when requested: {payload}")

            py_logger.exception(f"Error: Received data not in JSON format when requested:  {payload}")
            raise CantGetJsonFromServer

        if response['result'].upper() == 'OK':
            return response['data']
        else:
            if __name__ == '__main__':
                exit(f"Error: Server return error: {response['error']}")

            py_logger.exception(f"Error: Server return error: {response['error']}")
            raise CantGetJsonFromServer


# for test this class:
if __name__ == '__main__':
    print(
        f"JSON: {srv_request({'city': 'EKB1', 'name': 'badd1c9b49801ac57e7edc3e0a359a3e', 'mac': '65336ffbf765ee244fff277a7f6f31be'})}")
