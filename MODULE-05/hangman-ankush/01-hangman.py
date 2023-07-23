

import hangman

print("""
   +---------+----------------+
       |     | H A N G M A N 
       O     | G A M E :) 
      /|\    | B Y
      / \    | A N K U S H 
             | T I W A R I :)
   =============================
""")


chosen_word = hangman.pick_random_word()
print(chosen_word)

lives=6 #defines default lives 6
 
display=[]
for letter in chosen_word:
    display+= "_"  # creating blanks
# print(display)

game_over=False
while not game_over:
    user_guess= input("Guess a letter (any one from a to Z)\n")
    if user_guess in hangman.letters:
        # print(user_guess)
        user_guess=user_guess.lower()
        # if user_guess in chosen_word:
        #     print(f"{user_guess} is present\n")
        # else:
        #     print("not present\n")
    else:
        print("Invalid input\n")

    for pos in range(len(chosen_word)):
        letter=chosen_word[pos]
        if letter==user_guess: # then reveal that letter
            display[pos]=letter
    
    print(f"{' '.join(display)}")
    # print(display)

    if user_guess not in chosen_word:
        lives=lives-1
        if lives==0:
            game_over=True
            print("Out of lives, You lose\n🥲🥲🥲🥲🥲")

        print(hangman.hangman_stages[lives])

    if "_" not in display:
        game_over=True
        print("You won the Game\n😀😃😉😎😀")
    