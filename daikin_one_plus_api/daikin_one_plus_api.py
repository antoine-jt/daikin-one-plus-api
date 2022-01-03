import logging

from requests.models import Response

from daikin_one_plus_api.http import device
from daikin_one_plus_api.model.auth_session import AuthSession
from daikin_one_plus_api.model.daikin_one_plus_thermostat import DaikinOnePlusThermostat

class DaikinOnePlusApi():

    _logger = logging.getLogger('daikin_one_plus_api.daikin_one_api')

    def __init__(self, email, apiKey, integratorToken):
        self._authSession = AuthSession(email, apiKey, integratorToken)

    def getDevices(self):
        locations = device.getAll(self._authSession.getSession()).json()
        devices = []
        for location in locations:
            for jsonDevice in location['devices']:
                deviceConfig = self.__getDeviceConfig(jsonDevice['id'])
                devices.append(DaikinOnePlusThermostat(location['locationName'], **jsonDevice, **deviceConfig))
        return devices


    def __getDeviceConfig(self, id: str):
        response: Response = device.get(self._authSession.getSession(), id)

        if response.status_code != 200:
            self.__throw("Unable to fetch device data")

        return response.json()

    def __throw(self, message):
        self._logger.exception(message)
        raise Exception(message)
