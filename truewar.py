import random
import time
faces = ["two", "three", "four", "five", "six", "seven",
         "eight", "nine", "ten", "jack", "queen", "king", "ace"]
suit = ["clubs", "diamonds", "hearts", "spades"]
keep_going = True
cpu_score = 0
player_score = 0
while keep_going:
    print("Shuffling...")
    time.sleep(2)
    for x in range(26):
        my_face = random.choice(faces)
        your_face = random.choice(faces)
        my_suit = random.choice(suit)
        your_suit = random.choice(suit)
        if my_face != "eight" and my_face != "ace":
            print("My card is a", my_face, "of", my_suit, ".")
        else:
            print("My card is an", my_face, "of", my_suit, ".")
        if your_face != "eight" and your_face != "ace":
            print("Your card is a", your_face, "of", your_suit, ".")
        else:
            print("Your card is an", your_face, "of", your_suit, ".")
        if faces.index(my_face) > faces.index(your_face):
            (cpu_score) += 1
            print("Point to CPU (", cpu_score, ")")
        elif faces.index(my_face) < faces.index(your_face):
            (player_score) += 1
            print("Point to player (", player_score, ")")
        elif faces.index(my_face) == faces.index(your_face):
            print("It's a tie!")
        else:
            print("An error has occured.")
        time.sleep(1)
        if player_score == 14 or cpu_score == 14:
            break
    print("There are no more cards in the deck!")
    print("The results are out...")
    time.sleep(1)
    if (player_score > cpu_score):
        print("You win!")
    elif (player_score < cpu_score):
        print("CPU wins!")
    elif (player_score == cpu_score):
        print("Tie game!")
    else:
        print("An error has occurred...")
    cpu_score = 0
    player_score = 0
    status = input("Press [ENTER] to continue, anything else to exit.\n")
    keep_going = (status == "")
print("Thanks for playing!")
