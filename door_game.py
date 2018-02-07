import random
from sys import exit
import time

lives = 10 

# MY CODE 
def start():
    print("Welcome to the game of unknown...")
    time.sleep(1)
    print("If one dares type \'enter\' to begin")

    reply = input("> ")

    if 'enter' in reply:
        print("You have two doors to choose from...")
        time.sleep(2)
        print("Light and dark...which do you choose?")

    reply = input("> ")

    while reply != 'light' and reply != 'dark':
        print("Please type the correct door...")
        reply = input("> ")

    if 'light' == reply:
        light_door()
    if 'dark' == reply:
        dark_door()

# MY CODE 
def light_door():
    print("Welcome to the Light room..")
    time.sleep(3)
    print("Here things may feel new and a bit confusing..")
    time.sleep(2)
    print("First you must solve this riddle to show you are ready to proceed..")
    time.sleep(2)
    print("""There are 2 ducks in front of 2 other ducks. There are 2 ducks behind
    2 other ducks. There are 2 ducks beside 2 other ducks. How many ducks are there?
    """)

    reply = input("> ")
    while reply != '4':
        print("That is incorrect..")
        reply = input("> ")

    print("Good Job!")
    print("You may proceed through the next door.")
    maniac_door()

def dark_door():
    print("Welcome to the dark room.")
    time.sleep(2)
    print("Good luck trying to find the light.")
    print("But first, you must solve this riddle.")
    time.sleep(1)
    print("""I am a strong as a rock, but a word can destroy me.
    What am I?""")
    
    reply = input("> ")
    
    while reply != 'silence':
        print("I knew you would never solve my riddle.")
        time.sleep(1)
        print("But I'll give you another go.")
        reply = input("> ")

    print("Well done.")
    time.sleep(1)
    print("You may go farther in this journey than I originally anticipated.")
    time.sleep(1)
    print("You may proceed.")
    time.sleep(1)
    print("Would you like to enter \'door 1\' or \'door 2\'?")

    reply = input("> ")

    while reply != 'door 1' and reply != 'door 2':
        print("The option you have chosen is invalid.")
        time.sleep(1)
        print("Your studpidity is going to cost you your life.")
        dead("Better luck next time.")
        reply = input("> ")

    if 'door 1' == reply:
        weapon_door()
    if 'door 2' == reply:
        demon_door()

# MY CODE
def maniac_door():
    print("In this room there is a deranged man pointing to the ceiling shouting random numbers...")
    time.sleep(2)
    print("\'4, 3, 5, 7!!\'")
    time.sleep(1)
    print("You see two items laying on the floor...a backpack and a glass vial...")
    time.sleep(1)
    print("You must dash to one of the items and make for the door...")
    print("1. bag")
    print("2. vial")

    reply = input("> ")

    has_vial = False
    has_bag = False

    while reply != 'bag' and reply != 'vial':
        print("Please type the correct door...")
        reply = input("> ")

    has_vial = ('vial' == reply)
    has_bag = ('bag' == reply)

    if 'bag' == reply or 'vial' == reply:
        print("Now quickly pick a door!")
        print("red or green!?")

    while reply != 'red' and reply != "green":
        print("Please type the correct door...")
        reply = input("> ")

    if 'red' == reply:
        ogre_room(has_vial)
    if 'green' == reply:
        jump_room(has_bag)

# MY CODE
def ogre_room(has_vial):
    if not has_vial:
        print("Unfortunately you grabbed a parachute and entered the ogre's den...")
        time.sleep(1)
        print("You are ripped from limb to limb...")
        time.sleep(1)
        dead('. . .restarting. . .')

    print("There is a large ogre blocking the next door...would you like to turn around or use vial?")
    print("1. quit")
    print("2. vial")
    reply = input("> ")

    if reply == '1' or reply == 'quit':
        print("Exiting game. . .")
        exit_game()

    if reply == '2' or reply == 'vial':
        print("You threw the bottle at the ogre and he begins to melt away!")
        print("The door is already open! However, it's beginning to close!")
        print("Would you like to leap through or investigate room?")
        print("1. leap")
        print("2. invest")

    reply = input("> ")

    if reply == '1' or reply == 'leap':
        code_door()
    if reply == '2' or reply == 'invest':
        print("You wonder around the room for hours and find nothing...")
        print("Now you are locked in this room forever")
        dead()


    code_door()

