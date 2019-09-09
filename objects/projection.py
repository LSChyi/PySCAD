from .util import *
from .config import *
from . import node

class projection(node.Node):
    def __init__(self, target, **kwargs):
        self.cut = getKey(kwargs, 'cut', False)
        self.target = target

    def transcript(self, linePrefix=''):
        targetStr = self.target.transcript(linePrefix + indent)
        cutStr = 'cut=true' if self.cut else ''
        return f'{linePrefix}projection({cutStr}){{\n' + targetStr + f'{linePrefix}}}\n'

node.transformations['projection'] = projection
