import random

def guess(n):
    random_no = random.randint(1,n)
    guess = 0
    while guess != random_no:
        guess = int(input(f"guess a random number between 1 and {n}:"))
        if guess < random_no:
            print("sorry, your no is less.guess again")
        elif guess > random_no:
            print("sorry, your no is high. guess again")

    print(f"wooh ! your guess is correct. the no is {random_no}")



guess(9)
