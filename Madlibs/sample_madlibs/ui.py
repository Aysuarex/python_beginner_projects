"""
VERY basic Python Project
Madlibs using string concatenation
A passage about Unibadan
"""
def madlib():
    print("\nInput the following to create your madlib passage:")
    adj1 = input("An Adjective: ")
    adj2 = input("2nd Adjective: ")
    adj3 = input("3rd Adjective: ")
    adj4 = input("4th Adjective: ")
    adj5 = input("5th Adjective: ")
    adj6 = input("6th Adjective: ")
    adj7 = input("7th Adjective: ")
    adj8 = input("8th Adjective: ")
    noun = input("Noun: ")
    plural_noun = input("Noun(plural): ")
    pronoun = input("Second Person Pronoun: ")
    company = input("A company or Org.: ")

    madlib = (f"\nThe great University of Ibadan, popularly known as Unibadan or UI is a citadel of learning. \
A {adj1} giant amidst {adj2} tertiary institutions in Nigeria and Africa. Not only is the {adj3} Unibadan the first \
University in Nigeria, UI prides {pronoun}self as the best University in Nigeria, which is also consistent with {adj4} \
reports derived from research by {company}. The serene environment is not just spacious, but also {adj5} and conducive \
enough for {adj6} students from all {plural_noun} of life who require some {adj7} education in a {adj8} {noun}.")

    print(madlib)