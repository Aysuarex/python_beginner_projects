import random
from sample_madlibs import code, hp, hungergames, programming, ui, zombie

"""
selects a random madlib module from the `sample_madlibs` package
"""

if __name__ == "__main__":
    m = random.choice([code, hp, hungergames, programming, ui, zombie])
    m.madlib()