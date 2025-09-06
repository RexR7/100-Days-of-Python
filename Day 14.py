import art
import game_data
import random

print(art.logo)

main_list = game_data.data

A, B = random.sample(main_list, 2)
used_items = {id(A), id(B)}

score = 0
game = True

while game:
    values_a = list(A.values())
    values_b = list(B.values())

    print(f"Compare A: {values_a[0]}, a {values_a[2]}, from {values_a[3]}.")
    print(art.vs)
    print(f"Against B: {values_b[0]}, a {values_b[2]}, from {values_b[3]}.")

    ques = str(input("Who has more followers? Type 'A' or 'B': ")).upper()

    if values_a[1] > values_b[1]:
        winner, loser = A, B
    else:
        winner, loser = B, A

    if (ques == "A" and winner == A) or (ques == "B" and winner == B):
        score += 1
        print(f"You're right! Current score: {score}")
        A = winner
        remaining_choices = [item for item in main_list if id(item) not in used_items]
        if remaining_choices:
            B = random.choice(remaining_choices)
            used_items.add(id(B))
        else:
            print(f"No more new options left! Final score: {score}")
            game = False
    else:
        print(f"Sorry, that's wrong! Final score: {score}")
        game = False