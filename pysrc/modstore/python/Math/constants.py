class Infinity:
    def __repr__(self) -> str:
        return "Infinity"

    def __str__(self) -> str:
        return "inf"

    def __float__(self) -> float:
        return float('inf')

    def __eq__(self, other) -> bool:
        if isinstance(other, (int, float)):
            return float('inf') == float(other)
        return isinstance(other, Infinity)

    def __lt__(self, other) -> bool:
        if isinstance(other, (int, float)):
            return False  # Infinity is never less than any real number
        return False

    def __le__(self, other) -> bool:
        if isinstance(other, (int, float)):
            return float('inf') <= float(other)
        return isinstance(other, Infinity)

    def __gt__(self, other) -> bool:
        if isinstance(other, (int, float)):
            return True  # Infinity is always greater than any real number
        return not isinstance(other, Infinity)

    def __ge__(self, other) -> bool:
        if isinstance(other, (int, float)):
            return float('inf') >= float(other)
        return isinstance(other, Infinity)

    def __add__(self, other):
        return self  # Infinity + any number = Infinity

    def __radd__(self, other):
        return self  # Any number + Infinity = Infinity

    def __sub__(self, other):
        if isinstance(other, Infinity):
            raise ValueError("Indeterminate form: Infinity - Infinity")
        return self  # Infinity - any number = Infinity

    def __rsub__(self, other):
        if isinstance(other, Infinity):
            raise ValueError("Indeterminate form: Infinity - Infinity")
        return -self  # Real number - Infinity = -Infinity

    def __mul__(self, other):
        if other == 0:
            raise ValueError("Indeterminate form: Infinity * 0")
        return self if other > 0 else -self  # Infinity * positive = Infinity, Infinity * negative = -Infinity

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Infinity):
            raise ValueError("Indeterminate form: Infinity / Infinity")
        if other == 0:
            raise ZeroDivisionError("Division by zero")
        return self if other > 0 else -self  # Infinity / positive = Infinity, Infinity / negative = -Infinity

    def __rtruediv__(self, other):
        if other == 0:
            return 0  # 0 / Infinity = 0
        raise ValueError("Indeterminate form: Real number / Infinity")

    def __neg__(self):
        return NegativeInfinity()  # -Infinity

    def __pow__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                return 1  # Infinity^0 = 1
            if other > 0:
                return self  # Infinity^positive = Infinity
            return 0  # Infinity^negative = 0
        raise ValueError("Invalid exponent for Infinity")

    def __rpow__(self, other):
        if other == 0:
            return 0  # 0^Infinity = 0
        if other > 1:
            return self  # Base > 1 and positive = Infinity
        return 0  # 0 < base < 1 raised to Infinity = 0

class NegativeInfinity(Infinity):
    def __repr__(self) -> str:
        return "-Infinity"

    def __str__(self) -> str:
        return "-inf"

    def __float__(self) -> float:
        return float('-inf')

    def __neg__(self):
        return Infinity()  # Double negative gives positive infinity

    def __add__(self, other):
        return self  # -Infinity + any number = -Infinity

    def __sub__(self, other):
        if isinstance(other, Infinity):
            raise ValueError("Indeterminate form: -Infinity - Infinity")
        return self  # -Infinity - any number = -Infinity

    def __mul__(self, other):
        if other == 0:
            raise ValueError("Indeterminate form: -Infinity * 0")
        return self if other > 0 else -self  # -Infinity * positive = -Infinity, -Infinity * negative = Infinity

    def __truediv__(self, other):
        if isinstance(other, NegativeInfinity):
            raise ValueError("Indeterminate form: -Infinity / -Infinity")
        if isinstance(other, Infinity):
            return -1  # -Infinity / Infinity = -1
        return super().__truediv__(other)