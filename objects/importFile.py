from .util import *
from . import node

class importFile(node.Node):
    def __init__(self, path, **kwargs):
        self.path = path
        self.convexity = getKey(kwargs, 'convexity')
        self.layer = getKey(kwargs, 'layer')

    def transcript(self):
        opts = [ f'"{self.path}"' ]
        opts += convertToOptionList('convexity', self.convexity)
        opts += convertToOptionList('layer', self.layer)
        optsStr = ', '.join(opts)
        return f'import({optsStr});\n'
