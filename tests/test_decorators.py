from streamunolib import exposed, hidden


def test_exposed() -> None:
    @exposed
    def func() -> None:
        pass

    assert hasattr(func, '__exposed__')
    assert func.__exposed__ is True

    hidden(func)
    assert func.__exposed__ is False


def test_hidden() -> None:
    @hidden
    def func() -> None:
        pass

    assert hasattr(func, '__exposed__')
    assert func.__exposed__ is False

    exposed(func)
    assert func.__exposed__ is True
