import random
def games():
    print("Welcome, To the game 🎮")
    print ("Selct a function (1-3)")
    print("1. Guess Number Game 🎯\n2. Rock Paper Scissors Game✊✋✌️ \n3. Exit Program ❌ ")
    
    selection = int(input("Enter Your Choice:"))
    if selection==1:
        value = random.randint(1, 15)
        attempt=0
        while True:
            try:
                guesses=int(input("Guess a number:"))
                if guesses<1 or guesses>15:
                    print("Please enter the number between 1 to 15")
                    continue
                attempt +=1
                if guesses< value:
                    print("Opps!!....It's too low🔽")
                elif guesses > value:
                    print("Ohh!!!...It's too high🔼")
                else:
                    print("WOW!!!.. You have the guessed the numer in", guesses, "attemps")
                    break
            except ValueError:
                print("Enter a valid number")
    elif selection ==2:
        print("1. rock✊\n2.paper✋ \n3.scissor✌️ ")
        attempt=0
        while True:
            computer = random.choice(["paper","scissor","rock"])
            player = input("Enter your choice:")
            attempt=1
            if player not in (["rock","paper","scissor"]):
                print("Invalid choice, Please enter from the given list")
                continue
            else:
                print("Computer choice is",computer)
                if player == computer:
                    print("OMG!!!... It's a tie🤝")
                elif (player=="rock" and computer=="paper") or (player=="paper" and computer=="scissor") or (player=="scissor" and computer=="rock"):
                    print("Sorry!!!.. You lost the game😞")
                else:
                    print("Yes!!!....You won🏆")
                not_playing=input("Do you want to play again? [yes/no]")
                if not_playing=="yes":
                    continue
                else:
                    print("Thanks for playing")
                    break
    elif selection==3:
        print("Exiting the game")

    else:
        print("Invalid choice")
games()





        

    


