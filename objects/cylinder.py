from .util import *
from .node import Node

class cylinder(Node):
    def __init__(self, h=0, r=0, **kwargs):
        self.center = getKey(kwargs, 'center', True)
        self.h = h
        self.r1 = r
        self.r2 = getKey(kwargs, 'r2', r)
        self.fa = getKey(kwargs, 'fa')
        self.fs = getKey(kwargs, 'fs')
        self.fn = getKey(kwargs, 'fn')

    def transcript(self):
        opts = [ f'h={self.h}' ]
        if self.r1 != self.r2:
            opts += [ f'r1={self.r1}', f'r2={self.r2}' ]
        else:
            opts += [ f'r={self.r1}' ]
        opts += convertToOptionList('$fa', self.fa)
        opts += convertToOptionList('$fs', self.fs)
        opts += convertToOptionList('$fn', self.fn)
        opts += [ 'center=' + 'true' if self.center else 'false' ]
        optsStr = ', '.join(opts)
        
        return f'cylinder({optsStr});'
