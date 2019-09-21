.. PySCAD documentation master file, created by
   sphinx-quickstart on Sat Sep 21 11:26:10 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PySCAD: Python 3D Modeling Tool
===============================

**PySCAD** is a 3D modeling libaray that allows users to adpot the elegacne, power 
and simplity of Python to design 3D models with `OpenSCAD <https://www.openscad.org>`_.

-------------------

The most powerful feature, also the biggest difference between other 3D modeling libraries 
of PySCAD is that you can design the model in a very natural way. Check the picture
below, how will you describe this model?

.. image:: https://i.imgur.com/nKD7bJ5.png

Usually, we would say "a cube with a hollowed sphere being placed at some position",
but how do we implement this in OpenSCAD? We would write OpenSCAD code like this::

    translate([-10, 0, 0]) {
        difference() {
            cube(10, center=true);
            sphere(6, $fn=200);
        }
    }

, which is very different from how we describe it while reading and writing this 
code. With PySCAD, you can write code like this::
    
    cube(10).difference(sphere(6, fn=200)).translate([-10, 0, 0])

, which makes implementing the code has the same flow when we are describing it,
and this greatly relief the minds of developers and designers.

API Documentation
-----------------
Below is the documentation for a specific function or class.

.. toctree::
   :maxdepth: 2

   api



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
