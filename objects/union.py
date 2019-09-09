from .config import *
from . import node

class union(node.Node):
    def __init__(self, target, *args):
        self.children = []
        if type(target) == list:
            self.children = target
        else:
            self.children.append(target)
        self.children += args

    def transcript(self, linePrefix=''):
        childrenStr = ''.join([ child.transcript(linePrefix + indent) for child in self.children ])
        return f'{linePrefix}union(){{\n' + childrenStr + f'{linePrefix}}}\n'

node.booleanOperations['union'] = union