# MY CODE 
def jump_room(has_bag):
    if not has_bag:
        print("Unfortunately you choose a vial over a parachute...")
        time.sleep(1)
        print("You fall for what feels like forever and splatter like a balloon...")
        time.sleep()
        #dead(. . .restarting. . .)

    print("As soon as you step through the door you begin to fall!!")
    time.sleep(2)
    print("Quickly equip the bag and pull chute!!")
    time.sleep(2)
    print("type \'equip bag\' ")

    start = time.time()

    reply = input("> ")

    if reply == 'equip bag':
        print("NOW PULL THE CHUTE!!!")
        print("type \'chute\' ")

    reply = input("> ")
    stop = time.time()

    if stop - start > 12:
        print("You unfortunately were not quick enough and you have fallen to your death...")
        time.sleep(2)
        print('. . .restarting. . .')
        start()

    elif reply == 'chute':
        print("Phew...that was close. You land in front of the next door...")
        code_door()

# MY CODE
def code_door():
    print("As the door closes behind you, you hear it lock...")
    print("you are now standing in a empty white walled room with a keypad on the wall across from you.")
    print("They screen asks for a 4-digit code...")

    reply = input("> ")

    while reply != '4357' and reply == '6969':
        print("Incorrect password")
        reply = input("> ")

    if reply == '4357' or reply == '6969':
        print("The front wall begins to drop into the ground.")
        time.sleep(1)
        print("There is a sign that reads, \'Enter the maze or abort by typing quit\'")

    reply = input("> ")

    if reply == 'enter':
        maze_room()
 
def weapon_door():
    print("I see you've solved my riddle..")
    time.sleep(1)
    print("""Here you must choose your weapon that will help you
defend yourself for the remainder of the journey..""")
    time.sleep(1)
    print("There is a chest with the number \'1122\' printed on it.")
    time.sleep(1)
    print("Open the chest. Remember the code. You might need it later on.")
    time.sleep(1)
    print("In the case, there are two items for you to choose from.")
    print("The \'hatchet\' or a bottle of \'holy water\'.")
    time.sleep(1)
    print("Whatever you choose will help you along the journey.")
    print("So choose wisely.")

    reply = input("> ")

    while reply != 'hatchet' and reply != 'holy water':
        print("Quickly, choose one of these two weapons.")
        reply = input("> ")

    has_holy_water = ('holy water' == reply)
    has_hatchet = ('hatchet' == reply)

    if reply == 'hatchet' or reply == 'holy water':
        print("""Now that you have your item, lets move on. There are two gates
do you wish to go through the \'narrow\' gate, or the gate that is
\'wide\'?""")

        reply = input("> ")

    while reply != 'narrow' and reply != 'wide':
        print("You have not chosen a vaild path.")
        print("Choose and, and choose wisely.")
        reply = input("> ")

    if reply == 'wide':
        demon_room(has_holy_water)
    if reply == 'narrow':
        tree_room(has_hatchet)

def demon_door():
    print("There is a demon in this room.")
    time.sleep(1)
    print("What would you like to do? \'fight demon\' or \'run\'?")

    reply = input("> ")

    while reply != 'fight demon' and reply != 'run':
        print("You need to make a clear decision on what you want to do.")
        print("And quick!")
        reply = input("> ")

    if reply == 'fight demon':
        print("The demon enters your body.")
        time.sleep(1)
        dead("Your soul is lost forever.")

    if reply == 'run':
        dark_door()

