
import logging
from requests import Session
from requests.models import Response

from daikin_one_plus_api.const import INTEGRATION_ENDPOINT

_logger = logging.getLogger('daikin_one_plus_api.http.auth')
_endpoint = INTEGRATION_ENDPOINT + '/v1/token'

X_API_KEY_HEADER = 'x-api-key'

def login(email, apiKey, integratorToken):

    def throw(message):
        _logger.exception(message)
        raise Exception(message)

    def createSession(apiKey):
        session = Session()
        session.headers.update({'Content-Type' : 'application/json'})
        session.headers.update({X_API_KEY_HEADER : apiKey})
        return session
    
    def sendLoginRequest(session: Session, email, integratorToken):
        data = {
            "email" : email,
            "integratorToken" : integratorToken
        }

        return session.post(_endpoint, json=data)


    def updateSession(session: Session, response: Response):
        _logger.log(logging.INFO, "Login successfull")
        responseData = response.json()
        session.headers.update({'Authorization' : 'Bearer ' + responseData["accessToken"]})
        session.accessTokenExpiresIn = responseData["accessTokenExpiresIn"]
        return session

    
    session = createSession(apiKey)
    response = sendLoginRequest(session, email, integratorToken)

    errorMessage = 'Fail to authenticate to ' + _endpoint

    if response.status_code == 200:
        return updateSession(session, response)
    elif response.status_code == 401:
        throw(errorMessage + '. Unauthorized')
    elif response.status_code == 403:
        throw(errorMessage + '. Forbidden')
    else:
        throw(errorMessage)

    
    