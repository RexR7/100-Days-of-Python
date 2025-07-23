print(r'''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
Choice1 = str(input("You are lost in a jungle. Choose a way, Right, Left or Straight. ")).strip().capitalize()

if Choice1 == "Right":
    Choice2 = str(input('''Oh! So you want to go Right. Very well.
You have found a cycle. Do you want to use it? Yes or No. ''')).strip().capitalize()
    if Choice2 == "Yes":
        print("The cycle's seat broke. The iron bar is in your ass now. Game Over!")
    elif Choice2 == "No":
        Choice3= str(input('''You have found two boxes on your way. Pick one.
"Gold or Black? ''')).strip().capitalize()
        if Choice3 == "Gold":
            print("Greedy Human! Game Over!")
        elif Choice3 == "Black":
            print("You have found the treasure. CONGRATULATIONS!")
        else:
            print("Alright I give up. You do not deserve to play this game.")
    else:
        print("DO NOT MESS WITH ME!")
elif Choice1 == "Left":
    print("You fell into a Gorge. Game Over!")
elif Choice1 == "Straight":
    print("You were eaten by a man-eating hippopotamus. Game Over!")
else:
    print("Ah! You're trying to be over-smart. NOT FUNNY!")
