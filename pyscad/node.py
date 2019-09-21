"""Base for all other modules"""
transformations = {}
booleanOperations = {}

indentNum = 2

class Node:
    """The base of all classes

    This class implements a shortcut of transformations and boolean operations, 
    which allow users to call these shortcut methods in a cascading way. As a 
    result, all classes inherent from it also have the cascading way to call 
    transformations and boolean operations, and all classes in PySCAD are also
    a kind of Node.
    """
    def __init__(self):
        """Initialization of the class"""
        self.children = []

    def union(self, *args):
        """Short cut of union operation

        Parameters
        ----------
        *args: list of nodes, ex: union([node1, node2]) or union(node1, node2)
            The nodes to be unionized with this objects.

        Returns
        -------
        node: Node
            An union node.
        """
        return booleanOperations['union'](composeTargets(self, *args))

    def difference(self, *args):
        """Short cut of difference operation

        Parameters
        ----------
        *args: list of nodes, ex: difference([node1, node2]) or difference(node1, node2)
            The nodes to be eliminated with this objects.

        Returns
        -------
        node: Node
            A difference node.
        """
        return booleanOperations['difference'](composeTargets(self, *args))

    def intersection(self, *args):
        """Short cut of intersection operation

        Parameters
        ----------
        *args: list of nodes, ex: intersection([node1, node2]) or intersection(node1, node2)
            The nodes to be intersected with this objects.

        Returns
        -------
        node: Node
            A intersection node.
        """
        return booleanOperations['intersection'](composeTargets(self, *args))

    def linear_extrude(self, h, **kwargs):
        """Short cut of linear_extrude transformation

        Parameters
        ----------
        h: number
            Extrusion height.
        **center: boolean
            Generate this extrusion at center, default is True.
        **convexity: number
            The convexity for the extrusion.
        **twist: number
            The twist used in this extrusion.
        **slices: number
            The slice used in this extrusion.
        **scale: number
            The scale used in this extrusion.
        **fn: number
            The $fn used in this extrusion.

        Returns
        -------
        node: Node
            A linear_extrude node.
        """
        return transformations['linear_extrude'](h, self, **kwargs)

    def rotate_extrude(self, **kwargs):
        """Short cut of rotate_extrude transformation

        Parameters
        ----------
        **angle: number
            The angle for the extrusion.
        **convexity: number
            The convexity for the extrusion.

        Returns
        -------
        node: Node
            A rotate_extrude node.
        """
        return transformations['rotate_extrude'](self, **kwargs)

    def projection(self, **kwargs):
        """Short cut of projection transformation

        Parameters
        ----------
        **cut: boolean
            The cut used in this projection, default is False.

        Returns
        -------
        node: Node
            A projection node.
        """
        return transformations['projection'](self, **kwargs)

    def translate(self, vector):
        """Short cut of translate transformation

        Parameters
        ----------
        vector: a list composed of 3 numbers
            Indicates how to move this object.

        Returns
        -------
        node: Node
            A translate node.
        """
        return transformations['translate'](vector, self)

    def rotate(self, deg, vector):
        """Short cut of translate transformation

        Parameters
        ----------
        deg: nubmer
            The degree to rotate.
        vector: a list composed of 3 numbers
            The axis used in rotation. In OpenSCAD, it follows the right hand rule.

        Returns
        -------
        node: Node
            A rotate node.
        """
        return transformations['rotate'](deg, vector, self)

    def scale(self, scale_factor):
        """Short cut of scale transformation

        Parameters
        ----------
        scale_factor: a list composed of 3 numbers
            The vector used in scale transformation.

        Returns
        -------
        node: Node
            A scale node.
        """
        return transformations['scale'](scale_factor, self)

    def resize(self, vector, **kwargs):
        """Short cut of resize transformation

        Parameters
        ----------
        vector: a list composed of 3 numbers
            The vector used in resize transformation.
        **auto: boolean
            Whether to auto-scale any 0-valued dimension in given vector.

        Returns
        -------
        node: Node
            A resize node.
        """
        return transformations['resize'](vector, self, **kwargs)

    def mirror(self, vector):
        """Short cut of mirror transformation

        Parameters
        ----------
        vector: a list composed of 3 numbers
            The normal vector of a plane used in mirror transformation.

        Returns
        -------
        node: Node
            A mirror node.
        """
        return transformations['mirror'](vector, self)

    def color(self, colorVal, **kwargs):
        """Short cut of color transformation

        Parameters
        ----------
        colorVal: color name (str), hex value(str), 3-d vector([r, g, b]) or 4-d vector([r, g, b, a])
            The color value.
        **alpha: number
            The alpha value used in this color.

        Returns
        -------
        node: Node
            A color node.
        """
        return transformations['color'](colorVal, self, **kwargs)

    def offset(self, **kwargs):
        """Short cut of offset transformation

        Parameters
        ----------
        r: number
            Amount to offset.
        delta: number
            Amount to offset.
        chamfer: boolean
            Whether to apply chamfer on the offset when using delta, default is False.

        Returns
        -------
        node: Node
            A offset node.
        """
        return transformations['offset'](self, **kwargs)

    def hull(self, *args):
        """Short cut of hull transformation

        Parameters
        ----------
        *args: list of nodes, ex: hull([node1, node2]) or hull(node1, node2)
            The nodes to be hulled with this objects.

        Returns
        -------
        node: Node
            A hull node.
        """
        return transformations['hull'](composeTargets(self, *args))

    def minkowski(self, *args):
        """Short cut of minkowski transformation

        Parameters
        ----------
        *args: list of nodes, ex: minkowski([node1, node2]) or minkowski(node1, node2)
            The nodes to apply minkowski transformation with this objects.

        Returns
        -------
        node: Node
            A minkowski node.
        """
        return transformations['minkowski'](composeTargets(self, *args))

    def transcript(self):
        """transcript to OpenSCAD code

        No indentation will be added.
        """
        return ''.join([ child.transcript() for child in self.children ])

    def __str__(self):
        """transcript to OpenSCAD code

        Indentation is added.
        """
        lines = self.transcript()
        counter = 0
        res = []
        for line in lines.splitlines():
            if line[-1] == '{':
                res.append(' ' * indentNum * counter + line)
                counter += 1
            elif line[-1] == '}':
                counter -= 1
                res.append(' ' * indentNum * counter + line)
            else:
                res.append(' ' * indentNum * counter + line)
        return '\n'.join(res)

def composeTargets(target, *args):
    """Convert inputs to a list of nodes"""
    targets = [ target ]
    for obj in args:
        if type(obj) == list:
            if len(args) != 1:
                raise Exception(f'invalid input parameters')
            targets += obj
        else:
            targets.append(obj)
    return targets
