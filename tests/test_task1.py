import pytest
from task1.solution import strict


@pytest.fixture
def func_add():
    @strict
    def add(a: int, b: int) -> int:
        return a + b

    return add


@pytest.fixture
def func_concat():
    @strict
    def concat(a: str, b: str) -> str:
        return a + b

    return concat


@pytest.fixture
def func_is_valid():
    @strict
    def is_valid(flag: bool) -> bool:
        return flag

    return is_valid


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (-5, 10, 5),
    ],
)
def test_add_valid(func_add, a, b, expected):
    assert func_add(a, b) == expected


@pytest.mark.parametrize(
    "a, b",
    [
        (1, 2.5),
        ("1", 2),
    ],
)
def test_add_invalid(func_add, a, b):
    with pytest.raises(TypeError):
        func_add(a, b)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("hello", " world", "hello world"),
        ("a", "b", "ab"),
    ],
)
def test_concat_valid(func_concat, a, b, expected):
    assert func_concat(a, b) == expected


@pytest.mark.parametrize(
    "a, b",
    [
        ("hello", 5),
        (None, "text"),
    ],
)
def test_concat_invalid(func_concat, a, b):
    with pytest.raises(TypeError):
        func_concat(a, b)


@pytest.mark.parametrize(
    "flag, expected",
    [
        (True, True),
        (False, False),
    ],
)
def test_is_valid_valid(func_is_valid, flag, expected):
    assert func_is_valid(flag) == expected


@pytest.mark.parametrize(
    "flag",
    [
        (1),
        ("True"),
        (None),
    ],
)
def test_is_valid_invalid(func_is_valid, flag):
    with pytest.raises(TypeError):
        func_is_valid(flag)
