"""
VERY basic Python Project
Madlibs using string concatenation
A passage about Harry Potter
"""

def madlib():
    print("\nInput the following to create your madlib passage:")
    adj1 = input("First Adjective: ")
    adj2 = input("Second Adjective: ")
    adj3 = input("Third Adjective: ")
    adj4 = input("Fourth Adjective: ")
    verb = input("Verb: ")
    verb_past1 = input("Verb(Past Tense): ")
    verb_past2 = input("2nd Verb(Past Tense): ")
    noun1 = input("First Noun: ")
    noun2 = input("Second Noun: ")
    noun3 = input("Third Noun: ")
    noun4 = input("Fourth Noun: ")
    noun5 = input("Fifth Noun: ")
    noun6 = input("Sixth Noun: ")
    plural_noun = input("Noun(Plural): ")
    spell1 = input("First Spell: ")
    spell2 = input("Second Spell: ")
    body_part1 = input("A Body part: ")
    body_part2 = input("2nd Body part: ")

    madlib = (f"\nA {adj1} glow burst suddenly across the enchanted sky above them as an edge of \
dazzling sun appeared over the sill of the nearest {noun1}. The light hit both of their {body_part1} \
at the same time, so that Voldemort's was suddenly a flaming {noun2}. Harry Potter heard the high voice \
shriek as he too {verb_past1} his best hope to the heavens, pointing Draco's {noun3}:\n\
\"{spell1}!\"\n\
\"{spell2}!\"\n\
The bang was like a cannon blast, and the {adj2} flames that erupted between them, \
at the dead centre of the circle they had been threading, marked the point where the \
{plural_noun} collided. Harry saw Voldemort's {adj3} jet meet his own spell, saw the Elder Wand \
fly high, dark against the sunrise, spinning across the enchanted ceiling like the \
head of Nagini, spinning through the air toward the master it would not {verb}, who had \
come to take full posession of it as well. And Harry, with the unerring skill of a Seeker, \
caught the {noun4} in his free hand as Voldemort fell backward, arms splayed, the slit pupils \
of the {adj4} {body_part2} rolling upward. Tom Riddle hit the floor with a mundane finality, his body \
feeble and shrunken, the white hands empty, the snakelike face vacant and unknowing. Voldemort \
was dead, {verb_past2} by his own rebounding {noun5}, and Harry stood with the two wands in his hands, \
staring down at his enemy's {noun6}.")

    print(madlib)