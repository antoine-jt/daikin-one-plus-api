from requests.sessions import Session

from daikin_one_plus_api.model.fan_circulated import FanCirculated
from daikin_one_plus_api.model.fan_circulated_speed import FanCirculatedSpeed
from daikin_one_plus_api.model.thermostat_mode import ThermostatMode

from daikin_one_plus_api.const import INTEGRATION_ENDPOINT

_endpoint = INTEGRATION_ENDPOINT + '/v1/devices'


def getAll(session: Session):
    return session.get(_endpoint)


def get(session: Session, id: str):
    return session.get(_endpoint + '/' + id)


def updateMode(session: Session, mode: ThermostatMode, heatSetpoint: float, coolSetpoint: int):
    url = _endpoint + '/' + id + '/msp'
    data = {
            'mode' : mode,
            'heatSetpoint' : heatSetpoint,
            'coolSetpoint': coolSetpoint
        }
    
    return session.put(url, data=data)


def enableSchedule(session: Session, enabled: bool):
    data = {
        'scheduleEnabled': enabled
    }

    return session.put(_endpoint + '/' + id + '/schedule', data=data)


def updateFan(session: Session, fanCirculate: FanCirculated, fanCirculateSpeed: FanCirculatedSpeed):
    url = _endpoint + '/' + id + '/msp'
    data = {
            'fanCirculate' : fanCirculate,
            'fanCirculateSpeed' : fanCirculateSpeed
        }
    
    return session.put(url, data=data)