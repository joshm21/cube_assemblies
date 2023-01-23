import numpy as np
import orientation as Ort

def generate_pieces(bounding_box: Ort.Orientation, ):



# def generate_by_adding_cubes(
#     max_cubes: int,
#     bounding_box: Ort.Orientation,
#     get_orientations: callable,
#     get_children: callable,
# ) -> set[Ort.Orientation]:

#     seen = set()
#     queue = [bounding_box]
#     while queue:
#         current = queue.pop(0)
#         if Ort.number_of_cubes(current) > max_cubes:
#             break
#         if Ort.to_tuples(current) in seen:
#             continue
#         for ort in get_orientations(current):
#             seen.add(Ort.to_tuples(ort))
#         queue.extend(get_children(current, bounding_box))
#     return seen


# def generate_polyominos(max_cubes: int) -> set[Ort.Orientation]:
#     max_x = max_cubes
#     max_y = math.ceil(max_cubes / 2)
#     bounding_box = np.zeros((max_x, max_y, 1), dtype=np.bool_)
#     return generate_by_adding_cubes(
#         max_cubes,
#         bounding_box,
#         Ort.get_polyomino_orientations,
#         Ort.get_polyomino_children,
#     )


def main():
    pass


if __name__ == "__main__":
    main()
