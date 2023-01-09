from generate_pieces import generate_pieces, Node
from cube import Cube
from piece import Piece


def get_child_nodes(node):
    x = node.last_cube.x
    y = node.last_cube.y
    last_cubes = []
    last_cubes.append(Cube(x+1, y, 0))
    last_cubes.append(Cube(x, y+1, 0))
    if x > 0:
        last_cubes.append(Cube(x-1, y, 0))
    if y > 0:
        last_cubes.append(Cube(x, y-1, 0))

    new_depth = node.depth + 1
    previous_cubes = tuple(node.piece.cubes)
    child_nodes = []
    for last_cube in last_cubes:
        new_piece = Piece(frozenset([*previous_cubes, last_cube]))
        child_nodes.append(Node(new_depth, new_piece, last_cube))
    # check last_cube not where another already exists
    return tuple(child_nodes)


def main():
    # https://en.wikipedia.org/wiki/Polyomino
    for piece in generate_pieces(1, get_child_nodes):
        # print(piece)
        pass


if __name__ == '__main__':
    main()
