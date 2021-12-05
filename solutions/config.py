import io
import os
from contextlib import contextmanager
import os

_RESOURCES = "..\\resources\\"


@contextmanager
def get_input(file_path: str) -> io.TextIOWrapper:
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    file_name = file_path.split("\\")[-1]
    input_value = file_name.split(".")[0]
    with open(_RESOURCES + f"{input_value}.txt") as file:
        yield file
