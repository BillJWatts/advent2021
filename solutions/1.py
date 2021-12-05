"""Solution to day 1 problem"""

from config import get_input

with get_input(__file__) as _input:
    values = [int(value) for value in _input.readlines()]

total_values = len(values)

increases = 0
for i, value in enumerate(values):
    if i > 0 and i < total_values - 2:
        A = sum([values[i - 1], value, values[i + 1]])
        B = sum([value, values[i + 1], values[i + 2]])

        if A < B:
            increases += 1


print(increases)
