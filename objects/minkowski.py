from . import node
from .config import *
from .hull import hull

class minkowski(hull):
    def transcript(self, linePrefix=''):
        childrenStr = ''.join([ child.transcript(linePrefix + indent) for child in self.children ])
        return f'{linePrefix}minkowski(){{\n' + childrenStr + f'{linePrefix}}}\n'

node.transformations['minkowski'] = minkowski
