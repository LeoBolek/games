# Author: Leonardo Bolek

def play():
    print('*******************************************')
    print('*** Hello, welcome to the Hangman Game! ***')
    print('*******************************************')

    secret_word = 'banana'
    right_letters = ['_', '_', '_', '_', '_', '_']
    hanged = False
    right = False

    print(right_letters)

    while(not hanged and not right):

        guess = input('What letter? ')
        guess = guess.strip()

        index = 0
        for letter in secret_word:
            if(guess.upper() == letter.upper()):
                right_letters[index] = letter
            index = index + 1

        print(right_letters)

    print('Game over! Thanks for playing.')


if(__name__ == '__main__'):
    play()
