transformations = {}

class Node:
    def __init__(self):
        self.children = []

    def transcript(self):
        return ''.join([ child.transcript(level) for child in self.children ])

    def translate(self, vector):
        return transformations['translate'](vector, self)

    def scale(self, scale_factor):
        return transformations['scale'](scale_factor, self)

    def mirror(self, vector):
        return transformations['mirror'](vector, self)

    def hull(self, *args):
        return transformations['hull'](composeTargets(self, *args))

    def __str__(self):
        return self.transcript()

def composeTargets(target, *args):
    targets = [ target ]
    for obj in args:
        if type(obj) == list:
            targets += obj
        else:
            targets.append(obj)
    return targets
