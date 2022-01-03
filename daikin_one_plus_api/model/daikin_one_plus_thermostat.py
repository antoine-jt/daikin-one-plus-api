class DaikinOnePlusThermostat():

    def __init__(self,
                 locationName,
                 id,
                 name,
                 model,
                 firmwareVersion,
                 coolSetpoint,
                 equipmentCommunication,
                 equipmentStatus,
                 fan,
                 fanCirculate,
                 fanCirculateSpeed,
                 heatSetpoint,
                 geofencingEnabled,
                 humIndoor,
                 humOutdoor,
                 mode,
                 modeEmHeatAvailable,
                 modeLimit,
                 scheduleEnabled,
                 setpointDelta,
                 setpointMaximum,
                 setpointMinimum,
                 tempIndoor,
                 tempOutdoor):

        self.locationName = locationName
        self.id = id
        self.name = name
        self.model = model
        self.firmwareVersion = firmwareVersion
        self.coolSetpoint = coolSetpoint
        self.equipmentCommunication = equipmentCommunication
        self.equipmentStatus = equipmentStatus
        self.fan = fan
        self.fanCirculate = fanCirculate
        self.fanCirculateSpeed = fanCirculateSpeed
        self.heatSetpoint = heatSetpoint
        self.geofencingEnabled = geofencingEnabled
        self.humIndoor = humIndoor
        self.humOutdoor = humOutdoor
        self.mode = mode
        self.modeEmHeatAvailable = modeEmHeatAvailable
        self.modeLimit = modeLimit
        self.scheduleEnabled = scheduleEnabled
        self.setpointDelta = setpointDelta
        self.setpointMaximum = setpointMaximum
        self.setpointMinimum = setpointMinimum
        self.tempIndoor = tempIndoor
        self.tempOutdoor = tempOutdoor
