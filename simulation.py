from board import Board
from game_easy import Player
from game_hard import Bot

def main():
    board = Board()
    player = Player()
    bot = Bot()
    while not board.has_winner() and len(board.free) >= 1:
        board = player.make_move(board)
        print("your move:")
        print(board)
        board.free = board.free_positions()
        if len(board.free) < 1:
            print("This is a draw!")
            return
        if not board.has_winner():
            board = bot.make_move(board)
            print("bot's move:")
            board.free = board.free_positions()
            print(board)
    if board.has_winner()[1] == "x":
        print("Congratulations! You won!")
    elif board.has_winner()[1] == "o":
        print("Sorry! You've lost")
    elif len(board.free) == 0:
        print("This is a draw")

main()