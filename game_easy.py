from board import Board
from btree import  Btree


class Player:
    def input_prompt(self):
        while True:
            inp = input("Please enter number of row and column, separated by space: ")
            try:
                row, col = int(inp.split(' ')[0]) -1 , int(inp.split(' ')[1]) -1
            except (ValueError, IndexError):
                print("Please enter valid numbers")
                continue
            if row >= 0 and row <=2 and col >=0 and col <= 2:
                return row,col
            else:
                print("Please enter valid numbers from 1 to 3")
                continue

    def make_move(self, board):
        while True:
            row,col = self.input_prompt()
            if board.field[row][col] is None:
                board.field[row][col] = "x"
                board.free.remove([row,col])
                return board
            else:
                print("Sorry, but this place is taken!")
                continue

class Bot:
    def make_move(self, board):
        from copy import deepcopy
        brd = Board(deepcopy(board.field))
        tree = Btree(brd)
        tree.fill_tree(tree.root)
        board = tree.root.left.data if tree.get_score(tree.root.left) > tree.get_score(tree.root.right) else tree.root.right.data
        board.free = board.free_positions()
        return board


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


if __name__ == "__main__":
    main()