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

def guess_computer(x) :
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' :
        if low != high :
            guess = random.randint(low,high)
        else :
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C): ').lower()
        if feedback == "h" :
            high = guess - 1
        elif feedback == "l" :
            low = guess + 1
    print(f"Yeah, The computer guessed your number, {guess}, correctly!")
    

guess_computer(500)
# guess(5)