from config import get_input

with get_input(__file__) as _input:
    commands = [tuple(com.split()) for com in _input.readlines()]


""" --- PART ONE --- """
horizontal_pos: int = 0
vertical_pos: int = 0

for direction, magnitude in commands:
    if direction == "forward":
        horizontal_pos += int(magnitude)

    elif direction == "up":
        vertical_pos -= int(magnitude)

    elif direction == "down":
        vertical_pos += int(magnitude)

print(" --- PART ONE ---")
print(f"Horizontal pos: {horizontal_pos}")
print(f"Vertical pos: {vertical_pos}")
print(f"Multiplied: {horizontal_pos * vertical_pos}")


""" --- PART TWO --- """
horizontal_pos: int = 0
vertical_pos: int = 0
aim: int = 0

for direction, magnitude in commands:
    if direction == "forward":
        horizontal_pos += int(magnitude)
        vertical_pos += int(magnitude) * aim

    elif direction == "up":
        aim -= int(magnitude)

    elif direction == "down":
        aim += int(magnitude)

print(" --- PART TWO ---")
print(f"Horizontal pos: {horizontal_pos}")
print(f"Vertical pos: {vertical_pos}")
print(f"Multiplied: {horizontal_pos * vertical_pos}")
