from . import node
from .hull import hull

class minkowski(hull):
    def transcript(self):
        childrenStr = ''.join([ child.transcript() for child in self.children ])
        return f'minkowski(){{\n' + childrenStr + f'}}\n'

node.transformations['minkowski'] = minkowski
