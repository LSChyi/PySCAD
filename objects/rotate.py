from .util import *
from .config import *
from . import node

class rotate(node.Node):
    def __init__(self, deg, vector, targets, *args):
        if not isVector(vector):
            raise Exception('invalid vector: {vector}')
        self.x, self.y, self.z = vector
        self.deg = deg

        self.children = []
        if type(targets) != list:
            self.children.append(targets)
        else:
            self.children = targets
        self.children += args

    def transcript(self, linePrefix=''):
        childrenStr = ''.join([ child.transcript(linePrefix + indent) for child in self.children ])
        return f'{linePrefix}rotate(a={self.deg}, v=[{self.x}, {self.y}, {self.z}]){{\n' + childrenStr + f'{linePrefix}}}\n'

node.transformations['rotate'] = rotate
