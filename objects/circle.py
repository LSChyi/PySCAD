from .util import *
from .sphere import sphere

class circle(sphere):
    def transcript(self, linePrefix=''):
        opts = [ f'r={self.r}' ]
        opts += convertToOptionList('$fa', self.fa)
        opts += convertToOptionList('$fs', self.fs)
        opts += convertToOptionList('$fn', self.fn)
        optsStr = ', '.join(opts)
        return f'{linePrefix}circle({optsStr})\n'
