def getKey(kwargs, key, defaultVal=None):
    return defaultVal if key not in kwargs else kwargs[key]

def convertToOptionList(key, val):
    return [ f'{key}={val}' ] if val != None else []

def isVector(val):
    return False if type(val) != list or len(val) != 3 else True

def getDiameterKey(kwargs, key, defaultRadius):
    return defaultRadius if key not in kwargs else kwargs[key] / 2
