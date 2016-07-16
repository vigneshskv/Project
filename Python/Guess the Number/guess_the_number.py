import random

def guess_my_number():
    """
    Player to guess a number within 5 chances
    """
    guess_attempts = 0
    ai_number = random.randint(1, 25)
    player_name = raw_input("Hi, What is your name?")
    print('Well, ' + player_name + ', I am thinking of a number between 1 and 25.')

    while(guess_attempts < 5):
        guess = int(raw_input("Take a guess"))
        guess_attempts += 1

        if(guess < ai_number):
            print "Your guess is too low."
        elif(guess < ai_number):
            print "Your guess is too high."
        else:
            break

    if guess == ai_number:
        print "Good job" + player_name + "! You guessed my number in " + str(guess_attempts) + " guesses!"
    else:
        print "Nope. The number I was thinking of was " + str(guess_attempts)

if __name__ =="__main__":
    guess_my_number()