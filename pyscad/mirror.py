from .util import *
from . import node

class mirror(node.Node):
    def __init__(self, vector, target):
        if not is3DVector(vector):
            raise Exception('invalid vector: {vector}')
        self.x, self.y, self.z = vector

        self.target = target

    def transcript(self):
        targetStr = self.target.transcript()
        return f'mirror([{self.x}, {self.y}, {self.z}]){{\n' + targetStr + f'}}\n'

node.transformations['mirror'] = mirror
