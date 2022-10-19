def max_gain_sum(m, distances, gains, delta):
    dp = [-1] * m
    dp[0] = gains[0]

    for i in range(1, m):
        d = distances[i]
        g = gains[i]
        nearest_index = i - 1
        nearest = distances[nearest_index]

        # O(m)?
        while d - delta < nearest and nearest_index > 0:
            nearest_index -= 1
            nearest = distances[nearest_index]

        if d - delta < nearest:
            dp[i] = max(dp[i - 1], g)
        else:
            dp[i] = max(dp[i - 1], dp[nearest_index] + g)

    print("Total gain:", dp[m-1])


### TEST ###
m = 5
distances = [0, 1, 2, 3, 4]
gains = [0, 0, 10, 15, 0]
delta = 3

max_gain_sum(m, distances, gains, delta)
