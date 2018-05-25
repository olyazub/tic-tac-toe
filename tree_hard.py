from board import Board


class Node:
    def __init__(self, data, sign="x"):
        self.data = data
        self.sign = sign
        self.children = []


class Tree:
    def __init__(self, board):
        self.root = Node(board)

    def fill_tree(self, node):
        import copy
        sign = "x" if node.sign == "o" else "o"
        for el in node.data.free:
            if not node.data.has_winner():
                field1 = copy.deepcopy(node.data.field)
                field1[el[0]][el[1]] = sign
                node1 = Node(Board(field1), sign=sign)
                node.children.append(node1)
                self.fill_tree(node1)

    def get_score(self, node):
        score = node.data.has_winner()
        l = len(node.children)
        if not score:
            if l >= 1:
                if l == 8:
                    return self.get_score(node.children[0]) + self.get_score(node.children[1]) + \
                           self.get_score(node.children[2]) + self.get_score(node.children[3]) + \
                           self.get_score(node.children[4]) + self.get_score(node.children[5]) + \
                           self.get_score(node.children[6]) + self.get_score(node.children[7])
                elif l == 7:
                    return self.get_score(node.children[0]) + self.get_score(node.children[1]) + \
                           self.get_score(node.children[2]) + self.get_score(node.children[3]) + \
                           self.get_score(node.children[4]) + self.get_score(node.children[5]) + \
                           self.get_score(node.children[6])
                elif l == 6:
                    return self.get_score(node.children[0]) + self.get_score(node.children[1]) + \
                           self.get_score(node.children[2]) + self.get_score(node.children[3]) + \
                           self.get_score(node.children[4]) + self.get_score(node.children[5])
                elif l == 5:
                    return self.get_score(node.children[0]) + self.get_score(node.children[1]) + \
                           self.get_score(node.children[2]) + self.get_score(node.children[3]) + \
                           self.get_score(node.children[4])
                elif l == 4:
                    return self.get_score(node.children[0]) + self.get_score(node.children[1]) + \
                           self.get_score(node.children[2]) + self.get_score(node.children[3])
                elif l == 3:
                    return self.get_score(node.children[0]) + self.get_score(node.children[1]) + \
                           self.get_score(node.children[2])
                elif l == 2:
                    return self.get_score(node.children[1]) + self.get_score(node.children[0])
                elif l == 1:
                    return self.get_score(node.children[0])
            else:
                return 0
        elif score[1] == 'o':
            return 1
        elif score[1] == "x":
            return -1


