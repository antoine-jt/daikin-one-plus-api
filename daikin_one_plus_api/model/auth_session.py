import logging

from datetime import datetime, timedelta
from requests import Session
from requests.models import Response

from daikin_one_plus_api.http import auth

X_API_KEY_HEADER = 'x-api-key'

class AuthSession():
    _logger = logging.getLogger('daikin_one_plus_api.model.auth_session')
    _session: Session = None

    def __init__(self, email: str, apiKey: str, integratorToken: str):
        self._apiKey = apiKey
        self._email = email
        self._integratorToken = integratorToken


    def getSession(self):
        if self._session is None or self._isExpired():
            self._login()

        return self._session

    def _isExpired(self):
        return self._session.createdOn + timedelta(seconds=self._session.accessTokenExpiresIn) < datetime.utcnow()

    def _login(self):
        session = self.__createSession(self._apiKey)
        response = auth.login(session, self._email, self._integratorToken)

        if response.status_code == 200:
            self._logger.log(logging.INFO, "Login successfull")
            self._session = self.__updateSession(session, response)
        else:
            self.__handleError('Fail to login: ', response)


    def __createSession(self, apiKey):
        if(not self._session is None):
            self._session.close()
            self._session = None

        session = Session()
        session.headers.update({'Content-Type' : 'application/json'})
        session.headers.update({X_API_KEY_HEADER : apiKey})
        return session

    def __updateSession(self, session: Session, response: Response):
        responseData = response.json()
        session.headers.update({'Authorization' : 'Bearer ' + responseData["accessToken"]})
        session.accessTokenExpiresIn = responseData["accessTokenExpiresIn"]
        session.createdOn = datetime.utcnow()
        return session


    def __handleError(self, errorMessage: str, response: Response):
        if response.status_code == 401:
            self.__throw(errorMessage + 'Unauthorized')
        elif response.status_code == 403:
            self.__throw(errorMessage + 'Forbidden')
        else:
            self.__throw(errorMessage)

    def __throw(self, message):
        self._logger.exception(message)
        raise Exception(message)