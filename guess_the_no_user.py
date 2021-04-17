import random

def computer_guess(x):
    low = 1
    high = x
    
    advice = ""
    while advice != 'c' and low != high:
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #could be high also b/c low=high
        guess = random.randint(low, high)
        advice = input(f"is {guess} too high(H) ,too low(L), or correct(C)").lower()

        if advice=='h':
            high = guess -1
        elif advice=='l':
            low = guess +1
    
    print(f"wooh ! the computer guessed it correct. it is {guess} !")



computer_guess(100)

