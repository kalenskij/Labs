import argparse


def fill_bag(capacity, items, n):
    bag = [[0 for x in range(capacity+1)] for x in range(n + 1)]
    for i in range(1, n+1):
        for j in range(capacity+1):
            if items[i-1] <= j:
                bag[i][j] = max(bag[i-1][j], items[i-1] + bag[i-1][j-items[i-1]])
            else:
                bag[i][j] = bag[i-1][j]
    return bag[n][capacity]


parser = argparse.ArgumentParser(description="Calculates maximum possible weight")
parser.add_argument("-W", metavar="Capacity", type=int, help="An integer for capacity of bag")
parser.add_argument("-w", metavar="Items", nargs='*', type=int,
                    help="Some integers that represent weight of your items")
parser.add_argument("-n", metavar="Number of items", type=int, help="Integer for the amount of your items")
args = parser.parse_args()
result = fill_bag(args.W, args.w, args.n)
print(result)
