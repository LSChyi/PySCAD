from . import node
from .union import union

class intersection(union):
    def transcript(self):
        childrenStr = ''.join([ child.transcript() for child in self.children ])
        return f'intersection(){{\n' + childrenStr + f'}}\n'

node.booleanOperations['intersection'] = intersection
