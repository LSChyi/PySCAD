from .util import *
from . import node

class surface(node.Node):
    def __init__(self, path, **kwargs):
        self.path = path
        self.center = getKey(kwargs, 'center', True)
        self.invert = getKey(kwargs, 'invert')
        self.convexity = getKey(kwargs, 'convexity')

    def transcript(self, linePrefix=''):
        opts = [ f'"{self.path}"' ]
        opts += [ 'center=' + 'true' if self.center else 'false' ]
        opts += [ 'invert=' + 'true' if self.invert else 'false' ]
        opts += convertToOptionList('convexity', self.convexity)
        optsStr = ', '.join(opts)
        return f'{linePrefix}surface({optsStr});\n'
