from .util import *
from .config import *
from . import node

class hull(node.Node):
    def __init__(self, targets, *args):
        self.children = []
        if type(targets) == list:
            self.children = targets
        else:
            self.children.append(targets)

        self.children += args

    def transcript(self, linePrefix=''):
        childrenStr = ''.join([ child.transcript(linePrefix + indent) for child in self.children ])
        return f'{linePrefix}hull(){{\n' + childrenStr + f'{linePrefix}}}\n'

node.transformations['hull'] = hull
