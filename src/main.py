from console_helper import handle_user_input
from game_engine import TicTacToeGame
from ai_player import AiPlayer
from console_player import ConsolePlayer


def main():
    print('Welcome to TicTacToe game!\n')

    while True:
        print('Choose game format:\n'
              '1 - Human vs AI\n'
              '2 - Human vs Human\n'
              '0 - Exit\n')

        is_choose_game_handled = handle_user_input(
            'Enter format number:',
            {
                '1': play_game_vs_ai,
                '2': play_game_vs_player,
                '0': False
            }
        )

        if is_choose_game_handled is False:
            return

        is_repeat_game_handled = handle_user_input(
            'Do you want to play again? (y/n)',
            {
                'y': True,
                'n': False
            }
        )

        if is_repeat_game_handled is False:
            return


def play_game_vs_ai():
    game = TicTacToeGame({
        'players': [ConsolePlayer(), AiPlayer()],
        'onGameStart': on_game_start,
        'onMoveMade': on_move_made,
        'onBoardChange': on_board_change,
        'onGameEnd': on_game_end
    })
    game.play()


def play_game_vs_player():
    game = TicTacToeGame({
        'players': [ConsolePlayer(), ConsolePlayer()],
        'onGameStart': on_game_start,
        'onMoveMade': on_move_made,
        'onBoardChange': on_board_change,
        'onGameEnd': on_game_end
    })
    game.play()


def on_game_start():
    print('Game started!\n')


def on_move_made(move_data):
    output = 'Player {active_player} goes to cell {row} {col}\n'.format(
        active_player=move_data.player_char.upper(),
        row=move_data.row,
        col=move_data.col)

    print(output)


def on_board_change(board):
    for line in board:
        print(*line)

    print()


def on_game_end(winner_char):
    print('Player {winner} won!\n'.format(winner=winner_char.upper()))
