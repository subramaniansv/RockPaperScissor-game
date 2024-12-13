import random

print("---------WELCOME---------")
playerScore=0
computerScore=0
options =("rock" ,"paper","scissor")

playerChoice=""
while True:
    
    playerChoice=input("enter your choice (rock,paper,scissor or q to quit)").lower()
    
    if playerChoice=="q":
        if playerScore>computerScore:
            print("You won the match")
            
        if playerScore<computerScore:
            print("Computer won the match")
           
        if playerScore==computerScore:
            print("It's a tie!")
        print(f"Final Scores -> You: {playerScore}, Computer: {computerScore}")
        print("-"*30)
        break
    
    else :
        
        if playerChoice not in options:
            print("Invalid options")
            continue
        computerChoice=random.choice(options)
        if playerChoice==computerChoice:
            print("it's a tie")
        elif (playerChoice == "rock" and computerChoice == "scissor") or \
         (playerChoice == "paper" and computerChoice == "rock") or \
         (playerChoice == "scissor" and computerChoice == "paper"):
            playerScore += 1
            print(f"Your choice:{playerChoice}")
            print(f"Computer choice:{computerChoice}")
            print(f"You score a point {playerScore}")
            print("You won a point!")
        else:
            computerScore+=1
            print(f"Your choice:{playerChoice}")
            print(f"Computer choice:{computerChoice}")
            print(f"computer score a point {computerScore}")