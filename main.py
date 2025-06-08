import random
computer_choice = random.choice([-1,0,1])
user= input("Enter your choice (Snake, Water or Gun): ")
userdict={"Snake":-1, "Water": 0, "Gun": 1}
revdict={-1:"Snake", 0:"Water", 1:"Gun"}
you=userdict[str(user)]
print(f"User Chose: {revdict[you]} \nComputer chose: {revdict[computer_choice]}")
if (you==computer_choice):
    print("It's a Tie")
else:
    if you==1 and computer_choice==-1:
        print("You Win")
    elif you==-1 and computer_choice==0:
        print("You Win")
    elif you==0 and computer_choice==1:
        print("You Win")
    elif you==1 and computer_choice==0:
        print("You Lose")
    elif you==-1 and computer_choice==1:
        print("You Lose")
    elif you==0 and computer_choice==-1:
        print("You Lose")
    else:
        print("Game disqualified")