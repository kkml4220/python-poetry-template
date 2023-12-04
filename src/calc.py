# Standard Library
from typing import Union

Number = Union[int, float]


class Calc(object):
    def __init__(self, a: Number, b: Number) -> None:
        """constructor

        Args:
            a (Number): number
            b (Number): number
        """
        self.a = a
        self.b = b

    def add(self) -> Number:
        """add a and b

        Returns:
            Number: a + b
        """
        return self.a + self.b

    def sub(self) -> Number:
        """sub a and b

        Returns:
            Number: a - b
        """
        return self.a - self.b

    def mul(self) -> Number:
        """mul a and b

        Returns:
            Number: a * b
        """
        return self.a * self.b

    def div(self) -> Number:
        """div a and b

        Returns:
            Number: a / b
        """
        return self.a / self.b
