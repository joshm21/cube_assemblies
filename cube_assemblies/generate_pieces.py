from piece import Piece
from orientation import Orientation
from cube import Cube
from dataclasses import dataclass


@dataclass
class Node:
    depth: int
    piece: Piece
    last_cube: Cube


def generate_pieces(max_depth: int, x_max: int, y_max: int, z_max: int) -> set['Piece']:

    def init_queue():
        initial_cube = Cube(0, 0, 0)
        initial_piece = Piece.from_xyz((0, 0, 0))
        initial_node = Node(0, initial_piece, initial_cube)
        queue = [initial_node]
        return queue

    def get_child_nodes() -> tuple[Node]:
        new_depth = current_node.depth + 1
        previous_cubes = tuple(current_node.piece.initial_orientation.cubes)

        last_cube_neighbors = current_node.last_cube.get_neighbors()
        for cube in last_cube_neighbors:
            if not 0 <= cube.x < x_max:
                continue

        child_nodes = []
        for last_cube in new_last_cubes:
            new_piece = Piece(Orientation((*previous_cubes, last_cube)))
            child_nodes.append(Node(new_depth, new_piece, last_cube))
            # check last_cube not where another already exists
        return tuple(child_nodes)

    seen_pieces = set()
    seen_orientations = set()
    queue = init_queue()

    while len(queue) > 0:

        current_node = queue.pop(0)
        seen_pieces.add(current_node.piece)
        seen_orientations.update(current_node.piece.orientations)
        if current_node.depth == max_depth:
            break

        for child_node in get_child_nodes():
            if child_node.piece.initial_orientation in seen_orientations:
                continue
            queue.append(child_node)

            # print(f'New Piece Found: {child_node.piece}')
            # print('Seen Pieces')
            # for piece in seen_pieces:
            #     print(piece)
            # print('Seen Orientations')
            # for piece in seen_orientations:
            #     print(piece)

    return seen_pieces
