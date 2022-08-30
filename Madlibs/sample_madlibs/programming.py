"""
VERY basic Python Project
Madlibs using string concatenation
A passage about programming
"""

def madlib():
    print("\nInput the following to create your madlib passage:")
    adj = input("Adjective: ")
    verb1 = input("First Verb: ")
    verb2 = input("Second Verb: ")
    famous_person = input("A Famous Person: ")

    madlib = (f"\nComputer programming is so exciting! It makes me feel so {adj} all the time because \
I love to {verb1}, stay hydrated, throw on some music and {verb2}, like you are {famous_person}!")

    print(madlib)