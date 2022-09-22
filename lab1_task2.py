import argparse
import operator
import math


def calculate(my_oper, *args) -> str:
    try:
        operator_func = getattr(operator, my_oper)
        return operator_func(*args)
    except AttributeError:
        try:
            math_func = getattr(math, my_oper)
            return math_func(*args)
        except Exception:
            return "Error"
    except ZeroDivisionError:
        return "Zero Division Error"



parser = argparse.ArgumentParser()
parser.add_argument("Operator", type=str)
parser.add_argument("Numbers", type=int, nargs="+")
args = parser.parse_args()

print(calculate(args.Operator, *args.Numbers))
