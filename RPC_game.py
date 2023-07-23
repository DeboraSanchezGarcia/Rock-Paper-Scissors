import random



while True:
    
    user = str(input("Choose: Rock, Paper, or Scissors? \n"))

    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)

    if user.lower() == computer:
        print("Tie!")
    elif user.lower() == "rock":
        if computer == "paper":
            print("You lost, paper covers rock.")
        else:
            print("You won! Rock breaks scissors.")
    elif user.lower() == "paper":
        if computer == "rock":
            print("You won! Paper covers rock!")
        else:
            print("You lost. Scissors cut paper.")
    else:
        if computer == "rock":
            print("You lost. Rock breaks Scissors.")
        else:
            print("You won! Scissors cut paper!")
    
    keepgoing= input("Do you want to keep playing? \n")

    if keepgoing.lower() == "no":
        print("Ok.")
        break
    else:
        print("Ok.")
        continue

