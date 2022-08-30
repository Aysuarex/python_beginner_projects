"""
VERY basic Python Project
Madlibs using string concatenation
A passage about hunger games
"""

def madlib():
    print("\nInput the following to create your madlib passage:")
    number = input("Number: ")
    adj1 = input("Adjective: ")
    noun1 = input("First Noun: ")
    noun2 = input("Second Noun: ")
    noun3 = input("Third Noun: ")
    noun4 = input("Fourth Noun: ")
    noun5 = input("Fifth Noun: ")
    plural_noun1 = input("Noun(Plural): ")
    plural_noun2 = input("2nd Noun(Plural): ")
    plural_noun3 = input("3rd Noun(Plural): ")
    verb1 = input("First Verb: ")
    verb2 = input("Second Verb: ")
    sound_important = input("Name of something that sounds important: ")

    madlib = (f"\n{number} seconds. That's how long we're required to {verb1} on our metal circles before \
the sound of a {noun1} releases us. Step off before the {number} seconds is up, and {plural_noun1} blow your \
legs off, {number} seconds to take in the ring of tributes all equidistant from the {sound_important}, a giant \
{adj1} {noun2} shaped like a {noun3} with a curved tail, the mouth of which is at least twenty feet \
high, spilling over with the things that will give us life here in the arena. Food, containers of water, \
{plural_noun2}, medicine, garments, {plural_noun3}. Strewn around the {sound_important} are other supplies, their value \
decreasing the farther they are from the {noun2}. For instance, only a few steps from my feet lies a three-foot \
square of {noun4}. Certainly it could be of some use in a downpour. But there in the mouth, I can see a {noun5} \
that would protect from almost any sort of weather. If I had the guts to go in and {verb2} for it against \
the other twenty-three tributes. Which I have been instructed not to do.")

    print(madlib)