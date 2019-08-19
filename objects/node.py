class Node:
    def __init__(self):
        self.childs = []

    def _transcript(self, level):
        return ''.join([ child.transcript(level) for child in self.childs ])

    def transcript(self, level=0):
        return self._transcript(self, level)

    def __str__(self):
        return self.transcript(0)
