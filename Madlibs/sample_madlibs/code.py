"""
VERY basic Python Project
Madlibs using string concatenation
A passage about code
"""

def madlib():
    print("\nInput the following to create your madlib passage:")
    name = input("Your name: ")
    noun1 = input("First Noun: ")
    noun2 = input("Second Noun: ")
    plural_noun1 = input("First Plural Noun: ")
    plural_noun2 = input("Second Plural Noun: ")
    adj1 = input("First Adjective: ")
    adj2 = input("Second Adjective: ")
    adj3 = input("Third Adjective: ")
    adj4 = input("Fourth Adjective: ")
    adj5 = input("Fifth Adjective: ")
    verb = input("Verb: ")
    body_part = input("A Body Part: ")

    madlib = (f"\nI love computer programming because it's {adj1}! The journey to becoming a good \
programmer starts with hope in your mind and a dream in your {body_part}. Through blood, sweat \
and {plural_noun1}, hopefully it never ends. Yes, once you learn to {verb}, it becomes a \
part of your life identity and you can become a super {adj2} hacker. Knowledge of programming \
lets you take control of your {noun1}. You can create your own personal {plural_noun2}, anything \
from developing {adj3} software to analyzing data and making predictions about the {noun2}. You \
can maybe even recreate Jarvis and make him extra {adj4}. {name}, I hope you'll start your {adj5} journey \
by coding daily, because consistency beats speed💪!")

    print(madlib)