from base_player import PlayerBase


class AiPlayer(PlayerBase):
    def get_move(self, board):
        raise NotImplementedError()
