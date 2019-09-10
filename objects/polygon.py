from .util import *
from . import node

class polygon(node.Node):
    def __init__(self, points, paths=[], **kwargs):
        for point in points:
            if not is2Dvector(point):
                raise Exception(f'invalid point {point}')
        self.points = points
        self.paths = paths
        self.convexity = getKey(kwargs, 'convexity')

    def transcript(self, linePrefix=''):
        def convertPoint(path):
            return '[' + ', '.join([ str(p) for p in path ]) + ']'
        points = ', '.join([ convertPoint(p) for p in self.points ])
        paths = ', '.join([ convertPoint(path) for path in self.paths ])
        opts = [ f'points=[{points}]' ]
        opts += [ f'paths=[{paths}]' ] if self.paths else []
        opts += convertToOptionList('convexity', self.convexity)
        optsStr = ', '.join(opts)
        return f'{linePrefix}polygon({optsStr})\n'
