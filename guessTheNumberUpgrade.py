# Timothy Swain
import random

def generateNumber( topLimit ):
    return random.randint(1,topLimit) 
    
def askUserToGuess( times, secretNumber ):

    for guessesTaken in range(1, times+1):
        print('Take your guess #' + str(guessesTaken) + ': ')
        guess = int(input())

        if evaluateAnswer( guess, secretNumber ) == True:
            return True
        
    return False

def evaluateAnswer( userGuess, userSecretNumber ):
    
    if userGuess > userSecretNumber:
        print("Go lower")
        return False

    if userGuess < userSecretNumber:
        print("Go higher")
        return False

    else:
        return True


def playGame( showAnswer ):
    
    topLimit = int(input("Hello player, welcome to the number lottery!\nPlease pick a maximum number.\n"))

    totalGuesses = int(input("Before you start to guess, how many tries do you think it will take to get it right?\n"))

    theNumber = generateNumber(topLimit)

    print("Now guess a number between 1 and " + str(topLimit) +" . " +" You have" + str(totalGuesses) + " guesses.") 


    
    if( showAnswer == True ):
        print('--shhh, the real number is ' + str(theNumber) + '.')
    
    
    if askUserToGuess(totalGuesses,theNumber) == True:
        print('Good job! You guessed my number!')
    else:
        print('Nope. The number I was thinking of was ' + str(theNumber))
