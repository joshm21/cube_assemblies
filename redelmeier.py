# https://math.stackexchange.com/a/4457462

# The basic idea in Redelmeier is to carefully manage the set of squares that can be added to the polyomino - the so-called "untried set". The algorithm is basically this:

# Start with the empty polyomino and the untried set containing only the origin, [(0,0)]

# Perform the following recursively:

# While the untried set is not empty, remove a square from it and add to the current polyomino
# Count this polyomino - this is the only time it will be generated in the algorithm (one can also print it to a file etc. at this stage).
# Create a copy of the untried set. This is very important that we work with a copy (since this copy is going to be emptied in the subsequent recursive call).
# To this copy add all of the new neighbors of the current polyomino, and then recursively return to 1, with the new polyomino and untried set, unless the current polyomino is already of the requested maximal size.
# After returning from the recursion, remove the new square you've added to the polyomino at stage 1, and proceed to the next element of the untried set.
# The most important part here is how new neighbors are defined. This are cells that are:

# Neighbors of the new square we just added to the polyomino at this stage.
# Are not part of the current polyomino and are not neighbors of the current polyomino (before we added the new square)
# Are not out of the grid (in order to avoid double-counting, the grid only contains the cells (x,y) where y>0 or y=0 and x≥0).
# The algorithm can indeed get "stuck" in the sense that a specific branch of the recursion cannot add more squares to the current polyomnino, but it's not a problem; any polyomino will be counted at some branch. Which branch depends on the order in which elements are sorted in the untried set.

# In your example we only see the current polyomino, not the untried set, so it's hard to understand in which sense we are "stuck". For example, cell 19: it won't be added to the untried set when adding 42 since it's not a new neighbor, but it should already be in the untried set (it was added when 16 was added). If it's not in the untried set in this stage, it means that earlier, in another branch of the recursion, all the polyominoes containing 19 were already counted; now we are counting all the polyominoes not containing 19, so not adding 19 again doesn't mean we lost anything.

# I hope this helps future readers arriving here. I'm also attaching an ad-hoc Python code for computing this; it's sometimes easier to understand from a working code.

import copy

Square = (int, int)
Polyomino = frozenset[Square]

Cube = (int, int, int)
Polycube = frozenset[Cube]
Free_Polycube = frozenset[Polycube]


def precompute_neighbors(max_cubes: int) -> dict:
    search_space = set()
    for x in range(-max_cubes, max_cubes):
        for y in range(max_cubes):
            if y == 0 and x < 0:
                continue
            search_space.add((x, y))
    precomputed = {}
    for x in range(-max_cubes, max_cubes):
        for y in range(max_cubes):
            square = (x, y)
            possible_neighbors = square_neighbors(square)
            neighbors_in_search_space = search_space.intersection(possible_neighbors)
            precomputed[square] = neighbors_in_search_space
    return precomputed


def square_neighbors(sq: Square) -> set[Square]:
    neighbors = set()
    x, y = sq
    neighbors.add((x + 1, y))
    neighbors.add((x - 1, y))
    neighbors.add((x, y + 1))
    neighbors.add((x, y - 1))
    return neighbors


def neighbors(polyomino: Polyomino) -> set[Square]:
    neighbors = set()
    for square in polyomino:
        for neighbor in PRECOMPUTED[square]:
            neighbors.add(neighbor)
    return neighbors


# def neighbors(polyomino: Polyomino) -> set[Square]:
#     neighbors = set()
#     four_neighbor_deltas = ((1, 0), (-1, 0), (0, 1), (0, -1))
#     for x, y in polyomino:
#         for delta_x, delta_y in four_neighbor_deltas:
#             if y + delta_y < 0 or (y + delta_y == 0 and x + delta_x < 0):
#                 continue
#             new_square = (x + delta_x, y + delta_y)
#             neighbors.add(new_square)
#     return neighbors


def redelmeier(n):
    results = [0 for n in range(n + 1)]
    results[0] = 1
    polyomino = []
    untried_set = [(0, 0)]
    redelmeier_recursion(n, results, polyomino, untried_set)
    return results


def redelmeier_recursion(n, counts, polyomino, untried):
    while untried:
        polyomino_neighbors = neighbors(polyomino)

        to_try = untried.pop()
        to_try_neighbors = neighbors([to_try])

        next_node_untried = copy.copy(untried)
        next_node_untried.extend(
            to_try_neighbors.difference(polyomino_neighbors).difference(polyomino)
        )

        next_polyomino = copy.copy(polyomino)
        next_polyomino.append(to_try)
        counts[len(next_polyomino)] += 1
        if len(next_polyomino) < n:
            redelmeier_recursion(n, counts, next_polyomino, next_node_untried)


def generate_polyominoes(max_cubes: int) -> list[Polyomino]:
    results = [[] for n in range(max_cubes)]
    results[0].append(frozenset(((0, 0),)))


PRECOMPUTED = precompute_neighbors(12)

if __name__ == "__main__":
    # print(precompute_neighbors(2))

    # generate_polyominoes(5)

    for n in redelmeier(12):
        print(n)
