import random as rn
import linecache 
from findDiff import findDiff 

#introduction to the game and explain what the results mean
print("Welcome to Wordle!\n")
print("You get 6 tries to guess the 5 letter word")
print("If a letter is correct it will be shown as the letter: i.e. _ _ a _ _")
print("If a letter is correct but in the wrong place it will be shown as a \'*\': i.e.  _ _ * _ _")
print("If a letter is wrong it will be shown as a \'_\': i.e. _ _ _ _ _")
print("If the word is not on the word list, or is not 5 letters long, you will be asked to guess again.")
print("Hint: There can be double letters!\n\n")

#read the words.txt file and randomly choose a word
num_lines = sum(1 for line in open('words.txt')) #Count the number of lines in the file

random_line_number = rn.randint(1, num_lines) #Generate a random line number within the range of lines

word = linecache.getline('words.txt', random_line_number) #Get the random line using linecache

#get the user guesses and return what is correct
i = 1 #track the guesses

while (i<=6) :
    #get the guess
    guess = input(f"Input Guess #{i}:")
    #check if the guess is valid (assume all 5 letter words are valid words)
    if(guess not in open('wordle.txt')):
        print('That is not a valid word. Guess again!\n')
        continue
    #find the differences
    output, count_correct = findDiff(guess, word)
    print(output + "\n")
    #check if they won
    if(count_correct == 5): #all 5 letters are correct
        break
    else:
        i+=1

#determine if they won or not
if(i<=6): #they guessed correctly within 6 tries
    print("Congrats you won!\n")
else:
    print("Oh no. Maybe next time.")
    print(f"the word was {word}")
