import logging

from requests import Session

from daikin_one_plus_api.const import INTEGRATION_ENDPOINT

_endpoint = INTEGRATION_ENDPOINT + '/v1/token'

def login(session: Session, email: str, integratorToken: str):
    data = {
        "email" : email,
        "integratorToken" : integratorToken
    }

    return session.post(_endpoint, json=data)

    
    