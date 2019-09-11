from .util import *
from . import node

class translate(node.Node):
    def __init__(self,  vector, targets, *args):
        if not is3DVector(vector):
            raise Exception('invalid vector: {vector}')
        self.x, self.y, self.z = vector

        self.children = []
        if type(targets) != list:
            self.children.append(targets)
        else:
            self.children = targets
        self.children += args

    def transcript(self):
        childrenStr = ''.join([ child.transcript() for child in self.children ])
        return f'translate([{self.x}, {self.y}, {self.z}]){{\n' + childrenStr + f'}}\n'

node.transformations['translate'] = translate
