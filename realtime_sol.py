"""Real-Time solution function."""
def sudoku(board):

    def cell_pos(matrix, sol):
        row = set(sol[matrix[0]])
        row |= {sol[i][matrix[1]] for i in range(9)}
        k = matrix[0] // 3, matrix[1] // 3

        for i in range(3):
            row |= set(sol[k[0] * 3 + i][k[1] * 3:(k[1] + 1) * 3])

        return set(range(1, 10)) - row

    def is_invalid(row):
        matrix = set(row) - {0}
        for col in matrix:
            if row.count(col) != 1:
                return True
        return False

    sol = []
    empty_pos = []
    for nl, l in enumerate(board):
        try:
            n = list(map(int, l))
        except:
            return
        if len(n) != 9:
            return
        empty_pos += [[nl, i] for i in range(9) if n[i] == 0]
        sol.append(n)

    if nl != 8:
        return

    for row in range(9):
        if is_invalid(sol[row]):
            return

    for col in range(9):
        k = [sol[row][col] for row in range(9)]
        if is_invalid(k):
            return

    for row in range(3):
        for col in range(3):
            matrix = []
            for i in range(3):
                matrix += sol[row * 3 + i][col * 3:(col + 1) * 3]
            if is_invalid(matrix):
                return

    pos = [[] for i in empty_pos]
    cell_row = 0

    while cell_row < len(empty_pos):
        pos[cell_row] = cell_pos(empty_pos[cell_row], sol)
        try:
            while not pos[cell_row]:
                sol[empty_pos[cell_row][0]][empty_pos[cell_row][1]] = 0
                cell_row -= 1
        except:
            return

        sol[empty_pos[cell_row][0]][empty_pos[cell_row][1]] = pos[cell_row].pop()
        cell_row += 1

    return(sol)
