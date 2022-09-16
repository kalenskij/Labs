import argparse


def isvalid(line, n):
    if not line[n].isdigit():
        if (line[n] == "-" or line[n] == "+") and n != len(line) - 1:
            if not line[n + 1].isdigit():
                return False
        else:
            return False
    return True


parser = argparse.ArgumentParser()
parser.add_argument("line_parsed", nargs="?", type=str)
args = parser.parse_args()
ind = False
if args.line_parsed:
    ind = True
if ind:
    for i in range(0, len(args.line_parsed)):
        ind = isvalid(args.line_parsed, i)
if ind:
    try:
        print("True,", eval(args.line_parsed))
    except SyntaxError:
        print("False,", None)
else:
    print("False,", None)
