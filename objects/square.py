from .util import *
from .node import Node

class square(Node):
    def __init__(self, dimension, **kwargs):
        if type(dimension) == list:
            if len(dimension) != 2:
                raise Exception(f'invalid dimention for square {dimension}')
            self.x, self.y = dimension
        else:
            self.x = self.y = dimension
        self.center = getKey(kwargs, 'center', True)

    def transcript(self, linePrefix=''):
        opts = []
        if self.x != self.y:
            opts += [ f'size=[{self.x}, {self.y}]' ]
        else:
            opts += [ f'size={self.x}' ]
        opts += [ 'center=' + 'true' if self.center else 'false' ]
        optsStr = ', '.join(opts)

        return f'{linePrefix}square({optsStr});\n'
