from piece import Piece
from dataclasses import dataclass

from orientation import Orientation


@dataclass
class Node:
    xyzs: tuple[tuple[int]]


def generate_pieces(max_cubes: int, max_x: int, max_y=int, max_z=int) -> None:

    # keep track of which orientations already seen to avoid reprocessing
    seen_orientations = set()
    # results stored in list of lists; index n corresponds to pieces with n+1 cubes
    results = [[] for _ in range(max_cubes)]

    # start at origin
    initial_xyzs = ((0, 0, 0),)
    queue = [initial_xyzs]
    while len(queue) > 0:

        xyzs = queue.pop(0)  # process next xyzs in queue
        number_cubes = len(xyzs)

        if number_cubes > max_cubes:
            break  # finish when cubes > max because breadth first search

        piece = Piece.from_xyz(xyzs)

        if piece.normalized in seen_orientations:
            continue  # already seen; skip

        # print(piece)
        seen_orientations.update(piece.orientations)  # add new piece to seen
        results[number_cubes - 1].append(piece.normalized)  # store result

        # generate children
        # loop through cubes, add new cube at neighboring open spaces with x,y,z maxes
        for xyz in xyzs:
            x, y, z = xyz
            neighbors = (
                (x+1, y, z), (x, y+1, z), (x, y, z+1),
                (x-1, y, z), (x, y-1, z), (x, y, z-1)
            )
            for neighbor in neighbors:
                neighbor_x, neighbor_y, neighbor_z = neighbor
                if neighbor in xyzs:
                    continue  # space already taken by another cube
                if neighbor_x > max_x or neighbor_x < -max_x:
                    continue
                if neighbor_y > max_y or neighbor_y < -max_y:
                    continue
                if neighbor_z > max_z or neighbor_z < -max_z:
                    continue
                new_xyz = (*xyzs, neighbor)
                queue.append(new_xyz)

    return results


def print_results(results) -> None:
    for level in range(len(results)):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'{len(results[level])} pieces with {level + 1} cubes:')
        # for orientation in results[level]:
        #     print(f'{orientation}')


def generate_polyomino():
    # https://en.wikipedia.org/wiki/Polyomino#Enumeration_of_polyominoes
    max_cubes = 8
    results = generate_pieces(max_cubes, max_cubes-1, max_cubes-1, max_z=0)
    print_results(results)


def generate_polycube():
    # https://en.wikipedia.org/wiki/Polycube#Enumerating_polycubes
    max_cubes = 6
    results = generate_pieces(max_cubes, max_cubes-1, max_cubes-1, max_cubes-1)
    print_results(results)


def generate_burr():
    results = generate_pieces(max_cubes=6*2*2, max_x=5, max_y=1, max_z=1)
    print_results(results)


def generate_burr_alternate():
    # https://billcutlerpuzzles.com/docs/CA6PB/pieces.html
    # 12 cubes can be included or not, 2 ^ 12 = 4096
    # get all combinations, but check if connected
    # then use Pieces to group like orientations
    # connected_orientations = []
    # for twelve_cube_combo in range(4096):
    #     if twelve_cube_combo in connected_configs
    #         append


if __name__ == '__main__':
    # generate_polyomino()
    # generate_polycube()
    generate_burr()
