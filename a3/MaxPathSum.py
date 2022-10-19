import copy


def max_path_sum(grid):
    n = len(grid)
    dp = copy.deepcopy(grid)

    for row in range(1, n):
        for column in range(n):
            if 0 < column < n - 1:
                dp[row][column] += max(dp[row - 1][column - 1], dp[row - 1][column], dp[row - 1][column + 1])

            elif column > 0:  # column == n
                dp[row][column] += max(dp[row - 1][column - 1], dp[row - 1][column])

            elif column < n - 1:  # column == 0
                dp[row][column] += max(dp[row - 1][column], dp[row - 1][column + 1])

    print("Max sum:", max(dp[n - 1]))
    get_path(dp, n)


def get_path(dp, n):
    path = [-1] * n

    column = dp[n - 1].index(max(dp[n - 1]))
    path[n - 1] = column

    for row in range(n - 2, -1, -1):
        if 0 < column < n - 1:
            column = dp[row].index(max(dp[row][column - 1], dp[row][column], dp[row][column + 1]))

        elif column > 0:  # column == n
            column = dp[row].index(max(dp[row][column - 1], dp[row][column], dp[row][column + 1]))

        elif column < n - 1:  # column == 0
            column = dp[row].index(max(dp[row][column - 1], dp[row][column], dp[row][column + 1]))

        path[row] = column

    print("Path:", path)


def max_path_sum_generic(grid):
    n = len(grid)
    m = len(grid[0])
    dp = copy.deepcopy(grid)

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