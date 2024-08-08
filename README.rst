Test PyMathics module

This is a Python module for Mathics that is an simple "Hello, World" example
that is typically used as a minimal example for demonstration.

You can also use this as a template to clone if you want to create your own Pymathics module.

Here we are demonstrating how to write a PyMathics module.

To install in development mode (run code from the source tree):

::

   $ make develop


After installing inside Mathics you can load this using the
``LoadModule[]`` function.

Then the function ```Hello[]`` is available::

      $ mathicsscript
      In[1]:= LoadModule["pymathics.hello"]
      Out[1]= pymathics.hello

      In[2]:= Hello["World"]
      Out[2]:= Hello, World!

You can test with ``py.test``::

     $ py.test test

or simply::

     $ make check
