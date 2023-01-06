from cube_assemblies.cube import Cube


# Node
#

# initial_node, func_find_children, func_validate_child

class Node:

    def __init__(self) -> None:
        pass


def main():
    """
    Start with cube at 0,0,0
    Find adjacent cubes with x,y,z >= 0
    For each adjacent cube
        Create new piece including previous cubes and newly found adjacent cube
        Check if new piece is unique by checking seen orientations; if new
            dd piece orientations to seen orientations
            add piece to piece list
    """
    pass


def find_adjacent_positive_cubes(cube):
    pass


if __name__ == '__main__':
    main()
