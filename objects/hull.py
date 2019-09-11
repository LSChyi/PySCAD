from .util import *
from . import node

class hull(node.Node):
    def __init__(self, targets, *args):
        self.children = []
        if type(targets) == list:
            self.children = targets
        else:
            self.children.append(targets)

        self.children += args

    def transcript(self):
        childrenStr = ''.join([ child.transcript() for child in self.children ])
        return f'hull(){{\n' + childrenStr + f'}}\n'

node.transformations['hull'] = hull
