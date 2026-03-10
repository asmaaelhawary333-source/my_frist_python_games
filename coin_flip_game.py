import random
print(" welcome to the coin guessing game ")
print("""
choice the way:
1-using random.random()
2-using random.ranint()
""")
choice=input("enter your choose (1 or 2) \n")
if choice=="1":
    toss=random.random()
    if toss>=0.5:
        computer_choice="heads"
        print(f"the computer choice {computer_choice}")
    else: 
        computer_choice="tails"
        print(f"the computer choice {computer_choice}")
elif choice=="2":
    if random.randint(0,1)==0:
         computer_choice="heads"
         print(f"the computer choice {computer_choice}")

    else:
        computer_choice="tails"
