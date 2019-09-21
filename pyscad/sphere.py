from .util import *
from .node import Node

class sphere(Node):
    def __init__(self, r=0, **kwargs):
        self.r = getDiameterKey(kwargs, 'd', r)
        self.fa = getKey(kwargs, 'fa')
        self.fs = getKey(kwargs, 'fs')
        self.fn = getKey(kwargs, 'fn')

    def transcript(self):
        opts = [ f'r={self.r}' ]
        opts += convertToOptionList('$fa', self.fa)
        opts += convertToOptionList('$fs', self.fs)
        opts += convertToOptionList('$fn', self.fn)
        optsStr = ', '.join(opts)
        
        return f'sphere({optsStr});\n'
