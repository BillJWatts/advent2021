from typing import List
from config import get_input
import numpy as np


def day_four_solution():
    with get_input(__file__) as _input:
        file = _input.read().splitlines()

    draw_values = file.pop(0).split(",")
    game_boards = get_game_boards(file)

    winning_board = None
    final_draw = ""
    try:
        for draw in draw_values:
            for board in game_boards:
                board.mark_number(draw)
                if board.check_win():
                    final_draw = draw
                    winning_board = board
                    raise Winner
    except Winner:
        pass

    unmarked_sum = 0
    for x, y in [tuple(index) for index in np.argwhere(winning_board.mark_board == 0)]:
        unmarked_sum += int(winning_board.array[x, y])

    print(" --- Part One --- ")
    print(unmarked_sum * int(final_draw))


class GameBoard:
    def __init__(self, array) -> None:
        self.array = array
        self.mark_board = np.zeros(self.array.shape)

    def mark_number(self, number: str):
        indexes = [tuple(index) for index in np.argwhere(self.array == number)]
        for x, y in indexes:
            self.mark_board[x, y] = 1

    def check_win(self) -> bool:
        if 1 in self.mark_board[0, :] or 1 in self.mark_board[:, 0]:
            for i in range(5):
                if (sum(self.mark_board[i, :]) == 5) or (sum(self.mark_board[:, i]) == 5):
                    return True
        return False


class Winner(Exception):
    pass


def get_game_boards(file) -> List[GameBoard]:
    game_boards = []
    temp_game_board = []
    for line in file:
        if line:
            temp_game_board.append(line.split())
        if len(temp_game_board) == 5:
            board_array = np.array(temp_game_board)
            game_boards.append(GameBoard(board_array))
            temp_game_board = []
    return game_boards


day_four_solution()
