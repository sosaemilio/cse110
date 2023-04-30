"""
CSEPC 110 W05 - Milestone

Instructor: Travis Christiansen

Developed by Emilio Sosa


"""
# First Question
from concurrent.futures import thread


first_answer = input(f"You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? \n")

# Game starts here
if first_answer.lower() == "match":
    # Second Prompt
    second_answer = input(f"You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? \n")
    if second_answer.lower() == "run":
        # Third Propmt
        third_answer = input(f"You run and the large grizzly start hunting you around the forest. You see two ways one has a Candle (RIGHT) while the other is dark (LEFT). Which path will you take, RIGHT or LEFT?")
        if third_answer.lower() == "right":
            fourth_answer = input(" You took the right path you see many candles you keep running, and you hear the growth of a bear far away. You are not sure where you are, you just see two spheres, one blue, and one red. Which will you choose RED or BLUE?")
            if fourth_answer.lower() == "red":
                print(f"You chose RED welcomes to the dark side, you are a force user; Darth Vader will train and will be your master, one day you will be very powerful. Thanks for playing.")
            elif fourth_answer.lower() == "blue":
                print(f"You chose BLUE welcome to the light side of the force, you are a force user; Master Obi-Wan will train you, and you one day will be very powerful. Thanks for playing")
            elif fourth_answer.lower() == "run":
                print("	You took an unexpected choice you run away and literally break the MATRIX. You… my fellow realize have been living in a simulation.")
            else:
                print(f"Oops, there was an error. You wrote something incorrect")
        elif third_answer.lower() == "left":
            fourth_answer = input(f"You took the left path. It is super dark but you follow your instinct and see… The Avengers? They are literally there fighting against Thanos. You have two choices grab a LIGHTSABER or use Thor's HAMMER?")
            if fourth_answer.lower() == "lightsaber":
               print("You choose the lightsaber and throw it to Thanos stopping his plans. Avengers thank you and ask you to join the team.")
            elif fourth_answer.lower() == "hammer":
                print("You took Thor’s Hammer and it was so light for you that Thor gets surprised you are worthy of using it. You create thunder and burn Thanos.")
            else:
                print("Meh, try again")
        else:
            print(f"You didn't choose a good value")
    elif second_answer.lower() == "hide":
        # Third Prompt
        third_answer = input(f"You hide behind a tree and hear a whisper “Come with me”. The Emperor Palpatine is there willing to give you some power to run out of the forest, Will you use it? YES OR NO")
        if third_answer == "yes":
            print("You used the power of the emperor and lit all the forest. The Bear is scared and runs. It worked!. You are now a child of the emperor.")
        elif third_answer == "no":
            print("You said NO! and the Bear now sees you. He gives up with you and goes away to a tree with Honey. Phew that was close")
        else:
            print("HELP ME. It is something wrong in my end :/")
    else:
        print(f"You didn't choose a correct answer. Please try again...")
elif first_answer.lower() == "flashlight":
    # Second Prompt
    second_answer = input(f"You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? \n")  
    if second_answer.lower() == "follow":
        # Third Propmt
        third_answer = input(f"You followed the path, and end in a weird place it feels ultra-natural. It seems quiet and fantastic at the same time. You see bricks and you realize you are in a magic town. Harry is there waiting for you, he said “Would you like to learn more about Magic?” YES or NO?")
        if third_answer.lower() == "yes":
            print("You chose YES, welcome to Howard. You are a wizard and you will be trained in one of the best school of Magic. Hermione Granger will be your teacher. Thanks for playing")
        elif third_answer.lower() == "no":
            print("You chose NO, you tell him no, and keep walking getting out of the tree into the big city you continue your normal life. Thanks for playing.")
        else:
            print("Sorry, I am in loop. You wrote something bad. Try again")
    elif second_answer.lower() == "look":
        # Third Prompt
        third_answer = input(f"You look into the dark, and you see a huge grizzly user sleeping, but it doesn't seem to be bad. You can TOUCH him or GO away?")
        if third_answer.lower() == "touched":
            print(" You touch him and start feeling weird, you vanish and then open your eyes you are the bear and you no longer see your body. Welcome, you have the ability to transform between Bear and Human, use the ability with precaution. Thanks for playing.")
        elif third_answer == "go":
            print(" You touch him and start feeling weird, you vanish and then open your eyes you are the bear and you no longer see your body. Welcome, you have the ability to transform between Bear and Human, use the ability with precaution. Thanks for playing.")
    else:
        print(f"You didn't choose a correct answer. Please try again...")
    
else:
    print(f"You didn't choose a correct answer. Please try again...")
    