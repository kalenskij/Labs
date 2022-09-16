import argparse
import operator


parser = argparse.ArgumentParser()
parser.add_argument("Operator", type=str, nargs="?")
parser.add_argument("Number1", type=int, nargs="?")
parser.add_argument("Number2", type=int, nargs="?")
args = parser.parse_args()
try:
    print(eval("operator." + args.Operator + "(" + str(args.Number1) + ", " + str(args.Number2) + ")"))
except AttributeError:
    print("Wrong Operator")
except ZeroDivisionError:
    print("Division by zero")
except TypeError:
    print("Type error (some arguments maybe missing)")
