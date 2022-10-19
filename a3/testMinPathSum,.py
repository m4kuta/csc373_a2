from MinPathSum import *


inf = float('inf')
V = [0, 1, 2, 3, 4, 5]
V_charge = [0, 3, 4, 5]
E = [[000, 200, 300, 400, inf, inf],
     [inf, 000, 200, 100, inf, inf],
     [inf, inf, 000, inf, inf, 250],
     [inf, inf, inf, 000, 200, inf],
     [inf, inf, 100, inf, 000, 400],
     [inf, inf, inf, inf, inf, 000]]
s = 0
t = 5
d = 400

min_path_sum(V, V_charge, E, s, t, d)