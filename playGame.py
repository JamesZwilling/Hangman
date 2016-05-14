import random
import tkinter
import tkinter.messagebox

def writeWord(word, guessed):
    secret_word = '' #set the printed word to an empty string
    for char in word: #check if each character in the word is in guessed
        if char in guessed:
            secret_word += char #if it is, add the haracter to the print
        else: #if not, add an underscore
            secret_word += ' _ '
    return(secret_word)#return printale word

def guess(guessed, guess):
    newGuess = str(guess)#rturn the guess into a string
    newGuess = newGuess.lower()
    if newGuess not in guessed: #check if new guess has already been guessed
        if newGuess.isalpha() == True: #check if guess is a letter
            if len(newGuess) == 1:#check that there is only one letter
                guessed += newGuess # if new letter, add it to list
        else: #display error if not a letter
            tkinter.messagebox.showwarning("Warning", "Enter a single letter")
    else: #display error if already guessed
        tkinter.messagebox.showwarning("Warning", "Letter has already been"+
                                       " guessed")
    return(guessed)#return list of guessed letters
    

def pickWord():
    #create a list of words to choose from
        wordList = ["boat", "banana", "computer", "super", "captain", "basketball",
                "telephone", "pizza", "detergent", "sword", "dragon", "turkey",
                "rhino", "chicken", "pepperoni", "dinosaur", "medicine",
                    "catfish", "explore", "confort", "concert", "lightbulb"]
        wordNum = random.randint(0, len(wordList) - 1)
        word = wordList[wordNum]#get a random word using random number
        return(word) #return the word

def remain(word, guessed):
    remain = 6 #set number of allowed guesses
    for guess in guessed: #check how many guessed letters are not in the word
        if guess not in word:
            remain -= 1
    if remain == 0: #if no more incorrect guesses remain, player loses 
            tkinter.messagebox.showinfo("You Lose", "Sorry, you lost! Your "+
                                        "word was " + word)
    return(remain) # return remaining guesses
        
def vicCon(word, guessed):
    victory = True
    for i in range(len(word)): #check if all neccesary letters have been guessed
         if word[i] not in guessed:
             victory = False
    if victory == True: #if all letters have been guessed, player wins
        tkinter.messagebox.showinfo("You Win", "Congratulations! You win!")
    return(victory)
