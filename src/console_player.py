from base_player import PlayerBase, PlayerMoveData


class ConsolePlayer(PlayerBase):
    def get_move(self, board):
        print('Enter your move cell (row and column separated by space):')

        # TODO check input
        input_str = input()
        print()

        coords = tuple(map(int, input_str.split()))
        return PlayerMoveData(coords[0], coords[1])

    def on_game_started(self, player_char):
        pass
