from math import inf


def divde(first, second):
    if second == 0:
        return inf
    else:
        div = first / second
        return div


if __name__ == '__main__':
    divde(5, 0)
    divde(5, 1)
