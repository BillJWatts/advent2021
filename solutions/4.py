from typing import List, final

import numpy as np

from config import get_input


def day_four_solution():
    with get_input(__file__) as _input:
        file = _input.read().splitlines()

    draw_values = file.pop(0).split(",")
    game_boards = get_game_boards(file)

    winning_board = None
    winning_draw = ""
    final_board = None
    final_draw = ""
    try:
        for draw in draw_values:
            winning_boards = []
            for i, board in enumerate(game_boards):
                board.mark_number(draw)
                if board.check_win():
                    if len(game_boards) == 1:
                        final_board = board
                        final_draw = draw
                        raise Winner
                    if not winning_draw:
                        winning_draw = draw
                    if not winning_board:
                        winning_board = board
                    winning_boards.append(i)
            for i in sorted(winning_boards, reverse=True):
                del game_boards[i]
    except Winner:
        pass

    winning_unmarked_sum = get_unmarked_sum(winning_board)
    final_unmarked_sum = get_unmarked_sum(final_board)

    print(" --- Part One --- ")
    print(winning_unmarked_sum * int(winning_draw))
    print("\n --- Part Two --- ")
    print(final_unmarked_sum * int(final_draw))


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


def get_unmarked_sum(board: GameBoard) -> int:
    unmarked_sum = 0
    for x, y in [tuple(index) for index in np.argwhere(board.mark_board == 0)]:
        unmarked_sum += int(board.array[x, y])
    return unmarked_sum


day_four_solution()
