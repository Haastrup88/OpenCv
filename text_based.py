name=input("Enter your name:")
print(f"Greeting {name}, welcome to my text_based game")
option=input("Would you rather play/Perish?")
if option.lower().strip()=="play":
    option_A=input(f" Dear {name}, do you want to bet once/multiple:")
    if option_A.lower().strip()=="once":
        print("You need a lot of fund to play Casino")
        print(f"Thank you {name}!, we hope to see you again")
    elif(option_A.lower().strip()=="multiple"):
        print("Perfect")
        rounds=int(input("How many rounds do you want to play(in figures):"))
        if rounds<=2:
            print("Oops! The number of rounds must be greater than 2 to have full enjoyment")
            print(f"Dear {name}, we hope to see you some other time")
        else:
            print("Congratulation! You are qualified for this game")
    else:
        print("Invalid input")
elif(option.lower().strip())=="perish":
    print("Game over, you\'re dead now")
else:
    print("Invalid Input")