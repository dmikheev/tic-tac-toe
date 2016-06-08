import re

from base_player import PlayerBase, PlayerMoveData


class ConsolePlayer(PlayerBase):
    input_re = re.compile(r'^([0-2])\s+([0-2])$')

    def get_move(self, board):
        print('Enter your move cell '
              '(row and column (from 0 to 2) separated by space):')

        match = None
        while True:
            input_str = input()

            match = self.input_re.match(input_str)
            if match:
                break

            print('Unrecognized input. Please repeat:')

        row = int(match.group(1))
        col = int(match.group(2))

        return PlayerMoveData(row, col)

    def on_game_started(self, player_char):
        pass
