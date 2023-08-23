import enchant
from itertools import combinations

dictionary = enchant.Dict("en_US")
mainWord = ""

        
def game():
    startWord = input("Enter the guessing word: ")
    
    allPossibleWords = []
    
    for count in range(3 , len(startWord) + 1):
        addingAllWords = combinations(startWord, count)
        allPossibleWords += [' '.join(i) for i in addingAllWords]
                    
    final_list = []
    
    for option in range(len(allPossibleWords)):
        if (dictionary.check(allPossibleWords[option].replace(" ", "")) == True):
            final_list.append(allPossibleWords[option].replace(" ", ""))
        
    game_active = True
    total_words = len(final_list)
    # import countdown
    while(game_active):
        guess = input("Enter a word made from the letters of " + startWord + ": ")
        
        if (guess.lower() == "q"):
            game_active = False
        if (total_words == 0):
            game_active = False
        
        if guess in final_list:
            print("Correct Word")
            total_words = total_words - 1
            print("The total number of words left is " + str(total_words))
            final_list.remove(guess)
        else:
            print("Not A Correct Word")
            print("The total number of words left is " + str(total_words))
              

game()
