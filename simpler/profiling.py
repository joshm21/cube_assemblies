import cProfile
import pstats

import generate

if __name__ == "__main__":
    prof = cProfile.Profile()
    prof.enable()
    print(len(generate.generate_polyominos(5)))
    prof.disable()
    stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
    stats.print_stats(10)
