from .util import *
from .config import *
from . import node

class mirror(node.Node):
    def __init__(self, vector, target):
        if not isVector(vector):
            raise Exception('invalid vector: {vector}')
        self.x, self.y, self.z = vector

        self.target = target

    def transcript(self, linePrefix=''):
        targetStr = self.target.transcript(linePrefix + indent)
        return f'{linePrefix}mirror([{self.x}, {self.y}, {self.z}]){{\n' + targetStr + f'{linePrefix}}}\n'

node.transformations['mirror'] = mirror
