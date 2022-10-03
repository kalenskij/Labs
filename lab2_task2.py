from math import gcd


class Rational:

    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Type Error")
        self.numerator = numerator//gcd(numerator, denominator)
        if not denominator:
            raise ZeroDivisionError("ZeroDivisionError")
        self.denominator = denominator//gcd(numerator, denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def get_float(self):
        return self.numerator/self.denominator

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


a1 = Rational(2, 4)
a2 = Rational(1, 2)
m = a1 / a2
print(m)