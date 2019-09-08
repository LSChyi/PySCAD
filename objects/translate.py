from .util import *
from .config import *
from . import node

class translate(node.Node):
    def __init__(self,  vector, targets, *args):
        if not isVector(vector):
            raise Exception('invalid vector: {vector}')
        self.x, self.y, self.z = vector

        self.children = []
        if type(targets) != list:
            self.children.append(targets)
        else:
            self.children = targets
        self.children += args

    def transcript(self, linePrefix=''):
        childrenStr = ''.join([ child.transcript(linePrefix + indent) for child in self.children ])
        return f'{linePrefix}translate([{self.x}, {self.y}, {self.z}]){{\n' + childrenStr + f'{linePrefix}}}\n'

node.transformations['translate'] = translate
