from . import node
from .util import *

class rotate_extrude(node.Node):
    def __init__(self, target, **kwargs):
        self.target = target
        self.angle = getKey(kwargs, 'angle')
        self.convexity = getKey(kwargs, 'convexity')

    def transcript(self):
        opts = []
        opts += convertToOptionList('angle', self.angle)
        opts += convertToOptionList('convexity', self.convexity)
        optsStr = ', '.join(opts)
        targetStr = self.target.transcript()
        return f'rotate_extrude({optsStr}){{\n' + targetStr + f'}}\n'

node.transformations['rotate_extrude'] = rotate_extrude
