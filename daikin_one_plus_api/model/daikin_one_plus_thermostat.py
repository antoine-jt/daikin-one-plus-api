class DaikinOnePlusThermostat():

    def __init__(self, id, name, model, firmwareVersion):
        self.id = id
        self.name = name
        self.model = model
        self.firmwareVersion = firmwareVersion

    @property
    def id(self) -> str:
        return self.id

    @property
    def name(self) -> str:
        return self.name

    @property
    def model(self) -> str:
        return self.model

    @property
    def firmwareVersion(self) -> str:
        return self.firmwareVersion

