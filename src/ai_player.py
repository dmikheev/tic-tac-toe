import copy

from base_player import PlayerBase, PlayerMoveData


class AiPlayer(PlayerBase):
    def __init__(self):
        self.player_char = None

    def get_move(self, board):
        if board[1][1] == '_':
            return PlayerMoveData(1, 1)

        board_list = list(board)

        best_move = self.get_best_move(board_list, self.player_char)
        return best_move.move_data

    def get_best_move(self, board, move_player_char):
        best_move = None

        if move_player_char == self.player_char:
            is_new_move_better = is_new_move_better_for_player
        else:
            is_new_move_better = is_new_move_better_for_enemy

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == '_':
                    move_data = PlayerMoveData(row, col)
                    score = self.get_move_score(board, move_data,
                                                move_player_char)
                    ai_move_data = AiMoveData(score, move_data)

                    if (best_move is None) or (
                            is_new_move_better(best_move, ai_move_data)):
                        best_move = ai_move_data

        return best_move

    def get_move_score(self, board_list, move_data, move_char):
        new_board_list = copy.deepcopy(board_list)
        new_board_list[move_data.row][move_data.col] = move_char
        win_char = get_win_char(new_board_list)

        if win_char:
            if win_char == self.player_char:
                return 100
            else:
                return -100

        is_tie = True
        for line in new_board_list:
            for cell in line:
                if cell == '_':
                    is_tie = False
                    break

        if is_tie:
            return 0

        next_move = self.get_best_move(new_board_list,
                                       get_opposite_player_char(move_char))

        if next_move.score > 0:
            next_move.score -= 1
        elif next_move.score < 0:
            next_move.score += 1

        return next_move.score

    def on_game_started(self, player_char):
        self.player_char = player_char


win_lines = (
    ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),
    ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2))
)


def get_win_char(board_list):
    for line in win_lines:
        first_cell = cell = line[0]
        first_cell_char = board_list[first_cell[0]][first_cell[1]]

        if first_cell_char == '_':
            continue

        is_win_line = True

        for i in range(1, len(line)):
            cell = line[i]
            cell_value = board_list[cell[0]][cell[1]]
            if cell_value != first_cell_char:
                is_win_line = False
                break

        if is_win_line:
            return first_cell_char

    return None


def is_new_move_better_for_player(old_move, new_move):
    return new_move.score > old_move.score


def is_new_move_better_for_enemy(old_move, new_move):
    return new_move.score < old_move.score


def get_opposite_player_char(player_char):
    if player_char == 'x':
        return 'o'

    if player_char == 'o':
        return 'x'

    raise ValueError('get_opposite_player_char() called with wrong argument')


class AiMoveData:
    def __init__(self, score, move_data):
        self.score = score
        self.move_data = move_data
