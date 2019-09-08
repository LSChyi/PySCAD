from .util import *
from .config import *
from . import node

class scale(node.Node):
    def __init__(self, scale_factor, target):
        if isVector(scale_factor):
            self.x, self.y, self.z = scale_factor
        elif type(scale_factor) == int or float:
            self.x = self.y = self.z = scale_factor
        else:
            raise Exception(f'invalid scale factory {scale_factor}')

        self.target = target

    def transcript(self, linePrefix=''):
        targetStr = self.target.transcript(linePrefix + indent)
        return f'{linePrefix}scale([{self.x}, {self.y}, {self.z}]){{' + targetStr + f'{linePrefix}}}\n'

node.transformations['scale'] = scale
