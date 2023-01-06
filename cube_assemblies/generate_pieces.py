from piece import Piece
from cube import Cube
from dataclasses import dataclass


@dataclass
class Node:
    depth: int
    piece: Piece
    last_cube: Cube


def generate_pieces(max_depth: int, get_child_nodes: callable) -> set['Piece']:
    seen_pieces = set()
    seen_orientations = set()

    initial_cube = Cube(0, 0, 0)
    initial_node = Node(0, Piece(frozenset([initial_cube])), initial_cube)
    queue = [initial_node]

    while len(queue) > 0:
        current_node = queue.pop(0)
        child_nodes = get_child_nodes(current_node)
        for child_node in child_nodes:
            if child_node.depth > max_depth:
                break
            if child_node.piece in seen_orientations:
                continue
            queue.append(child_node)
            seen_pieces.add(child_node.piece)
            seen_orientations.add(
                child_node.piece.get_24_positive_orientations())
    return seen_pieces
