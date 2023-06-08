#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    c = 10
    b = 5

    print("{} + {} = {}".format(c, b, add(c, b)))
    print("{} - {} = {}".format(c, b, sub(c, b)))
    print("{} * {} = {}".format(c, b, mul(c, b)))
    print("{} / {} = {}".format(c, b, div(c, b)))
