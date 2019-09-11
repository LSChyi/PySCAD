from .util import *
from . import node

class projection(node.Node):
    def __init__(self, target, **kwargs):
        self.cut = getKey(kwargs, 'cut', False)
        self.target = target

    def transcript(self):
        targetStr = self.target.transcript()
        cutStr = 'cut=true' if self.cut else ''
        return f'projection({cutStr}){{\n' + targetStr + f'}}\n'

node.transformations['projection'] = projection
