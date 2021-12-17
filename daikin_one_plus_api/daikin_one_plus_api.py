import logging

from requests.sessions import Session
from daikin_one_plus_api.http import auth

class DaikinOnePlusApi():

    _logger = logging.getLogger('daikin_one_plus_api.daikin_one_api')
    _session: Session = None;

    def __init__(self, email, apiKey, integratorToken):
        self._email = email
        self._apiKey = apiKey
        self._integratorToken = integratorToken

    
    def __throw(self, message):
        self._logger.exception(message)
        raise Exception(message)

    def __validateSession(self, session: Session):
        if session is None:
            self.__throw('Invalid session. You must login before interracting with the api')

    def login(self):
        self._session = auth.login(self._email, self._apiKey, self._integratorToken)


    def getDevices(self):
        self.__validateSession(self._session);
        return []
