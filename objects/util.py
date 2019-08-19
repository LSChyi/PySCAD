def getKey(kwargs, key, defaultVal=None):
    return defaultVal if key not in kwargs else kwargs[key]

def convertToIndent(level):
    return ' ' * (level * 2)

def convertToOptionList(key, val):
    return [ f'{key}={val}' ] if val != None else []
