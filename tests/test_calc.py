# Third Party Library
from pytest import raises

# First Party Library
from src.calc import Calc


class TestCalc(object):
    def setup_method(self) -> None:
        self.c = Calc(10, 5)

    def teardown_method(self) -> None:
        del self.c

    def test__init__(self) -> None:
        assert self.c.a == 10
        assert self.c.b == 5
        assert isinstance(self.c.a, int)
        assert isinstance(self.c.b, int)

    def test_add(self) -> None:
        assert self.c.add() == 15

    def test_sub(self) -> None:
        assert self.c.sub() == 5

    def test_mul(self) -> None:
        assert self.c.mul() == 50

    def test_div(self) -> None:
        assert self.c.div() == 2


def test_div() -> None:
    with raises(ZeroDivisionError):
        c = Calc(10, 0)
        c.div()
