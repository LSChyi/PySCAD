from . import node
from .config import *
from .union import union

class intersection(union):
    def transcript(self, linePrefix=''):
        childrenStr = ''.join([ child.transcript(linePrefix + indent) for child in self.children ])
        return f'{linePrefix}intersection(){{\n' + childrenStr + f'{linePrefix}}}\n'

node.booleanOperations['intersection'] = intersection
