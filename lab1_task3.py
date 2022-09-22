import argparse


def isvalid(line):
    ind = True
    if line:
        for i in range(len(line)):
            if not line[i].isdigit():
                if line[i] in ("-", "+") and i not in (len(line)-1, 0):
                    if not line[i + 1].isdigit():
                        ind = False
                        break
                else:
                    ind = False
                    break
    else:
        ind = False
    return ind


parser = argparse.ArgumentParser()
parser.add_argument("line_parsed", nargs="?", type=str)
args = parser.parse_args()
if isvalid(args.line_parsed):
    try:
        print("True,", eval(args.line_parsed))
    except SyntaxError:
        print("False,", None)
else:
    print("False,", None)