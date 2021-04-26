import random
word_list = ["arward","baboon","camel"]
chosen_word = random.choice(word_list)

#guess = input(" Guess a word : ").lower()

display =[]
word_length =len(chosen_word)
for _ in range(word_length):
    display += "_"
print (display)    

guess = input(" Guess a letter : ").lower()

for position in range(word_length) :
    letter = chosen_word[position]
    if letter == guess :
        display[position]=letter
    #     print (" Right !")
    # else :
    #     print (" Wrong !")    
print (display)

# display =[]
# # for letter in chosen_word:             #  the same output
# for _ in range (len(chosen_word)) :      # the same output
#        display +="-"                     #  add dash _ into display
# print(display)       


# print(f"Pssst, the solution is {chosen_word")
# for letter in chosen_word:
#     if letter == guess :
#         print(" Right ! ")
#     else :
#         print("wrong !")    
    
