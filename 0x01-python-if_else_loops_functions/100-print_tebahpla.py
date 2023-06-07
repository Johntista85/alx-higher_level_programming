#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in reverse order alternating upper- and lower-case."""
i = 0
for c in range(ord('z'), ord('A') - 1, -1):
    print("{}".format(chr(c)), end="")
    i = 32 if i == 0 else 0
