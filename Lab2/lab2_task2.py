from math import gcd


class Rational:

    def __init__(self, numerator=1, denominator=1):
        """
        :param numerator: Numerator of the rational number
        :param denominator: Denominator of the rational number
        """
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Type Error")
        if not denominator:
            raise ZeroDivisionError("ZeroDivisionError")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        numerator = self.numerator//gcd(self.numerator, self.denominator)
        denominator = self.denominator//gcd(self.numerator, self.denominator)
        return f"{numerator}/{denominator}"

    def __add__(self, other):
        result_numerator = self.numerator*other.denominator + other.numerator*self.denominator
        result_denominator = self.denominator*other.denominator
        return Rational(result_numerator, result_denominator)

    def __sub__(self, other):
        result_numerator = self.numerator*other.denominator - other.numerator*self.denominator
        result_denominator = self.denominator*other.denominator
        return Rational(result_numerator, result_denominator)

    def __mul__(self, other):
        result_numerator = self.numerator*other.numerator
        result_denominator = self.denominator*other.denominator
        return Rational(result_numerator, result_denominator)

    def __truediv__(self, other):
        result_numerator = self.numerator*other.denominator
        result_denominator = self.denominator*other.numerator
        return Rational(result_numerator, result_denominator)

    def get_float(self):
        return self.numerator/self.denominator


a1 = Rational(1, 4)
a2 = Rational(1, 2)
m = a1 + a2
print(m)
print(m.get_float())
