def make_field():
    field = []
    for i in range(3):
        s = [None, None, None]
        field.append(s)
    return field


class Board:
    def __init__(self, field=make_field()):
        self.field = field
        self.free = self.free_positions()

    def free_positions(self):
        free = []
        for i in range(len(self.field)):
            for j in range(len(self.field)):
                if self.field[i][j] is None:
                    free.append([i, j])
        return free

    def has_winner(self):
        for i in range(3):
            if (self.field[i][0] == self.field[i][1] == self.field[i][2]) and self.field[i][0] is not None:
                return [1, self.field[i][0]]
            elif (self.field[0][i] == self.field[1][i] == self.field[2][i]) and self.field[0][i] is not None:
                return [1, self.field[0][i]]
            if ((self.field[0][0] == self.field[1][1] == self.field[2][2]) or
                (self.field[0][2] == self.field[1][1] == self.field[2][0])) and self.field[1][1] is not None:
                return [1, self.field[1][1]]
        return 0

    def move(self, sign):
        import random, copy
        cell = random.choice(self.free)
        field1 = copy.deepcopy(self.field)
        field1[cell[0]][cell[1]] = sign
        self.free.remove(cell)
        return field1

    def __str__(self):
        s = ''
        for i in range(len(self.field)):
            for j in range(len(self.field)):
                if self.field[i][j] is None:
                    s += '*'
                else:
                    s += self.field[i][j]
            s += '\n'
        return s

    def to_str(self):
        lines = []
        s = ''
        for i in range(3):
            for j in range(3):
                if self.field[i][j] is None:
                    s += '*'
                else:
                    s += self.field[i][j]
            lines.append(s)
            s = ''
        return lines


if __name__ == '__main__':
    b = Board()
