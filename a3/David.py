# returns a list of tuples or a tuple. The latter if charging station. The first element in every tuple is how long a path to the finish from there is, and the second is how much distance there is on that path till the next charging station
def DAVID(start, charge_left, d, finish, vprime, visited_so_far):
    answers = []
    if start in vprime:
        charge_left = d

    if start.potentials is not empty:
        return start.potentials
    for all adjacent vertices x not in visited_so_far:
        if x is t:
            if w_xt <= charge_left:
                return [[w_tstart, w_tstart]]
        else:
            start.potentials = FUNCTION(x, charge_left - w_tstart, d, finish, vprime, [visited_so_far + start])
            for all tuples in start.potentials such that tuple[1] <= charge_left:
                append
                to
                answers

    if start in vprime:
        for all items in answers,
            return the
            one
            such
            that
            tuple[0] is smallest.
    else
        return answers