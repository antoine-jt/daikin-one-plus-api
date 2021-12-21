import logging

from daikin_one_plus_api.http import device
from daikin_one_plus_api.model.auth_session import AuthSession

class DaikinOnePlusApi():

    _logger = logging.getLogger('daikin_one_plus_api.daikin_one_api')

    def __init__(self, email, apiKey, integratorToken):
        self._authSession = AuthSession(email, apiKey, integratorToken)

    def getDevices(self):
        return device.getAll(self._authSession.getSession())

    def getDevice(self, id: str):
        return device.get(self._authSession.getSession(), id)
