import random
import time

'''
To-do
Make it not case sensitive
Make it check if the guess is a real word
'''

# def setUpGame():
#     pickWord()
#     guesses = []
#     round = 1
def loadWords():
    with open("two-letter-words.json") as file:
        twoLetterWords = file.read().split(",")
        twoLetterWords[0] = twoLetterWords[0][1:]
        twoLetterWords[-1] = twoLetterWords[-1][:-1]
        for i in range(len(twoLetterWords)):
            twoLetterWords[i] = twoLetterWords[i][1:-1]
    with open("three-letter-words.json") as file:
        threeLetterWords = file.read().split(",")
        threeLetterWords[0] = threeLetterWords[0][1:]
        threeLetterWords[-1] = threeLetterWords[-1][:-1]
        for i in range(len(threeLetterWords)):
            threeLetterWords[i] = threeLetterWords[i][1:-1]
    with open("four-letter-words.json") as file:
        fourLetterWords = file.read().split(",")
        fourLetterWords[0] = fourLetterWords[0][1:]
        fourLetterWords[-1] = fourLetterWords[-1][:-1]
        for i in range(len(fourLetterWords)):
            fourLetterWords[i] = fourLetterWords[i][1:-1]
    with open("five-letter-words.json") as file:
        fiveLetterWords = file.read().split(",")
        fiveLetterWords[0] = fiveLetterWords[0][1:]
        fiveLetterWords[-1] = fiveLetterWords[-1][:-1]
        for i in range(len(fiveLetterWords)):
            fiveLetterWords[i] = fiveLetterWords[i][1:-1]
    with open("six-letter-words.json") as file:
        sixLetterWords = file.read().split(",")
        sixLetterWords[0] = sixLetterWords[0][1:]
        sixLetterWords[-1] = sixLetterWords[-1][:-1]
        for i in range(len(sixLetterWords)):
            sixLetterWords[i] = sixLetterWords[i][1:-1]
    return twoLetterWords, threeLetterWords, fourLetterWords, fiveLetterWords, sixLetterWords
    
        
        

def pickWord():
    # with open("six-letter-words.json") as file:
    #     words = file.read().split(",")
    choice = random.randrange(5128)
    return sixLetterWords[choice]

def checkGuess(code, guess):
    codeSpliced = [i for i in code]
    guessSpliced = [i for i in guess]
    roundscore = 0
    outOfPlaceLetters = []
    hitSpots = []
    for i in range(len(guessSpliced)):
        if guessSpliced[i] == "-":
            pass
        else:
            if guessSpliced[i] == codeSpliced[i]:
                roundscore+=1000
                hitSpots.append(i)
            elif guessSpliced[i] in codeSpliced:
                outOfPlaceLetters.append(guessSpliced[i])
    for i in hitSpots[::-1]:
        codeSpliced.pop(i)
        guessSpliced.pop(i)
    for letter in codeSpliced:
        if letter in outOfPlaceLetters:
            roundscore+=250
            outOfPlaceLetters.remove(letter)
    if code == guess:
        roundscore+=3000
    return roundscore

def printTurn(round, guesses, scores):
    time.sleep(1)
    print(f"\n\n----Round {round}----")
    time.sleep(1)
    print("Secret Word:\n______\n")
    if round == 1 :
        return
    else:
        print(f"{guesses[0]}----  {scores[0]}")
        if round == 2 :
            return
        else:
            print(f"{guesses[1]}---  {scores[1]}")
            if round == 3 :
                return
            else:
                print(f"-{guesses[2]}--  {scores[2]}")
                if round == 4 :
                    return
                else:
                    print(f"--{guesses[3]}-  {scores[3]}")
                    if round == 5 :
                        return
                    else:
                        print(f"---{guesses[4]}  {scores[4]}")
                        if round == 6 :
                            return
                        else:
                            print(f"--{guesses[5]}  {scores[5]}")
                            if round == 7 :
                                return
                            else:
                                print(f"-{guesses[6]}-  {scores[6]}")
                                if round == 8 :
                                    return
                                else:
                                    print(f"{guesses[7]}--  {scores[7]}")
                                    if round == 9 :
                                        return
                                    else:
                                        print(f"{guesses[8]}-  {scores[8]}")
                                        if round == 10 :
                                            return
                                        else:
                                            print(f"-{guesses[9]}  {scores[9]}")
                                            if round == 11:
                                                return
                                            else:
                                                print(f"{guesses[10]}  {scores[10]}")


                
def getGuess(round):
    if round == 1:
        guess = input("__---- Guess a 2 letter word in the underlined positions: ")
    elif round == 2:
        guess = input("___--- Guess a 3 letter word in the underlined positions: ")
    elif round == 3:
        guess = input("-___-- Guess a 3 letter word in the underlined positions: ")
    elif round == 4:
        guess = input("--___- Guess a 3 letter word in the underlined positions: ")
    elif round == 5:
        guess = input("---___ Guess a 3 letter word in the underlined positions: ")
    elif round == 6:
        guess = input("--____ Guess a 4 letter word in the underlined positions: ")
    elif round == 7:
        guess = input("-____- Guess a 4 letter word in the underlined positions: ")
    elif round == 8:
        guess = input("____-- Guess a 4 letter word in the underlined positions: ")
    elif round == 9:
        guess = input("_____- Guess a 5 letter word in the underlined positions: ")
    elif round == 10:
        guess = input("-_____ Guess a 5 letter word in the underlined positions: ")
    else:
        guess = input("______ Guess the full 6 letter word: ")
    return guess.upper()

def validateGuess(round, guess):
    if round == 1:
        if len(guess) != 2 or guess not in twoLetterWords:
            return False
    elif round >= 2 and round <= 5:
        if len(guess) != 3 or guess not in threeLetterWords:
            return False
    elif round >= 6 and round <= 8:
        if len(guess) != 4 or guess not in fourLetterWords:
            return False
    elif round == 9 or round == 10:
        if len(guess) != 5 or guess not in fiveLetterWords:
            return False
    elif round == 11:
        if len(guess) != 6 or guess not in sixLetterWords:
            return False

            

def playGame():
    word = pickWord()
    guesses = []
    scores = []
    score = 0
    round = 1
    while round <= 11:
        printTurn(round, guesses, scores)
        guess = getGuess(round)
        valid = validateGuess(round, guess)
        if valid == False:
            time.sleep(1)
            print("----------Invalid Guess----------")
            time.sleep(1)
            print("---------Not a real word---------")
            time.sleep(1)
            print("------or wrong # of letters------")
            time.sleep(1)
            print("------------Try again------------")
            time.sleep(2)
        else:
            guesses.append(guess)
            
            # put the guess in the right slots
            if round == 3:
                guess = f"-{guess}"
            elif round == 4:
                guess = f"--{guess}"
            elif round == 5:
                guess = f"---{guess}"
            elif round == 6:
                guess = f"--{guess}"
            elif round == 7:
                guess = f"-{guess}"
            elif round == 10:
                guess = f"-{guess}"

            roundScore = checkGuess(word, guess)
            scores.append(roundScore)
            score+=roundScore
            round+=1
            print(f"You got {roundScore} points. You have {score} points")
            time.sleep(1)
    print(f"Good game! The word was {word} and you scored {score} points")

if __name__ == "__main__":
    twoLetterWords, threeLetterWords, fourLetterWords, fiveLetterWords, sixLetterWords = loadWords()
    playGame()