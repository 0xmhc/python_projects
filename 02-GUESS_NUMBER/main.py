import random;

def guess(x) :
    random_number = random.randint(1,x)
    guess = 0
    while random_number != guess :
        guess =  int(input(f"Guess a nunmber between 1 and {x}: "))
        if guess > random_number :
            print("Sorry, Guess again. Too high")
        elif guess < random_number :
            print("Sorry, Guess again. Too low")
    print(f"Great, You Win, The number is {guess}")
guess(5)