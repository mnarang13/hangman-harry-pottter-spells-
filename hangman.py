import random

def getWord():
    words = ['expelliarmus', 'glisseo', 'lumos', 'nox', 'geminio', 'aguamenti', 'episkey', 'sectumsempra', 'levicorpus', 'liberacorpus', 'crucio', 'imperio', 'sonorus', 'quietus', 'accio', 'alohomora', 'colloportus', 'defodio',
             'incendio', 'reducto', 'stupefy', 'protego', 'legilimens', 'inpedimenta', 'obliviate', 'scourgify', 'silencio', 'muffliato', 'confundo', 'diffindo', 'avis', 'brachiabindo', 'emancipare', 'confringo', 'deletrius',  'descendo',
             'evanesco', 'expulso', 'furnunculus', 'impervius', 'incarcerous', 'langlock', 'locomotor', 'mobilicorpus', 'morsmordre', 'obscuro', 'oppugno', 'orchideous', 'portus', 'reducio', 'engorgio', 'relashio', 'rennervate', 'reparo', 'rictusempra', 'riddikulus',
             'serpensortia', 'tarantallegra']
    return random.choice(words).upper()

def check(word, guesses, currentGuess):
    currentGuess = currentGuess.upper()
    status = ''
    i = 0
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += '*'
        if letter == currentGuess:
            matches += 1
    if matches > 1:
        print("The spell contains ", matches, '"' + currentGuess + '"' + 's.')
    elif matches == 1:
        print("The spell contains the letter "+ '"' + currentGuess + '"' + '.')
    else:
        print("Sorry, the spell does not contain the letter " + '"' + currentGuess + '".')
    return status

def main():
    word = getWord()
    guesses = []
    guessed = False
    print("Welcome to Harry Potter spell hangman!")
    print('The spell contains ', len(word), ' letters.')
    while not guessed:
        print('Please enter 1 letter or a ',len(word),'letter spell.')
        guess = input("Your guess: ")
        guess = guess.upper()
        if guess in guesses:
            print("You have already guessed this letter or spell.")
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print("Your guess was incorrect.")
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word, guesses, guess)
            if result == word:
                guessed = True
            else:
                print(result)

        else:
            print('Invalid Entry')

    print("Correct! Your spell was " + word + ". It took you",len(guesses),"tries to guess it. You win! :)")

main()    
