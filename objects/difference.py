from . import node
from .union import union

class difference(union):
    def transcript(self):
        childrenStr = ''.join([ child.transcript() for child in self.children ])
        return f'difference(){{\n' + childrenStr + f'}}\n'

node.booleanOperations['difference'] = difference
