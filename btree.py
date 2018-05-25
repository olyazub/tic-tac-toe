from board import Board
from bstnode import BSTNode



class Btree:
    def __init__(self, board):
        self.root = BSTNode(board)
        #print(self.root.data)
    def fill_tree(self, node):
        try:
            if not node.data.has_winner():
                self.add_left_child(node)
                self.add_right_child(node)
                self.fill_tree(node.left)
                self.fill_tree(node.right)
        except IndexError:
            return
    def add_left_child(self, node1):
        sign = "x" if node1.sign == "o" else "o"
        brd1 = Board(node1.data.move(sign))
        left = BSTNode(brd1)
        left.sign = sign
        node1.left = left
    def add_right_child(self, node1):
        sign = "x" if node1.sign == "o" else "o"
        brd1 = Board(node1.data.move(sign))
        right = BSTNode(brd1)
        right.sign = sign
        node1.right = right

    def get_score(self, node):
        score = node.data.has_winner()
        if not score:
           if node.right:
               return self.get_score(node.right) + self.get_score(node.left)
           else:
               return 0
        elif score[1] == 'o':
            return 1
        else:
            return -1

    def __str__(self):
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                k = node.data.to_str()
                for i in range(3):
                    s += "| " * level
                    s += k[i] + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self.root, 0)


if __name__ == "__main__":
    brd = Board()
    brd.move("x")
    tree = Btree(brd)
    print(tree)
    tree.fill_tree(tree.root)
    s = tree.get_score(tree.root.left)
    s1 = tree.get_score(tree.root.right)
    print(tree)
    print(s)
    print(s1)



