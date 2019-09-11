from . import node
from .util import *
from .hull import hull

class resize(node.Node):
    def __init__(self, vector, target, **kwargs):
        if not is3DVector(vector):
            raise Exception('invalid vector: {vector}')
        self.x, self.y, self.z = vector
        self.auto = getKey(kwargs, 'auto')
        self.target = target

    def transcript(self):
        opts = [ f'[{self.x}, {self.y}, {self.z}]' ]
        opts += [ 'auto=' + 'true' if self.auto else 'false' ]
        optsStr = ', '.join(opts)
        targetStr = self.target.transcript()
        return f'resize({optsStr}){{\n' + targetStr + f'}}\n'

node.transformations['resize'] = resize
