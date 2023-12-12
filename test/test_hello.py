from mathics.core.load_builtin import import_and_load_builtins
from mathics.session import MathicsSession

import_and_load_builtins()

session = MathicsSession(character_encoding="ASCII")


def check_evaluation(str_expr: str, expected: str, message=""):
    """Helper function to test that a Mathics expression against
    its results"""
    result = session.evaluate(str_expr).value

    if message:
        assert result == expected, f"{message}: got: {result}"
    else:
        assert result == expected


def test_hello():
    session.evaluate('LoadModule["pymathics.hello"]') == "pymathics.hello"
    check_evaluation('Hello["World"]', "Hello, World!")
