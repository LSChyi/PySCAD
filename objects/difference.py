from . import node
from .union import union

class difference(union):
    def transcript(self):
        childrenStr = ''.join([ child.transcript() for child in self.children ])
        return f'difference(){{{childrenStr}}}'

node.booleanOperations['difference'] = difference
