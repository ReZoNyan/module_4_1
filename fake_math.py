def divde(first, second):
    if second == 0:
        return 'error'
    else:
        div = first / second
        return div


if __name__ == '__main__':
    divde(5, 0)
    divde(5, 1)
