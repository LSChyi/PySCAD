from . import node
from .union import union

class intersection(union):
    def transcript(self):
        childrenStr = ''.join([ child.transcript() for child in self.children ])
        return f'intersection(){{{childrenStr}}}'

node.booleanOperations['intersection'] = intersection
