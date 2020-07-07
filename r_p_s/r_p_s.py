from random import randint

Rock = "Rock" 
Paper = "Paper" 
Scissors = "Scissors" 


while True:
    x = randint(1,3)
    your_input = input("Choose Rock, Paper, Scissors!")
    
    if x == 1 and your_input == "Rock":
        computer = Rock
        print("Computer choose: ", computer)
        print("Tie!")

    if x == 1 and your_input == "Scissors":
        computer = Rock
        print("Computer choose: ", computer)
        print("You lost!")

    if x == 1 and your_input == "Paper":
        computer = Rock
        print("Computer choose: ", computer)
        print("You Won!")

        
        
    if x == 2 and your_input == "Rock":
        computer = Paper
        print("Computer choose: ", computer)
        print("You lost!")

    if x == 2 and your_input == "Scissors":
        computer = Paper
        print("Computer choose: ", computer)
        print("You Won!")

    if x == 2 and your_input == "Paper":
        computer = Paper
        print("Computer choose: ", computer)
        print("Tie!")



    if x == 3 and your_input == "Rock":
        computer = Scissors
        print("Computer choose: ", computer)
        print("You Won!")

    if x == 3 and your_input == "Scissors":
        computer = Scissors
        print("Computer choose: ", computer)
        print("Tie!")

    if x == 3 and your_input == "Paper":
        computer = Scissors
        print("Computer choose: ", computer)
        print("You lost!")

    