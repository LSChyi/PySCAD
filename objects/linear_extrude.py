from . import node
from .util import *

class linear_extrude(node.Node):
    def __init__(self, h, target, **kwargs):
        self.h = h
        self.target = target
        self.center = getKey(kwargs, 'center', True)
        self.convexity = getKey(kwargs, 'convexity')
        self.twist = getKey(kwargs, 'twist')
        self.slices = getKey(kwargs, 'slices')
        self.scale = getKey(kwargs, 'scale')
        self.fn = getKey(kwargs, 'fn')

    def transcript(self):
        opts = [ f'height={self.h}' ]
        opts += [ 'center=' + 'true' if self.center else 'false' ]
        opts += convertToOptionList('convexity', self.convexity)
        opts += convertToOptionList('twist', self.twist)
        opts += convertToOptionList('slices', self.slices)
        opts += convertToOptionList('scale', self.scale)
        opts += convertToOptionList('$fn', self.fn)
        optsStr = ', '.join(opts)
        targetStr = self.target.transcript()
        return f'linear_extrude({optsStr}){{\n' + targetStr + f'}}\n'

node.transformations['linear_extrude'] = linear_extrude
