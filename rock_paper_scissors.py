import random
print(" welcome to the Rock , Paper and scissers game..")
rock = """
    ___
---'   ____)
      (_)
      (_)
      (____)
---.(_)
"""

paper = """
     ___
---'    __)__
           __)
          ___)
         ___)
---.__)
"""

scissors = """
    ___
---'   __)__
          __)
       __)
      (____)
---.(
"""
user=input(" press enter to continue or type (help) for the rules \n")
if user=="help":
    print("""****RULES****
   1-you chooce and the computer chooces
   2-Rock smashes scissors->Rock win
   3-Scissors cut paper->Scissors win
   4-Paper covers rock->Paper win
    """)
elif user=="":
    user_chooce=input(" enter your choice (rock, paper, scissors):").lower()
    if user_chooce=="rock":
        print(rock)
    elif user_chooce=="paper":
        print(paper)
    elif user_chooce=="scissors":
        print(scissors)
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    print(f"computer chose:{computer_choice}")
    if computer_choice=="rock":
        print(rock)
    elif computer_choice=="paper":
        print(paper)
    elif computer_choice=="scissors":
        print(scissors)
    
    if user_chooce == computer_choice:
        print("It's a draw! 🤝")

    elif (user_chooce == "rock" and computer_choice == "scissors") or \
             (user_chooce == "paper" and computer_choice == "rock") or \
             (user_chooce == "scissors" and computer_choice == "paper"):
            print("Congratulations! You win! 🎉")
    else:
            print("Computer wins! 🤖 Hard luck.")
else:
    print("invaild choice, please run the program again and chooce (rock, paper or scissers)")