def demon_room(has_holy_water):
    if not has_holy_water:
        print("""There is a demon blocking the path. He spots you and
        starts coming for you.""")
        time.sleep(1)
        print("Your hatchet does nothing against this mighty beast.")
        time.sleep(1)
        print("The demon takes over your body.")
        print("Your soul is lost forever.")
        dead("Better luck next time.")

    print("I see you have chosen to enter the wide gate.")
    time.sleep(1)
    print("This gate will lead to destruction.")
    time.sleep(2)
    print("""There is a demon blocking the door. He spots you and
starts coming for you. You can try and use your bottle of holy water
to disable the demon. Type \'use holy water\'""")

    reply = input("> ")

    while reply != 'use holy water':
        print("That didn't work. Try using the holy water.")
        reply = input("> ")

    if reply == 'use holy water':
        print("You have burned the demon!.")
        time.sleep(1)
        print("You see a door that the demon was guarding.")
        time.sleep(1)
        print("""Quickly, before he realized what has happened, run to the
        door and go through it!""")
        time.sleep(1)
        print("There's a door behind the sharks dead body.")
        print("You go through the door...")
        time.sleep(1)
        print("You hear the door shut, and lock, behind you.")
        code_door()

def tree_room(has_hatchet):
    if not has_hatchet:
        print("You have chosen the narrow path.")
        time.sleep(1)
        print("This road leads to life, but few find it.")
        time.sleep(1)
        print("The path behind you has disappeared.")
        time.sleep(1)
        print("The tree of the forbidden fruit is blocking the path ahead.")
        print("Would you like to eat the fruit? \'yes\' or \'no\'?")

        reply = input("> ")

        while reply != 'yes' and reply != 'no':
            print("Its a simple yes or no question.")
            print("Answer it.")
            reply = input("> ")

        if reply == 'yes':
            print("This fruit is forbidden.")
            dead("You will now suffer a painful death.")

        if reply == 'no':
            print("""You're stuck on the path with no food, and no way to
get past the tree.""")
            time.sleep(1)
            dead("You loose your mind and die of starvation.")

    print("You have chosen the narrow path.")
    time.sleep(1)
    print("This road leads to life, but few find it.")
    time.sleep(2)
    print("""The tree of the forbidden fruit is blocking the path ahead.
Would you life to replenish your strength and \'eat fruit\' or would you
like to \'use hatchet\' and chop down the tree?""")

    reply = input("> ")

    while reply != 'use hatchet' and reply != 'eat fruit':
        print("It's a simple question.")
        print("Answer it.")
        reply = input("> ")

    if reply == 'use hatchet':
        print("""Congradulations! You have successfully chopped down the tree
of the forbidden fruit.""")
        time.sleep(1)
        print("Further down the path, there is a door.")
        print("You walk to it and, go through the door...")
        time.sleep(1)
        print("You hear the door shut and lock behind you.")
        code_door()

    if reply == 'eat fruit':
        print("This fruit is forbidden.")
        dead("You will now suffer a painful death.")

def maze_room():
    print("There is no turning back now...")
    time.sleep(2)
    print("""To find your way through the maze type \'left\' or \'right.\' Any time you type an inccorect
direction you will be sent back to the beginning of the maze to restart. Keep your barrings and your footpath
to escape. Good luck!""")

    correct_answer = ['left', 'right', 'right', 'left', 'right', 'right', 'left', 'right']

    step = 0

    while True:
        path = input("> ")
        if path == correct_answer[step]:
            print("Good!")
            step += 1

            if step >= len(correct_answer):
                break

        else:
            print("""Well...this is unfortunate. You entered the wrong command so you must start
from the beginning.""")
            step = 0

    print("CONGRADULATIONS!You have completed the game of known!!")

def dead(why):
    global lives

    print(why, "Restarting...")
    time.sleep(1)
    lives -= 1
    print("You have", lives, "Lives left.")
    time.sleep(2)
    start()

def exit():
    print("You've come this far just to quit? Coward.")

start()
