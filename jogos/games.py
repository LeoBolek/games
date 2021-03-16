import hangman_game
import guess_the_number

def choose_game():
    print('***********************')
    print('*** Choose the game ***')
    print('***********************')

    print('(1) Hangman Game or (2) Guess The Number')

    game = int(input('What game? -> '))

    if(game == 1):
        print('Playing hangman')
        hangman_game.play()
    elif(game == 2):
        print('Playing guess the number')
        guess_the_number.play()


if(__name__ == '__main__'):
    choose_game()
