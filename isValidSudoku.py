def properLen(vector: List) -> int:
    sum = 0
    flag_dot = False
    for e in vector:
        if e != ".":
            sum += 1
        else:
            flag_dot = True

    if flag_dot:
        sum += 1

    return sum


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # # print_board(board)
        # rows
        for row in range(len(board)):
            row_set = set()
            row_len = properLen(board[row])  # no . items
            # print(row_len)
            # print_row(board[row])
            for cell in range(len(board[row])):  # horizontally
                s_cell = board[row][cell]
                row_set.add(s_cell)

            # print(len(row_set))
            if row_len != len(row_set):
                return False

        for column in range(len(board[0])):
            col_set = set()
            col = [row[column] for row in board]
            col_len = properLen(col)
            # print_row(col)
            for cell in range(len(board)):  # vertically
                s_cell = board[cell][column]
                col_set.add(s_cell)

            if col_len != len(col_set):
                return False

        for i in range(3):
            for j in range(3):
                # starting_p = board[3 * i][3 * j]
                selected_b = [
                    row[3 * j : 3 * j + 3] for row in board[3 * i : 3 * i + 3]
                ]
                # selected_b = board[3 * i : 3 * i + 3][3 * j : 3 * j + 3]
                # print_board(selected_b)
                mini_set = set()
                mini_len = properLen(selected_b[0] + selected_b[1] + selected_b[2])

                for k in range(3):
                    for l in range(3):
                        s_cell = selected_b[k][l]
                        mini_set.add(s_cell)

                if len(mini_set) != mini_len:
                    return False

        return True

        # starting point = (3 * row, 3 * col), row = {0, 1, 2}
        # for row in 3: for col in 3:


def print_board(b: List[List]):
    for i in range(len(b)):
        print("[ ", end="")
        for j in range(len(b[i])):
            print(f"{b[i][j]} ", end="")
        print("]\n", end="")


def print_row(l: List):
    for i in range(len(l)):
        print(f"{l[i] }", end="")


def main():
    print("\n" + str(Solution.isValidSudoku(Solution, T2)))


T1 = board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
T2 = board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "1", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

if __name__ == "__main__":
    main()

# Second try

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # sets for columns, rows, and boxes, every is 9
        columns_sets = [set() for _ in range(9)]
        rows_sets = [set() for _ in range(9)]
        boards_sets = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                b = (r // 3) * 3 + c // 3
                if v == ".":
                    continue

                if v in columns_sets[c] or v in rows_sets[r] or v in boards_sets[b]:
                    return False

                columns_sets[c].add(v)
                rows_sets[r].add(v)
                boards_sets[b].add(v)

        return True
