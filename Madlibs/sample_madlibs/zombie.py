"""
VERY basic Python Project
Madlibs using string concatenation
A passage about Zombies
"""

def madlib():
    print("\nInput the following to create your madlib passage:")
    food = input("Food: ")
    colour = input("Colour: ")
    time_of_day = input("Time of Day: ")
    noun = input("Noun: ")
    adj1 = input("First Adjective: ")
    adj2 = input("Second Adjective: ")
    adj3 = input("Third Adjective: ")
    plural_noun = input("A Noun(Plural): ")
    verb_past = input("Verb(Past Tense): ")
    body_part_plural = input("A Body Part: ")

    madlib = (f"\nIt was a {adj1} summer {time_of_day} when we realised that the vaccine to stop \
the spread of the disease did not work. Instead, it produced ZOMBIES!!! They were thirsty for \
{body_part_plural} and the streets were lined with these monsters holding {plural_noun} in their hands. \
Their eyes were {colour} with hunger as they {verb_past} around the city looking for {food}. \
They were {adj2}and {adj3}, unknowing how to act in thus human world... except eat {body_part_plural}!!! \
That was their sole mission and they were dedicated towards achieving it for the sake of {noun}.")

    print(madlib)