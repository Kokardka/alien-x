import random
import time
# used modules

print("""Hello my friend ^_^
0_0 afraid ? ? ?
????????????????????????""")
time.sleep(5)
# scary title, next line plus time delay before the first task

name = input("What is your name?")
print("Well hello " + name, "it is now time to talk")
time.sleep(5)
# input users name

while True:
    try:
        x = int(input("How many aliens did you see last night on the sky? Ghghghg stars I mean: "))
        y = int(input("and the night before: "))
        break
    except ValueError:
        print("Really? A word? nope! Need number...")
print(x+y)
# how to use exception ValueError

if x+y <= 20:
    print("Not bad...")
elif 21 <= x+y <= 50:
    print("Many! ! ! cool")
elif 51 >= x+y <= 90:
    print("WOW ! ! ! ! ! ! ! !")
elif 91 >= x+y <= 150:
    print("AMAZING! ! ! ! ! ! ! !")
elif x+y >= 151:
    print("UNBELIEVABLE! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !")
# first task "values" plus 'if' and 'elif'

time.sleep(3)
print("Now...................................")
time.sleep(2)
print("............................")
time.sleep(2)
print("..................")
time.sleep(2)
# something before the second task

print("The UFO is speaking to You...")
time.sleep(3)
print("........")
emotions = ["fear", "anger", "sadness", "disgust", "surprise", "trust", "disgust",
            "anticipation", "anger", "friendship", "fear", "shame", "kindness",
            "pity", "indignation", "envy", "love", "suffering", "weeping", "joy",
            "anxiety", "despair", "devotion", "reflection", "meditation", "guilt",
            "determination", "pride", "helplessness", "affirmation", "negation",
            "disdain", "astonishment", "horror", "shyness", "modesty", "blushing",
            "admiration", "adoration", "amusement", "awe", "awkwardness", "boredom",
            "calmness", "confusion", "craving", "entrancement", "interest", "relief",
            "nostalgia", "romance", "sadness", "satisfaction", "desire", "sexual",
            "ecstasy", "mood", "hug", "jealousy", "sympathy", "worry", "prudery",
            "pleasure", "romantic", "rumination", "pessimism", "courage", "malaise"
            ]
print(random.choice(emotions))
print(len(emotions))
print("...and more different emotions people have...")
# random computer choice from the list of emotions and len

time.sleep(3)
print("Oh no!")
time.sleep(3)
print("Something teleported You on some weird spaceship")
# walking into spaceships rooms, second task

time.sleep(3)
usr_input = ''
while usr_input not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    usr_input = input("Which room do You choose from 9 different rooms: ")
    if usr_input == '1':
        print("You are now in the room with some species...")
    elif usr_input == '2':
        print("You found some chest in the room...")
    elif usr_input == '3':
        print("You felt into some hole in the room...")
    elif usr_input == '4':
        print("Some creature attacked You when You just walked into the room...")
    elif usr_input == '5':
        print("You think that something is staring at You near the room doors...")
    elif usr_input == '6':
        print("You try to open some locked doors...")
    elif usr_input == '7':
        print("You found some potions on a shelf in the room...")
    elif usr_input == '8':
        print("In the room that You choose is really dark, You don't see anything...")
    elif usr_input == '9':
        print("After the room doors are another doors...")

time.sleep(3)
print("Guess the number to the door lock from 1 to 9, if You want to go out. Try:")
number = random.randint(1, 10)
amount = 0
while True:
    a = int(input("number"))
    if a == number:
        print("You have guessed it right!!!,the answer is ", number)
        break
    else:
        print("Try again and better hurry up!")
        amount = amount + 1
        print(amount)
        print("Trial counter")
# guessing game, amount of tries: declare variable at the beginning that will hold tries amount
# and add its incrementation in else block

time.sleep(3)
print("""
         -----
        |     |
        { = = }
        |  _  |
          ___
    <---- <><> ---->
         ||||||
         ||||||
         <><><>
         ||  ||
         ||  ||
        oO    Oo""")

from turtle import *
color('blue', 'yellow')
begin_fill()
while True:
    forward(200)
    left(50)
    if abs(pos()) < 3:
        break
end_fill()
done()
# Python turtle

print("Nice! You opened some strange portal...")
time.sleep(3)
print("Let's now play a... chess game! Yes, something like chess")
time.sleep(3)

enemy_1 = {'color': 'red', 'weapon': 'hammer'}
enemy_2 = {'color': 'blue', 'weapon': 'sword'}
enemy_3 = {'color': 'yellow', 'weapon': 'knife'}
enemy_4 = {'color': 'black', 'weapon': 'morning star'}
enemy_5 = {'color': 'orange', 'weapon': 'fists'}
enemy_6 = {'color': 'green', 'weapon': 'spear'}
opponent = input("What color of enemy do you want to choose?: " + "\nBe careful, It have a strong weapon. So? ")
if opponent == 'red':
    print("hammer")
elif opponent == 'blue':
    print("sword")
elif opponent == 'yellow':
    print("knife")
elif opponent == 'black':
    print("morning star")
elif opponent == 'orange':
    print("fists")
elif opponent == 'green':
    print("spear")
else:
    print("No enemy no weapon!")

print(type(enemy_1))
print(enemy_2.get("color"))
print(enemy_4)
enemy_4["Height"] = 320
print(enemy_4)
# dictionaries - dict

# generates a random number
# between 1 and 6 (including both 1 and 6):

time.sleep(3)
print("Maybe I can draw something for You?")
time.sleep(3)
print("so just choose a number in your mind...")
time.sleep(3)

x = "y"

while x == "y":

    p = random.randint(1, 6)

    if p == 1:
        print("+-----+")
        print("|     |")
        print("|  0  |")
        print("|     |")
        print("+-----+")
    if p == 2:
        print("+-----+")
        print("| 0   |")
        print("|     |")
        print("|   0 |")
        print("+-----+")
    if p == 3:
        print("+-----+")
        print("|     |")
        print("|0 0 0|")
        print("|     |")
        print("+-----+")
    if p == 4:
        print("+-----+")
        print("|0   0|")
        print("|     |")
        print("|0   0|")
        print("+-----+")
    if p == 5:
        print("+-----+")
        print("|0   0|")
        print("|  0  |")
        print("|0   0|")
        print("+-----+")
    if p == 6:
        print("+-----+")
        print("|0 0 0|")
        print("|     |")
        print("|0 0 0|")
        print("+-----+")

    x = input("press 'y' to roll some paint again and something else to exit...")

else:
    e = exit("and that was the last task... for now...")
