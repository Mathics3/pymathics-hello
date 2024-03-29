# -*- coding: utf-8 -*-
from mathics.core.atoms import String
from mathics.core.builtin import Builtin


class Hello(Builtin):
    """
    <dl>
      <dt>'Hello'[$person$]
      <dd>An example function in a Python-importable Mathics module.
    </dl>
    >> Hello["World"]
     = Hello, World!
    """

    # The function below should start with "apply"
    def eval_with_name(self, person, evaluation):
        "%(name)s[person_String]"
        # %(name)s is just a more flexible way of writing "Hello".
        # If the class name changes, so will the above pattern.
        # The above pattern matches Hello with a single string argument.
        # See https://reference.wolfram.com/language/tutorial/Patterns.html#7301
        # and https://reference.wolfram.com/language/ref/Cases.html
        return String(f"Hello, {person.value}!")
