from .util import *
from . import node

class offset(node.Node):
    def __init__(self, target, **kwargs):
        self.target = target
        self.r = getKey(kwargs, 'r')
        self.delta = getKey(kwargs, 'delta')
        self.chamfer = getKey(kwargs, 'chamfer')

    def transcript(self):
        opts = []
        if self.r:
            opts += convertToOptionList('r', self.r)
        elif self.delta:
            opts += convertToOptionList('delta', self.delta)
        opts += [ 'chamfer=' + 'true' if self.chamfer else 'false' ]
        optsStr = ', '.join(opts)

        targetStr = self.target.transcript()

        return f'offset({optsStr}){{\n' + targetStr + f'}}\n'

node.transformations['offset'] = offset
