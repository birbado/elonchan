# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Elon")

label start:


    scene bg americana at truecenter:
        xzoom 1 yzoom 1


    show elon pray at truecenter


    e "Hello."

    e "You may know me as the insanely successful billionare Elon Musk."

    show elon smile at truecenter

    e "But there is much more to who I am than just my money."

    e "I think you'll realize that I am much different than the public view."

    show elon what at truecenter:
        xzoom 0.25 yzoom 0.25

    e "But that's enough about me for now."

    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Space X"

    e "Wonderful to meet you, %(player_name)s!"

    #povname = renpy.input(prompt, default='your name', allow=None, exclude='{}', length=None, with_none=None,  pixel_width=None)










    # This ends the game.

    return
