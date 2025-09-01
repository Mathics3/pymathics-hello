# -*- coding: utf-8 -*-
"""
Mathics3 Module hello module.

This is an example of an external Mathics3 module.

A Mathics3 module is a Python module which can be loaded into Mathics using the
``LoadModule[]`` method.

In particular, to load this after installing this module as a Python module run inside
Mathics:

   ::

   In[1]:= LoadModule["pymathics.hello"]
   Out[1]= pymathics.hello

If you don't get an error, you should then be able to run:

   ::

   In[2]:= Hello["World"]
   Out[2]:= Hello, World!

   In[3]:= PyMathics`$HelloUser
   Out[3]:= $your-login-name$

"""

from pymathics.hello.version import __version__
from pymathics.hello.__main__ import Hello

__all__ = ("__version__", "Hello", "pymathics_version_data")

# To be recognized as an external mathics module, the following variable
# is required:
#
pymathics_version_data = {
    "author": "The Mathics3 Team",
    "version": __version__,
    "requires": [],
}
