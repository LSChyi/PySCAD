from .util import *
from . import node

class text(node.Node):
    def __init__(self, text, **kwargs):
        self.text = text
        self.size = getKey(kwargs, 'size')
        self.font = getKey(kwargs, 'font')
        self.halign = getKey(kwargs, 'halign')
        self.valing = getKey(kwargs, 'valing')
        self.direction = getKey(kwargs, 'direction')
        self.language = getKey(kwargs, 'language')
        self.script = getKey(kwargs, 'scripte')
        self.fn = getKey(kwargs, 'fn')

    def transcript(self, linePrefix=''):
        opts = [ f'"{self.text}"' ]
        opts += convertToOptionList('size', self.size)
        opts += convertToStringOptionList('font', self.font)
        opts += convertToStringOptionList('halign', self.halign)
        opts += convertToStringOptionList('valing', self.valing)
        opts += convertToStringOptionList('direction', self.direction)
        opts += convertToStringOptionList('language', self.language)
        opts += convertToStringOptionList('script', self.script)
        opts += convertToOptionList('$fn', self.fn)
        optsStr = ', '.join(opts)
        return f'{linePrefix}text();\n'
    
def convertToStringOptionList(key, val):
    return [ f'{key}="{val}"' ] if val != None else []
