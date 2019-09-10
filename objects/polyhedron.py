from .util import *
from . import node

class polyhedron(node.Node):
    def __init__(self, points, faces=[], **kwargs):
        for point in points:
            if not is3DVector(point):
                raise Exception(f'invalid point {point}')
        self.points = points
        self.faces = faces
        self.convexity = getKey(kwargs, 'convexity')

    def transcript(self, linePrefix=''):
        points = ', '.join([ convertPointToStr(p) for p in self.points ])
        faces = ', '.join([ convertPointToStr(p) for p in self.faces ])
        opts = [ f'points=[{points}]' ]
        opts += [ f'faces=[{faces}]' ] if self.faces else []
        opts += convertToOptionList('convexity', self.convexity)
        optsStr = ', '.join(opts)
        return f'{linePrefix}polyhedron({optsStr})\n'
