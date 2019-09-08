transformations = {}

class Node:
    def __init__(self):
        self.children = []

    def transcript(self):
        return ''.join([ child.transcript(level) for child in self.children ])

    def translate(self, vector, *args):
        return transformations['translate'](vector, self, *args)

    def scale(self, scale_factor, *args):
        return transformations['scale'](scale_factor, self, *args)

    def __str__(self):
        return self.transcript()
