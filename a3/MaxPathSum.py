from copy import deepcopy


def max_path_sum(grid):  # grid represented as 2-d matrix with zero indexing
    n = len(grid)
    OPT = deepcopy(grid)

    for i in range(1, n):  # rows
        for j in range(n):  # columns
            if 0 < j < n - 1:
                OPT[i][j] += max(OPT[i - 1][j - 1], OPT[i - 1][j], OPT[i - 1][j + 1])

            elif j < n - 1:  # j == 0
                OPT[i][j] += max(OPT[i - 1][j], OPT[i - 1][j + 1])

            elif j > 0:  # j == n
                OPT[i][j] += max(OPT[i - 1][j - 1], OPT[i - 1][j])

    print("Max sum:", max(OPT[n - 1]))
    get_path(OPT, n)


def get_path(OPT, n):
    path = [-1] * n

    j = OPT[n - 1].index(max(OPT[n - 1]))
    path[n - 1] = j

    for i in range(n - 2, -1, -1):
        if 0 < j < n - 1:
            j = OPT[i].index(max(OPT[i][j - 1], OPT[i][j], OPT[i][j + 1]))

        elif j > 0:  # j == n
            j = OPT[i].index(max(OPT[i][j - 1], OPT[i][j], OPT[i][j + 1]))

        elif j < n - 1:  # j == 0
            j = OPT[i].index(max(OPT[i][j - 1], OPT[i][j], OPT[i][j + 1]))

        path[i] = j

    print("Path:", path)


def max_path_sum_generic(grid):
    n = len(grid)
    m = len(grid[0])
    dp = deepcopy(grid)

    for row in range(1, n):
        for column in range(m):
            if 0 < column < m - 1:
                dp[row][column] += max(dp[row - 1][column - 1], dp[row - 1][column], dp[row - 1][column + 1])

            elif column > 0:  # column == n
                dp[row][column] += max(dp[row - 1][column - 1], dp[row - 1][column])

            elif column < m - 1:  # column == 0
                dp[row][column] += max(dp[row - 1][column], dp[row - 1][column + 1])

    print("Max sum:", max(dp[n - 1]))
    get_path(dp, n)


### TEST ###
grid0 = ([[10, 10, 2, 0, 20, 4],
          [1, 0, 0, 30, 2, 5],
          [0, 10, 4, 0, 2, 0],
          [1, 0, 2, 20, 0, 4],
          [10, 10, 2, 0, 20, 4],
          [0, 10, 4, 0, 2, 0]])
max_path_sum(grid0)
print()

grid1 = ([[10, 10, 2, 0, 20, 4],
          [1, 0, 0, 30, 2, 5],
          [0, 10, 4, 0, 2, 0],
          [1, 0, 2, 20, 0, 4]])
max_path_sum_generic(grid1)
