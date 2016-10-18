#ROOM ONE: This room leads to Door 1, Door 2, Door 3, and Door 4.
#only one Room contains the room to the ultimate prize. That is Room 6
import random
import time
from sys import exit

def major_room ():
    print "You discover yourself in a large unoccupied room."
    print "You see four doors with different labels."
    print "- Door 1: North"
    print "- Door 2: East"
    print "- Door 3: South"
    print "- Door 4: West"
    print "Which door do you take?"
    major_direction = raw_input ("> ")

    if "1" in major_direction or "North" in major_direction:
        door_one ()
    if "2" in major_direction or "East" in major_direction:
        door_two ()
    if "3" in major_direction or "South" in major_direction:
        door_three ()
    if "4" in major_direction or "West" in major_direction:
        door_four ()
    else:
        print "I don't understand what that means."

def dead ():
    print "You have died! Good job."
    exit (0)

def take_gold (number):
    gold_amount = int(number)
    print "You have chosen to taken %d amount of gold." % gold_amount
    while True:
        if gold_amount >= 100:
            print "That's not a lot of money...are you sure you don't want to take more?"
            retake = raw_input ("> ")

        elif gold_amount < 100:
            print "You're a damn hoarder, huh? Well, go on with it..before I stop you"
            break
            exit (0)
        else:
            print "I don't understand what that means."

def gold_room ():
    print "You enter an amazing room full of gold."
    print "It's clear you have reached the prize room!"
    print "How much gold do you want to take?"
    gold = raw_input ("Enter a number: ")
    take_gold (gold)

#DOOR ONE: Goes to ROOM 1 and ROOM 5
def door_one ():
    print "You open the first door to enter another unoccupied room."
    print "To your surprise, there are two more doors; which one do you take?"
    print "- Door 1: Room 1"
    print "- Door 5: Room 5"
    door_one_direction = raw_input ("> ")

    if "1" in door_one_direction:
        room_one ()
    if "5" in door_one_direction:
        room_five ()
    else:
        print "I don't understand what that means."

#DOOR TWO: Goes to ROOM TWO and ROOM SIX
def door_two ():
    print "You open the second door to enter another unoccupied room."
    print "To your surprise, there are two more doors; which one do you take?"
    print "- Door 2: Room 2"
    print "- Door 6: Room 6"
    door_two_direction = raw_input ("> ")

    if "2" in door_two_direction:
        room_two ()
    if "6" in door_two_direction:
        room_six ()
    else:
        print "I don't understand what that means."

#DOOR THREE: Goes to ROOM THREE and ROOM SIX
def door_three ():
    print "You open the third door to enter another unoccupied room."
    print "To your surprise, there are two more doors; which one do you take?"
    print "- Door 3: Room 3"
    print "- Door 6: Room 6"
    door_three_direction = raw_input ("> ")

    if "3" in door_three_direction:
        room_three ()
    if "6" in door_three_direction:
        room_six ()
    else:
        print "I don't understand what that means."

#DOOR FOUR: Goes to ROOM FOUR and ROOM FIVE
def door_four ():
    print "You open the fourth door to enter another unoccupied room."
    print "To your surprise, there are two more doors; which one do you take?"
    print "- Door 4: Room 4"
    print "- Door 5: Room 5"
    door_four_direction = raw_input ("> ")

    if "4" in door_four_direction:
        room_four ()
    if "5" in door_four_direction:
        room_five ()
    else:
        print "I don't understand what that means."

#ROOMS:
# - Room 1: Has a sleeping tiger
# - Room 2: Has a sleeping bear
# - Room 3: Has a sleeping Python
# - Room 4: Has a joker
# - Room 5: Has no one. It's an abyss!
# - Room 6: Has no one. It's an abyss!

#Once you enter each room, you have to get out only by doing the correct action.
#You will exit the room from which you came from and go back to the main_room.

