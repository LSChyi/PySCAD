from . import node

class union(node.Node):
    def __init__(self, target, *args):
        self.children = []
        if type(target) == list:
            self.children = target
        else:
            self.children.append(target)
        self.children += args

    def transcript(self):
        childrenStr = ''.join([ child.transcript() for child in self.children ])
        return f'union(){{\n' + childrenStr + f'}}\n'

node.booleanOperations['union'] = union
