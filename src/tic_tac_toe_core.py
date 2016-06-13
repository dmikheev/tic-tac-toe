from enum import Enum, unique


class TicTacToeCore:
    def __init__(self):
        self._state = State(
            move_status=MoveStatus.x_move,
            board=(
                ['_', '_', '_'],
                ['_', '_', '_'],
                ['_', '_', '_']
            ),
            winner=None
        )

    def get_state(self):
        return self._state

    def make_x_move(self, row, col):
        if self._state.move_status != MoveStatus.x_move:
            raise GameException(
                'X player make_move() called when it\'s not his move')

        self._make_move('x', row, col)

    def make_o_move(self, row, col):
        if self._state.move_status != MoveStatus.o_move:
            raise GameException(
                'O player make_move() called when it\'s not his move')

        self._make_move('o', row, col)

    def _make_move(self, player_char, row, col):
        try:
            cell_value = self._state.board[row][col]
        except IndexError:
            raise MoveException('Made move with wrong row and column')

        if cell_value != '_':
            raise MoveException('Made move to unfree cell')

        self._state.board[row][col] = player_char
        self._update_status()

    def _update_status(self):
        if self._check_for_game_end():
            self._state.move_status = MoveStatus.game_end
            return

        self._state.move_status = get_opposite_player_move_status(
            self._state.move_status)

    def _check_for_game_end(self):
        lines_to_check = (
            ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),

            ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),

            ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
        )

        for line in lines_to_check:
            chars_count = {'x': 0, 'o': 0, '_': 0}

            for cell in line:
                cell_value = self._state.board[cell[0]][cell[1]]
                chars_count[cell_value] += 1

            if chars_count['x'] == 3:
                self._state.winner = 'x'
                return True
            if chars_count['o'] == 3:
                self._state.winner = 'o'
                return True

        is_tie = True
        for line in self._state.board:
            for cell in line:
                if cell == '_':
                    is_tie = False
                    break

        return is_tie


@unique
class MoveStatus(Enum):
    x_move = 1
    o_move = 2
    game_end = 3


class GameException(Exception):
    pass


class MoveException(Exception):
    pass


class State:
    def __init__(self, board, move_status, winner):
        self.board = board
        self.move_status = move_status
        self.winner = winner


def get_opposite_player_move_status(player_move_status):
    if type(player_move_status) is not MoveStatus:
        raise TypeError

    if player_move_status == MoveStatus.x_move:
        return MoveStatus.o_move
    if player_move_status == MoveStatus.o_move:
        return MoveStatus.x_move

    raise ValueError
