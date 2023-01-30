class Sudoku:
    def __init__(self, solved_state):
        self.solved_state = solved_state

    def check_if_solved(self):
        rows_solved = []
        columns_solved = []
        boxes_solved = []

        for row in self.solved_state:
            rows_solved.append(self._check_if_numbers_are_present(row))

        current_column = 0

        for column in zip(*self.solved_state):
            columns_solved.append(self._check_if_numbers_are_present(column))

        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                box = (
                    self.solved_state[row][column:column + 3] +
                    self.solved_state[row + 1][column:column + 3] +
                    self.solved_state[row + 2][column:column + 3]
                )
                boxes_solved.append(self._check_if_numbers_are_present(box))

        return all(rows_solved) and all(columns_solved) and all(boxes_solved)

    def _check_if_numbers_are_present(self, numbers):
        expected_numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

        return expected_numbers == set(numbers)


data = [
    [1, 8, 2, 5, 4, 3, 6, 9, 7],
    [9, 6, 5, 1, 7, 8, 3, 4, 2],
    [7, 4, 3, 9, 6, 2, 8, 1, 5],
    [3, 7, 4, 8, 9, 6, 5, 2, 1],
    [6, 2, 8, 4, 5, 1, 7, 3, 9],
    [5, 1, 9, 2, 3, 7, 4, 6, 8],
    [2, 9, 7, 6, 8, 4, 1, 5, 3],
    [4, 3, 1, 7, 2, 5, 9, 8, 6],
    [8, 5, 6, 3, 1, 9, 2, 7, 4]
]
sudoku = Sudoku(data)
print('Is solved', sudoku.check_if_solved())

row_issue = [
    [0, 8, 2, 5, 4, 3, 6, 9, 7],
    [9, 6, 5, 1, 7, 8, 3, 4, 2],
    [7, 4, 3, 9, 6, 2, 8, 1, 5],
    [3, 7, 4, 8, 9, 6, 5, 2, 1],
    [6, 2, 8, 4, 5, 1, 7, 3, 9],
    [5, 1, 9, 2, 3, 7, 4, 6, 8],
    [2, 9, 7, 6, 8, 4, 1, 5, 3],
    [4, 3, 1, 7, 2, 5, 9, 8, 6],
    [8, 5, 6, 3, 1, 9, 2, 7, 4]
]
sudoku = Sudoku(row_issue)
print('Is solved', sudoku.check_if_solved())

column_issue = [
    [1, 8, 2, 5, 4, 3, 6, 9, 7],
    [9, 6, 5, 1, 7, 8, 3, 4, 2],
    [7, 4, 3, 9, 6, 2, 8, 1, 5],
    [3, 7, 4, 8, 9, 6, 5, 2, 1],
    [6, 2, 8, 4, 5, 1, 7, 3, 9],
    [5, 1, 9, 2, 3, 7, 4, 6, 8],
    [0, 9, 7, 6, 8, 4, 1, 5, 3],
    [0, 3, 1, 7, 2, 5, 9, 8, 6],
    [8, 5, 6, 3, 1, 9, 2, 7, 4]
]
sudoku = Sudoku(row_issue)
print('Is solved', sudoku.check_if_solved())


box_issue = [
    [1, 2, 3, 5, 4, 3, 6, 9, 7],
    [9, 6, 4, 1, 7, 8, 3, 4, 2],
    [7, 4, 3, 9, 6, 2, 8, 1, 5],
    [3, 7, 4, 8, 9, 6, 5, 2, 1],
    [6, 2, 8, 4, 5, 1, 7, 3, 9],
    [5, 1, 9, 2, 3, 7, 4, 6, 8],
    [0, 9, 7, 6, 8, 4, 1, 5, 3],
    [0, 3, 1, 7, 2, 5, 9, 8, 6],
    [8, 5, 6, 3, 1, 9, 2, 7, 4]
]
sudoku = Sudoku(row_issue)
print('Is solved', sudoku.check_if_solved())