#ROOM ONE: Sleeping tiger. You do not want to be in this room!
# In order to escape the room, you must sing a lullaby to it.
# All other options result in death.
# You may pet the tiger once, but the next time you pet it, it will kill you.
def room_one ():
    print "You enter the first room. At first it is very dark, but as your eyes adjust, you see..."
    print "A SLEEPING TIGER!!!!!! You panic and try to turn the knob from the door which you once came in."
    print "But it does not open. You're trapped! What to do? The tiger is about to wake up..."
    print "Choice 1: Yell at the tiger"
    print "Choice 2: Pet the tiger"
    print "Choice 3: Sing a lullaby to the tiger"
    tiger = True

    while True:
        r1_choice = raw_input ("> ")
        if "1" in r1_choice or "Yell" in r1_choice:
            print "The tiger opens its eyes angrily, leaps forward, and eats you in one bite!"
            dead ()
        elif ("2"  in r1_choice or "Pet" in r1_choice) and tiger:
            print "The tiger stares at you, doing nothing."
            tiger = False
        elif ("2" in r1_choice or "Pet" in r1_choice) and not tiger:
            print "The tiger, bored with your petting eats you."
            dead ()
        elif "3" in r1_choice or r1_choice == "Sing":
            print "The tiger yawns and goes back to sleep."
            print "You hear a click behind you! You can now exit the room."
            break
            time.sleep(1)
            major_room ()
        else:
            print "The tiger growls angrily, and eats you in one bite!"
            dead ()


#ROOM TWO: Sleeping bear.
# In order to escape the room, you must open the basket and feed the bear honey.
# All other options result in death.
# Petting the bear twice results in death.
# You are allowed up to three times to pick something from the basket.
def room_two ():
    bear_basket = ['Honey', 'Apples', 'Eggs', 'Bees']
    print "You enter the second room. At first it is very dark, but as your eyes adjust, you see..."
    print "A SLEEPING BEAR NEAR A BASKET!!!!!! You panic and try to turn the knob from the door which you once came in."
    print "But it does not open. You're trapped! What to do? The bear is about to wake up..."
    print "Choice 1: Yell at the bear"
    print "Choice 2: Pet the bear"
    print "Choice 3: Open the basket."
    bear = False

    while True:
        r2_choice = raw_input ("> ")

        if r2_choice == "Yell" or "1" in r2_choice:
            print "The bear opens its eyes immediately, leaps forward, and tears you into shreds with one swipe!"
            dead ()
        elif (r2_choice == "Pet" or "2" in r2_choice) and not bear:
            print "The bear stares at you, sniffing you hungrily."
            bear = True
        elif (r2_choice == "Pet" or "2" in r2_choice) and bear:
            print "The bear shakes its head angrily, and eats you up in one bite."
            dead ()
        elif r2_choice == "3" or "Open" in r2_choice:
            x = 0
            while x <= 1:
                print "You stick your hand in the basket and pull an object out."
                basket_item = random.choice (bear_basket)
                print "It's %r!" % basket_item
                if basket_item == "Honey":
                    print "You pass the honey to the bear. It hungrily eats it."
                    print "You hear a click behind you. The door is open! You can now exit the room."
                    time.sleep (2)
                    major_room ()
                elif basket_item == "Apples":
                    print "You pass the apples to the bear. It hungrily eats it."
                    print "You hear a click behind you. The door is open! You can now exit the room."
                    time.sleep (2)
                    major_room ()
                elif basket_item == "Eggs":
                    print "You smell the eggs. They look ruined. You decide to put them back in the basket."
                    x = x + 1
                elif basket_item == "Bees":
                    print "Oh no! Bees! You cover the basket immediately and pray the bear has not been stung."
                    x = x +1
                else:
                    x = x+1
                bear_basket.remove (basket_item)
            if x > 1:
                print "You stick your hand again, but the bear has awoken. He is angry!"
                print "He leaps toward you, destroying the basket and kiling you in one swipe."
                dead ()

