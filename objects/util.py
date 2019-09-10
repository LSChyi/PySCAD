def getKey(kwargs, key, defaultVal=None):
    return defaultVal if key not in kwargs else kwargs[key]

def convertToOptionList(key, val):
    return [ f'{key}={val}' ] if val != None else []

def is2Dvector(val):
    return False if type(val) != list or len(val) != 2 else True

def is3DVector(val):
    return False if type(val) != list or len(val) != 3 else True

def getDiameterKey(kwargs, key, defaultRadius):
    return defaultRadius if key not in kwargs else kwargs[key] / 2

def convertPointToStr(path):
    return '[' + ', '.join([ str(p) for p in path ]) + ']'
