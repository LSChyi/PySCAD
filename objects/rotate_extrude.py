from . import node
from .config import *
from .util import *

class rotate_extrude(node.Node):
    def __init_(self, target, **kwargs):
        self.target = target
        self.angle = getKey(kwargs, 'angle')
        self.convexity = getKey(kwargs, 'convexity')

    def transcript(self, linePrefix=''):
        opts = []
        opts += convertToOptionList('angle', self.angle)
        opts += convertToOptionList('convexity', self.convexity)
        optsStr = ', '.join(opts)
        targetStr = self.target.transcript(linePrefix + indent)
        return f'{linePrefix}rotate_extrude({optsStr}){{\n' + targetStr + f'{linePrefix}}}\n'

node.transformations['rotate_extrude'] = rotate_extrude
