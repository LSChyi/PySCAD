from .util import *
from .config import *
from . import node

class color(node.Node):
    def __init__(self, colorVal, target, **kwargs):
        self.colorStrVal = None
        self.a = getKey(kwargs, 'alpha', 1)
        if type(colorVal) == list:
            if len(colorVal) == 4:
                self.r, self.g, self.b, slef.a = colorVal
            elif len(colorVal) == 3:
                self.r, self.g, self.b = colorVal
        else:
            self.colorStrVal = colorVal

        self.target = target

    def transcript(self, linePrefix=''):
        targetStr = self.target.transcript(linePrefix + indent)
        opts = []
        if self.colorStrVal:
            opts.append(f'"{self.colorStrVal}"')
        else:
            opts.append(f'c = [{self.r}, {self.g}, {self.b}]')
        opts += convertToOptionList('alpha', self.a)
        optsStr = ', '.join(opts)

        return f'{linePrefix}color({optsStr}){{\n' + targetStr + f'{linePrefix}}}\n'

node.transformations['color'] = color
