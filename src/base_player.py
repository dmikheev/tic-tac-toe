class PlayerBase:
    def get_move(self, board):
        raise NotImplementedError()

    def on_game_started(self, player_char):
        pass


class PlayerMoveData:
    def __init__(self, row, col):
        self.row = row
        self.col = col
