import random
print(" welcome to The  game !!!")
choice = ["rock","paper","scissors","exit"]
def get_winner(player, computer):
    if player == computer:
        return "It's a tie! "
    elif  (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
         return " You Win !"
    else:
        return "computer wins!"

while True:
    print("Enter your choice\n"\
    "1. Rock\n"\
    "2. Paper\n"\
    "3. Scissors\n"\
    "4. Exit")
    player_choice = input("your choice: ")
    if player_choice == "1":
        player_choice = "rock"
    elif player_choice == "2":
        player_choice = "paper"
    elif player_choice == "3":
        player_choice = "scissors"
    elif player_choice == "4":
        player_choice = "exit"
    print("You chose:",player_choice)

    if player_choice == "exit":
        print ("Thanks for playing ")
        break
    
    if player_choice not in choice:
         print("Invalid choice. Please choose rock, paper, or scissors.")
         continue
    
    computer_choice = random.randrange(1,4)
    if computer_choice == 1:
        computer_choice = "rock"
    elif computer_choice == 2:
        computer_choice = "paper"
    elif computer_choice == 3:
        computer_choice = "scissors"
    print("Computer chose:",computer_choice)

    result = get_winner(player_choice, computer_choice)
    print(result)



    
