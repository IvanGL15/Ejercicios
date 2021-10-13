Player1 = "N/A"
Player2 = "N/A"

print("Hello, this is the Rock - Paper - Scissors game!!")

while (1):
    Player1 = input ("First player, introduce your choice (R - P - S): ")
    Player2 = input ("Second player, introduce your choice (R - P - S): ")

    if Player1 == "R":
        if Player2 == "R":
            print("You are tie, try again")
        elif Player2 == "P":
            print("Player2, you wins!!")
        elif Player2 == "S":
            print("Player1, you wins!!")
        else:
            print("Incorrect input, try again")

    elif Player1 == "P":
        if Player2 == "P":
            print("You are tie, try again")
        elif Player2 == "S":
            print("Player2, you wins!!")
        elif Player2 == "R":
            print("Player1, you wins!!")
        else:
            print("Incorrect input, try again")
        
    elif Player1 == "S":
        if Player2 == "S":
            print("You are tie, try again")
        elif Player2 == "R":
            print("Player2, you wins!!")
        elif Player2 == "P":
            print("Player1, you wins!!")
        else:
            print("Incorrect input, try again")

    else:
            print("Incorrect input, try again")

    restart = input ("Do you want to play again? (Y/N): ")

    if restart != "Y":
        break
    
        