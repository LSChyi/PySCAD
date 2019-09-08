from . import node
from .hull import hull

class minkowski(hull):
    def transcript(self):
        childrenStr = ''.join([ child.transcript() for child in self.children ])
        return f'minkowski(){{{childrenStr}}}'

node.transformations['minkowski'] = minkowski
