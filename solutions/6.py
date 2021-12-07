from config import get_input


with get_input(__file__) as _input:
    values = next(_input).split(",")

print(values)
