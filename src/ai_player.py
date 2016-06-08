from base_player import PlayerBase, PlayerMoveData


class AiPlayer(PlayerBase):
    def get_move(self, board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == '_':
                    return PlayerMoveData(row, col)
