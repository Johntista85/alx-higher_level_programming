#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(a, b, d):
    """Match bytecode provided by Holberton School."""
    if a < b:
        return (d)
    if d > b:
        return (a + b)
    return (a*b - d)

