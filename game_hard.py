from board import Board
from tree_hard import Tree

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
        tree = Tree(brd)
        tree.fill_tree(tree.root)
        max, index = tree.get_score(tree.root.children[0]), 0
        k = tree.root.children
        brd = k[0]
        for a in k:
            score = tree.get_score(a)
            if score > max:
                max = score
                brd = a
        board = brd.data
        board.free = board.free_positions()
        return board
