# Mad Libs Variables
creature = input("Name a creature:  ")
adj1 = input("Enter an adjectve:  ")
adj2 = input("Enter another adjectve:  ")
noun1 = input("A Noun Please:  ")
noun2 = input("Another Noun Please: ")
name = input("Give me a name:  ")
verb = input("Last one! Give me a verb: ")


# The Story
print(

    "Now and again, a bellicose " + creature + " shows up on my " + adj1 + " doorstep. He's comely and sagacious, but he eats at my " + adj2 + " " + noun1 + ". I've tried " + creature + " repellent to no avail. " +
    noun2.title() + "s almighty, I hoped it wouldn't come to this! It's time to call " + name.title() +
    ", my petulant pal. When she " + verb + "s, " +
    "there's simply no stopping her. She'll know what to do!"
)
