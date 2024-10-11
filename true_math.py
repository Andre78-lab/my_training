from math import inf
def divide(first, second):
    if second == 0:
        if first >= 0:
            return inf
        else:
            return -inf
    else:
        return first/second

