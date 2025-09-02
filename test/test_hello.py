# -*- coding: utf-8 -*-

from mathics.core.load_builtin import import_and_load_builtins
from mathics.session import MathicsSession

import_and_load_builtins()

session = MathicsSession(character_encoding="ASCII")


def check_evaluation(str_expr: str, expected: str, assert_message=""):
    """Helper function to test that a Mathics3 expression against
    its results"""
    result = session.evaluate(str_expr).value

    if assert_message:
        print(f"got: {result}, expect: {expected} -- {assert_message}")
        assert result == expected, assert_message
    else:
        print(f"got: {result}, expect: {expected}")

    if assert_message:
        assert result == expected, f"{assert_message}: got: {result}"
    else:
        assert result == expected


def test_hello():
    session.evaluate('LoadModule["pymathics.hello"]') == "pymathics.hello"
    check_evaluation('Hello["everyone"]', "Hello, everyone!")
    check_evaluation("Hello[]", "Hello, World!")