#ROOM THREE: Sleeping Python
# In order to escape from this room you must solve math puzzles.
# All other choices result in death!
# You can save your progress.
def room_three ():
        print "You enter the third room, to see a snoring python."
        print "You shudder in fear and turn around to get out but the door is locked! What do you do?"
        print "Choice 1: Greet the snake."
        print "Choice 2: Choke the snake."
        r3_choice = raw_input ("> ")

        if r3_choice == "1" or r3_choice == "Greet":
            print "The snake opens one eyelid and hisses. 'You've disturbed me, and now you must pay the price.'"
            print "'I will give you three puzzles. If you can solve them, you can pass.'"
            print '\'If you cannot, I shall devour you! Are you ready?\''
            readytopuzzle = raw_input ("> ")

            while True:
                if readytopuzzle == "Yes":
                    print "The snake nodded. 'Okay, first question. What is zero divided by zero?'"
                    print "- Infinity"
                    print "- Zero"
                    print "- Does not exist"

                    puzzle_one = raw_input ("> ")

                    if puzzle_one == "Infinity":
                        print "The snake shook its head. 'That's wrong! Try again."
                    elif puzzle_one == "Zero":
                        print "The snake shook its head. 'That's wrong! Try again."
                    elif puzzle_one == "Does not exist":
                        print "The snake nodded its head. 'That's right! Onto the next question."
                        break
                    else:
                        print "I don't understand what that means."
            time.sleep (1)
            while True:
                print "'The second question is, what is fifty times fifty?'"
                puzzle_two = raw_input ("> ")

                if puzzle_two == '2500' or puzzle_two == "two thousand five hundred":
                    print "The snake nodded its head. 'That's right! Onto the next question.'"
                    break
                else:
                    print "The snake shook its head. 'That's wrong! Try again.'"
            time.sleep (1)
            while True:
                print "The third question is: How old am I?"
                print "- 1003 years old"
                print "- 50 years old"
                print "- 27 years old"
                puzzle_three = raw_input ("> ")

                if '1003' in puzzle_three:
                    print "The snake shook its head. 'That's wrong! Try again."
                elif '50' in puzzle_three:
                    print "The snake shook its head. 'That's wrong! Try again."
                elif '27' in puzzle_three:
                    print "The snake shook its head. 'That's wrong! Try again."
                elif puzzle_three == "I don't know":
                    print "The snake nodded wisely. 'That's good. Sometimes, you aren't supposed to know the answer to everything."
                    print "'You are free to go! I hope you find what you are looking for.'"
                    print "You turn and the door behind you unlocks with a click. YOu can now exit!"
                    break
                else:
                    print "I don't know what that means."
            time.sleep(1)
            gold_room ()

        else:
            print "The snake turns angrily at you and swallows you whole!"
            dead ()

def room_four ():
    print "You enter the fourth room where a Joker stands atop a jack in the box."
    print "'Greetings,' he says, smirking. 'If you answer three of my questions right, I shall let you pass.'"
    print "'Do you accept my offer?'"
    joker_response = raw_input ("> ")

    if joker_response == "Yes":
        print "'Excellent! Here are the questions."
        time.sleep (1)
        joker_riddles = open ('ex36txt.txt', 'r')
        print joker_riddles.read ()
        time.sleep (2)
        print "'Now you must answer correct, in order.'"

        while True:
            riddle_answer1 = raw_input ("The answer to the first question is: ")
            riddle_answer2 = raw_input ("The answer to the second question is: ")
            riddle_answer3 = raw_input ("The answer to the third question is: ")
            if riddle_answer1 == "Clock" and riddle_answer2 == "Glove" and riddle_answer3 == "Egg":
                print "The joker nodded his head. 'Yes, that's right. You are free to go!"
                break
                major_room ()
            elif riddle_answer1 != "Clock" and riddle_answer2 == "Glove" and riddle_answer3 == "Egg":
                print "The joker shook his head. 'Yes, you got question 2 and 3, but your answer to question 1 is wrong...'"
            elif riddle_answer1 == "Clock" and riddle_answer2 != "Glove" and riddle_answer3 == "Egg":
                print "The joker shook his head. 'Yes, you got question 1 and 3, but your answer to question 1 is wrong...'"
            elif riddle_answer1 == "Clock" and riddle_answer2 == "Glove" and riddle_answer3 != "Egg":
                print "The joker shook his head. 'Yes, you got question 1 and 2, but your answer to question 1 is wrong...'"
            else:
                print "I don't understand what that means, sorry."
    else:
        print "The joker shook his head disapprovingly. 'Guess you're stuck!"
        dead ()
        joker_riddles.close ()

def room_five ():
    print "You open the door.....and stare into an abyss."
    print "What do you do?"
    print "Choice 1: Go back to where you came from."
    print "Choice 2: Dare to take the plunge!"
    abyss = raw_input ("> ")

    if "1" in abyss or "Go" in abyss:
        major_room ()
    else:
        dead ()

def room_six ():
    print "You open the door.....and stare into an abyss."
    print "What do you do?"
    print "Choice 1: Go back to where you came from."
    print "Choice 2: Dare to take the plunge!"
    abyss = raw_input ("> ")

    if "1" in abyss or "Go" in abyss:
        major_room ()
    else:
        dead ()

room_four()
