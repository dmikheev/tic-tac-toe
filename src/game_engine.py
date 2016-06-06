from random import shuffle

from tic_tac_toe_core import TicTacToeCore, MoveStatus


class TicTacToeGame:
    def __init__(self, options):
        self._core = TicTacToeCore()

        players = options.get('players')

        if (not isinstance(players, list)) or (len(players) != 2):
            raise TypeError('You must specify list of two players')

        players_copy = players.copy()
        shuffle(players_copy)

        self.players = {
            'x': players_copy[0],
            'o': players_copy[1]
        }

        self.gameStartHandler = options.get('onGameStart')
        self.moveMadeHandler = options.get('onMoveMade')
        self.boardChangeHandler = options.get('onBoardChange')
        self.gameEndHandler = options.get('onGameEnd')

    def play(self):
        call_handler(self.gameStartHandler)

        for player_char in self.players:
            call_handler(self.players[player_char], player_char)

        call_handler(self.boardChangeHandler, self._core.get_state().board)

        while True:
            state = self._core.get_state()
            if state.move_status == MoveStatus.game_end:
                call_handler(self.gameEndHandler, state.winner)
                return
            else:
                active_player_char = {
                    MoveStatus.x_move: 'x',
                    MoveStatus.o_move: 'o'
                }[state.move_status]
                active_player = self.players[active_player_char]
                player_move_data = active_player.get_move(state.board)

                core_make_move_func = {
                    'x': self._core.make_x_move,
                    'o': self._core.make_o_move
                }[active_player_char]
                core_make_move_func(player_move_data.row, player_move_data.col)

                call_handler(self.moveMadeHandler,
                             MoveData(active_player_char,
                                      player_move_data.row,
                                      player_move_data.col))
                call_handler(self.boardChangeHandler, state.board)


class MoveData:
    def __init__(self, player_char, row, col):
        self.player_char = player_char
        self.row = row
        self.col = col


def call_handler(handler, *params):
    if callable(handler):
        handler(*params)
