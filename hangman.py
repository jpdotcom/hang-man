import random
import time
f=open("words_alpha.txt","r")

words = []
for line in f:
    words.append(line)



for i in range(0,len(words)):
    b=words[i]
    b=b[0:len(b)-1]
    words[i]=b

man=open("man.txt")

drawing=[]

for line in man:
    drawing.append(line)

for i in range(0,len(drawing)):
    b=drawing[i]
    b=b[0:len(b)-1]
    drawing[i]=b

word_to_guess=random.choice(words)
lives=1

def MainFuc():
    print ("Let's play a game of Hangman!. What is your name?")
    name=input()
    print("Hello "+ name +"!. Hang on just a second, I'm getting my word ready")
    word_list=list(word_to_guess)
    time.sleep(5)
    return word_list

def letter_guessing(letter_guess,forming_letter,word_list,letters_said):
    global lives
    if letter_guess in letters_said:
        print("That letter was already said! I'll restart your turn and won't take any lives :)")
        return
    if letter_guess.isalpha()==False:
        print("That's not a letter! I'll reset your turn")
        return
    if letter_guess[0] in word_list:
        print(letter_guess[0] + " is in my word!")
        for i in range(0,len(word_list)):
            if word_list[i]==letter_guess[0]:
                forming_letter.pop(i)
                forming_letter.insert(i,letter_guess[0])
        letters_said.append(letter_guess[0])
        time.sleep(3)
        print("So this is the word so far", forming_letter)
    if forming_letter== word_list:
        time.sleep(2)
        return True
    elif letter_guess[0] not in word_list:
        letters_said.append(letter_guess[0])
        lives-=1
        print("Sorry! " + letter_guess[0] + " is not in my word. You have " + str(lives) + " lives left" )

def guess_the_word(word_to_guess):
    global lives
    print("Ok what is your guess:")
    guessed_word=input()
    time.sleep(2)
    if guessed_word == word_to_guess:
        return True
    elif guessed_word!=word_to_guess:
        lives-=1
        print("Sorry! " + guessed_word + " is not my word. You have " + str(lives) + " lives left")
    




def complete_guess_process(word_list):
    global lives
    letters_said=[]
    forming_letter=["_"]*len(word_list)
    print("Ok I'm Ready. You have " + str(len(forming_letter))+ " lives before the game is over. After each turn, I will allow you to guess what the word or a letter is. However, if you guess a letter wrong, it will cost you 1 life")
    time.sleep(2)
    print("This is how long my word is", forming_letter)
    while lives!=0:
        time.sleep(2)
        print("Want to guess the word or guess a letter")
        word_or_letter=input()
        
        if "letter" in word_or_letter:
            print("What is your letter")
            letter_guess=input()
            c= letter_guessing(letter_guess,forming_letter,word_list,letters_said)
            if c:
                return "You've completed the word! It was " + word_to_guess +". You win!"
            
        elif "word" in word_or_letter:
            b=guess_the_word(word_to_guess)
            if b:
                return "Correct! You Win"
    if lives==0:
        for e in drawing:
            print(e)
        return "You lost you pathetic subhuman filth. You are not worthy of exisitng and should be hanged. This was my word: " + word_to_guess
            
            
print(word_to_guess)
print(complete_guess_process((MainFuc())))
