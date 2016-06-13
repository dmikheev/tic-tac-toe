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
        'on_game_start': on_game_start,
        'on_move_made': on_move_made,
        'on_board_change': on_board_change,
        'on_game_end': on_game_end,
        'on_move_exception': on_move_exception
    })
    game.play()


def play_game_vs_player():
    game = TicTacToeGame({
        'players': [ConsolePlayer(), ConsolePlayer()],
        'on_game_start': on_game_start,
        'on_move_made': on_move_made,
        'on_board_change': on_board_change,
        'on_game_end': on_game_end,
        'on_move_exception': on_move_exception
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
    if winner_char is None:
        print('It\'s a tie!')
    else:
        print('Player {winner} won!\n'.format(winner=winner_char.upper()))


def on_move_exception(ex):
    print(ex, end='\n')
