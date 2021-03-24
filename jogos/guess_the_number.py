# Author: Leonardo Bolek

import random

def play():
    print('****************************************************')
    print('*** Hello, welcome to the Guess the Number Game! ***')
    print('****************************************************')

    secret_number = random.randrange(1, 101)
    chances = 0
    points = 1000

    print('Levels of difficulty:')
    print('(1) Easy | (2) Medium | (3) Hard')

    level = int(input('Choose your level: '))
    if(level == 1):
        chances = 20
    elif(level == 2):
        chances = 10
    else:
        chances = 5

    for round in range(1, chances + 1):
        print(f'Chance {round} of {chances}')

        guess = int(input('Guess the number from 1 to 100: '))
        print(f'You typed: {guess}')

        right_answer = guess == secret_number
        bigger = guess > secret_number
        lower = guess < secret_number

        if(guess < 1 or guess > 100):
            print('You must type a number from 1 to 100.')
            continue

        if(right_answer):
            print(f'You guessed the right number and scored {points} points! Congratulations!!!')
            break
        else:
            if(bigger):
                print('Wrong! You guessed a bigger number.')
            elif(lower):
                print('Wrong! You guessed a lower number.')
            lost_points = abs(secret_number - guess) # 40 - 20 = 20 points
            points = points - lost_points

    print(f'Game over! You scored {points} points. Thank you for playing!')


if(__name__ == '__main__'):
    play()
