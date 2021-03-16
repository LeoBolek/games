
def play():
    print('*******************************************')
    print('*** Hello, welcome to the Hangman Game! ***')
    print('*******************************************')

    secret_word = 'banana'
    hanged = False
    right = False

    while(not hanged and not right):
        print('Playing')

    print('Game over! Thanks for playing.')


if(__name__ == '__main__'):
    play()
