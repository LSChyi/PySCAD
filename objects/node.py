transformations = {}
booleanOperations = {}

class Node:
    def __init__(self):
        self.children = []

    def union(self, *args):
        return booleanOperations['union'](composeTargets(self, *args))

    def difference(self, *args):
        return booleanOperations['difference'](composeTargets(self, *args))

    def intersection(self, *args):
        return booleanOperations['intersection'](composeTargets(self, *args))

    def linear_extrude(self, h, **kwargs):
        return transformations['linear_extrude'](h, self, **kwargs)

    def rotate_extrude(self, **kwargs):
        return transformations['rotate_extrude'](self, **kwargs)

    def projection(self, **kwargs):
        return transformations['projection'](self, **kwargs)

    def translate(self, vector):
        return transformations['translate'](vector, self)

    def rotate(self, deg, vector):
        return transformations['rotate'](deg, vector, self)

    def scale(self, scale_factor):
        return transformations['scale'](scale_factor, self)

    def resize(self, vector, **kwargs):
        return transformations['resize'](vector, self, **kwargs)

    def mirror(self, vector):
        return transformations['mirror'](vector, self)

    def color(self, colorVal, **kwargs):
        return transformations['color'](colorVal, self, **kwargs)

    def offset(self, **kwargs):
        return transformations['offset'](self, **kwargs)

    def hull(self, *args):
        return transformations['hull'](composeTargets(self, *args))

    def minkowski(self, *args):
        return transformations['minkowski'](composeTargets(self, *args))

    def transcript(self):
        return ''.join([ child.transcript(level) for child in self.children ])

    def __str__(self):
        return self.transcript()

def composeTargets(target, *args):
    targets = [ target ]
    for obj in args:
        if type(obj) == list:
            if len(args) != 1:
                raise Exception(f'invalid input parameters')
            targets += obj
        else:
            targets.append(obj)
    return targets
