from handlers.fibonacci import get_fibonacci_sequence


def test_fibonacci_once():
    assert get_fibonacci_sequence(1) == {"value": 0}


def test_fibonacci_four_times():
    assert get_fibonacci_sequence(4) == {"value": 2}
