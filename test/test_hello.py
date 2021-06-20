from mathics.session import MathicsSession

session = MathicsSession(add_builtin=True, catch_interrupt=False)

def check_evaluation(str_expr: str, expected: str, message=""):
    """Helper function to test that a WL expression against
    its results"""
    result = session.evaluate(str_expr).value

    if message:
        assert result == expected, "%s: got: %s" % (message, result)
    else:
        assert result == expected


def test_hello():
    session.evaluate('LoadModule["pymathics.hello"]') == "pymathics.hello"
    check_evaluation('Hello["World"]', "Hello, World!")
