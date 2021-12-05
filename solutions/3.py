from types import SimpleNamespace
from typing import List, Tuple
from config import get_input
import numpy as np
from collections import Counter


def get_bits(line: str) -> List[int]:
    """Convert bit string to List[int]"""
    bits = []
    for bit in list(line):
        try:
            bit = int(bit)
            bits.append(bit)
        except ValueError:
            continue
    return bits


def get_most_least_bit(array: np.ndarray) -> Tuple[str, str]:
    bit_count = Counter(array)
    most_bit = max(bit_count, key=bit_count.get)
    least_bit = min(bit_count, key=bit_count.get)

    return (str(most_bit), str(least_bit))


with get_input(__file__) as _input:
    bit_array = np.array(get_bits(next(_input)))
    for line in _input:
        line_array = np.array(get_bits(line))
        bit_array = np.vstack((bit_array, line_array))


bit_array_row_length = bit_array.shape[1]

""" --- PART ONE --- """

gamma: str = ""
epsilon: str = ""

for column_index in range(bit_array_row_length):
    most_bit, least_bit = get_most_least_bit(bit_array[:, column_index])
    gamma += most_bit
    epsilon += least_bit

gamma_value = int(gamma, 2)
epsilon_value = int(epsilon, 2)

print(" --- Part One --- ")
print(f"gamma = {gamma_value}")
print(f"epsilon = {epsilon_value}")
print(f"multiplied = {gamma_value * epsilon_value}\n")


""" --- PART TWO --- """
oxygen_array = np.copy(bit_array)
for column_index in range(bit_array_row_length):
    ox_column = oxygen_array[:, column_index]
    most_bit, least_bit = get_most_least_bit(ox_column)
    if most_bit == least_bit:
        oxygen_array = oxygen_array[ox_column != 0]
    else:
        oxygen_array = oxygen_array[ox_column != int(least_bit)]
    if oxygen_array.shape[0] == 1:
        break

oxygen: str = ""
for bit in oxygen_array[0]:
    oxygen += str(bit)
oxygen_value = int(oxygen, 2)

co2_array = np.copy(bit_array)
for column_index in range(bit_array_row_length):
    co2_column = co2_array[:, column_index]
    most_bit, least_bit = get_most_least_bit(co2_column)
    if most_bit == least_bit:
        co2_array = co2_array[co2_column != 1]
    else:
        co2_array = co2_array[co2_column != int(most_bit)]

    if co2_array.shape[0] == 1:
        break

co2: str = ""
for bit in co2_array[0]:
    co2 += str(bit)
co2_value = int(co2, 2)

print(" --- Part Two --- ")
print(f"oxygen = {oxygen_value}")
print(f"co2 = {co2_value}")
print(f"multiplied = {oxygen_value * co2_value}\n")
