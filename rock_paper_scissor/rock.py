import random

choices = ["Pierre", "Papier", "Ciseaux"]
print("if you want to end write 'End'")
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0

while True: 
    player = input("Pierre, Papier, Ciseaux?").capitalize()

    if player == computer: 
        print("Play Again")

    elif player == "Pierre":
        if computer == "Papier":
            print("You loose")
            cpu_score+=1
        else:
            print("You win")
            player_score+=1


    elif player == "Papier":
        if computer == "Ciseaux": 
            print("You loose")
            cpu_score+=1
        else: 
            print("You win")
            player_score+=1

    
    elif player == "Ciseaux":
        if computer == "Pierre":
            print("You loose")
            cpu_score+=1
        else: 
            print("You win")
            player_score+=1   


    elif player == "End":
        print("Your score:",player_score)
        print("Computer score", cpu_score)
        break 