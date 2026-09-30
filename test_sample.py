def inc(x):
    return x + 1

def test_answer():
    """A basic test function."""
    assert inc(3) == 4

def test_fail_example():
    """An example of a failing test."""
    assert inc(5) == 5 # This will fail
