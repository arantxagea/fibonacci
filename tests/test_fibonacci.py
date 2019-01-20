from src.fibonacci import compute_fibonacci


def test_fibonacci_0_is_0():
    assert 0 == compute_fibonacci(0)
