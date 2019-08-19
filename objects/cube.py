from .util import *
from .node import Node

class cube(Node):
    def __init__(self, dimension, **kwargs):
        if type(dimension) == list:
            if len(dimension) != 3:
                raise Exception(f'invalid dimension {dimension}')
            self.x, self.y, self.z = dimension
        else:
            self.x, self.y, self.z = dimension, dimension, dimension
        self.center = getKey(kwargs, 'center', True)

    def transcript(self, level=0):
        opts = []
        if self.x != self.y or self.x != self.z or self.y != self.z:
            opts += [ f'size=[ {self.x}, {self.y}, {self.z} ]' ]
        else:
            opts += [ f'size={self.x}' ]
        opts += [ 'center=' + 'true' if self.center else 'false' ]
        optsStr = ', '.join(opts)

        indent = convertToIndent(level)
        return f'{indent}cube({optsStr});\n'
