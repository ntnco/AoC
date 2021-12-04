from aoc_get import get_input


inp = get_input()
lines = inp.splitlines()

picks = [int(num) for num in lines[0].split(',')]
grids = inp.split('\n\n')[1:]


class board:
    def __init__(self, num_grid):
        nums = [int(x) for x in num_grid.split()]
        self.nums = nums
        self.picked = [1 for num in nums]
        self.dead = False # don't check dead board in part 2

    def add_num(self, n):
        if n in self.nums:
            i = self.nums.index(n)
            self.picked[i] = 0
        return n in self.nums

    def final_score(self, p):
        total = 0
        for i in range(len(self.picked)):
            total += self.picked[i] * self.nums[i]
        return total * p

    def check_win(self):
        for i in range(5):
            j = 0
            while self.picked[i * 5 + j] == 0:
                j += 1
                if j == 5:
                    return True
        for i in range(5):
            j = 0
            while self.picked[j * 5 + i] == 0:
                j += 1
                if j == 5:
                    return True
        return False

# part 1
boards = []
for grid in grids:
    boards.append(board(grid))

def get_first_board(boards, picks):
    for n in picks:
        for board in boards:
            if board.add_num(n):
                if board.check_win():
                    return board.final_score(n)
print(get_first_board(boards, picks))


# part 2: reinitialize boards
boards = []
for grid in grids:
    boards.append(board(grid))

def get_last_board(picks, boards):
    num_alive = len(boards)

    for n in picks:
        for i in range(len(boards)):
            board = boards[i]
            if not board.dead and board.add_num(n):
                if board.check_win():
                    board.dead = True
                    num_alive -= 1
                    if num_alive == 0:
                        return board.final_score(n)

print(get_last_board(picks, boards))
