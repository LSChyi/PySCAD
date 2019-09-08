from . import node
from .config import *
from .union import union

class difference(union):
    def transcript(self, linePrefix=''):
        childrenStr = ''.join([ child.transcript(linePrefix + indent) for child in self.children ])
        return f'{linePrefix}difference(){{\n' + childrenStr + f'{linePrefix}}}\n'

node.booleanOperations['difference'] = difference
