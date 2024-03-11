#find the differences between the guess and the word
def findDiff(guess, word):
    output = ''
    count_correct = 0
    for i in range(0,5):
        if(guess[i] == word[i]): #the letter is right and in the correct spot
            output = output + guess[i]+' '
            count_correct+=1
        elif(guess[i] in word): #the letter is correct but in the wrong spot
            output = output+'* '
        else:   #the letter is wrong
            output = output+ '_ '
    return output, count_correct