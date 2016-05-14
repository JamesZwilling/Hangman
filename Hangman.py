from tkinter import*
import tkinter.messagebox
import playGame

class Hangman:
    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.title("Hangman")
        word = playGame.pickWord() #pick the word for the game
        guessed = [] #create an empty list for guessed
        
#create frames
        self.__welcome_frame = Frame(self.__main_window)
        self.__word_frame = Frame(self.__main_window)
        self.__remain_frame = Frame(self.__main_window)
        self.__guessed_frame = Frame(self.__main_window)
        self.__entry_frame = Frame(self.__main_window)
        self.__button_frame = Frame(self.__main_window)

#create and pack widget for welcome display
        self.__welcome_label = Label(self.__welcome_frame,
                                    text = "HANGMAN",
                                    bg = "white", fg = "blue",
                                    font=("Helvetica", 40))
        self.__welcome_label.pack(side="top")

#create and pack widgets for word display
        self.__secret_word_label = Label(self.__word_frame, \
                                   text="Secret Word:")
        self.__secret_word = StringVar()
        self.__word_label = Label(self.__word_frame, \
                                  textvariable=self.__secret_word)
        self.__secret_word_label.pack(side="left")
        self.__word_label.pack(side="left")

#create and pack widgets for guess remaining display
        self.__remain_text_label = Label(self.__remain_frame, \
                                   text="Guesses remaining:")
        self.__remain = StringVar()
        self.__remain_label = Label(self.__remain_frame, \
                                  textvariable=self.__remain)
        self.__remain_text_label.pack(side="left")
        self.__remain_label.pack(side="left")

#create and pack widgets for guessed letter display
        self.__guessedText_label = Label(self.__guessed_frame,\
                                         text="Guessed letters:")
        self.__guessed = StringVar()
        self.__guessed_label = Label(self.__guessed_frame, \
                                     textvariable=self.__guessed)
        self.__guessedText_label.pack(side="left")
        self.__guessed_label.pack(side="left")

#create and pack entry field
        self.__entryText_label = Label(self.__entry_frame, \
                                       text="Guess:")
        self.__entry = Entry(self.__entry_frame, \
                             width=1)
        self.__entryText_label.pack(side="left")
        self.__entry.pack(side="left")

#create and pack buttons
        self.__guess_button = Button(self.__button_frame, \
                                     text="Guess", \
                                     command= lambda: self.__guess(word,
                                                            guessed))
        #lambda function stops the called function from being called until
        #the button is pressed. 
        self.__quit_button = Button(self.__button_frame, \
                                    text="Quit", \
                                    command=self.__main_window.destroy)
        self.__guess_button.pack(side="left")
        self.__quit_button.pack(side="left")
        #link the return key to the guess function
        self.__entry.bind("<Return>", lambda event: self.__guess(word,
                                                            guessed))
#pack frames
        self.__welcome_frame.pack()
        self.__word_frame.pack()
        self.__remain_frame.pack()
        self.__guessed_frame.pack()
        self.__entry_frame.pack()
        self.__button_frame.pack()
        
#set the game board
        self.__setGame(word, guessed)

#enter tkinter main loop
        mainloop()
    
    def __guess(self, word, guessed):
        guess = self.__entry.get() #get the entered letter
        guessed = playGame.guess(guessed, guess) #check the guess, and add it
        #to list
        self.__guessed.set(guessed)#set the guessed list display
        secret_word = playGame.writeWord(word, guessed)#write the word with
        #approprite blanks
        self.__secret_word.set(secret_word) #set word display
        self.__entry.delete(0, END) #clear entry box
        remain = playGame.remain(word, guessed) #check how many incorrect
        #guesses remain
        if remain == 0: #if no guesses close the window
            self.__main_window.destroy()
            main()
        self.__remain.set(remain) #if guesses are left, set the display
        victory = playGame.vicCon(word, guessed) #check for victroy
        if victory == True: #if victorious, close window
            self.__main_window.destroy()
            main()

    def __setGame(self, word, guessed):
        secret_word = playGame.writeWord(word, guessed)#write the word with
        #approprite blanks
        self.__secret_word.set(secret_word) #set word display
        remain = playGame.remain(word, guessed) #check how many incorrect
        #guesses remain
        self.__remain.set(remain) #if set the guessed display

def main():
    h1 = Hangman()

main()

