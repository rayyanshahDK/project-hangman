#HANGMAN CODE ALPHA
import random
words = ["mercedes", "alpine", "toyota", "lamborghini", "ferrari", 
             "volkswagon", "pagani", "pininferina"]
max_incorrect_guesses = 6
def hangman():
    word_of_choice = random.choice(words)
    guessed = []
    wrong = 0
    print("Welcome to Hangman!")
    while wrong < max_incorrect_guesses:
        display = ""
        for letter in word_of_choice:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "
        print("\nWord:", display)
        print("Guessed:", ", ".join(guessed) if guessed else "None")
        print("Wrong guesses left:", 6 - wrong)
        
        if all(letter in guessed for letter in word_of_choice):
               print("\nYou won! The word was:", word_of_choice)
               break
        while True:
                guess = input("Guess the CAR: ").lower()
                if len(guess) != 1:
                  print("Please enter a single letter.")
                elif guess in guessed:
                  print("You already guessed that!")
                elif guess in word_of_choice:
                  guessed.append(guess)
                  print("Correct!")
                  break
                else:
                  guessed.append(guess)
                  wrong += 1
                  print("Wrong Guess!!!")
                  break
    else:
        print("\nGame over! The word was:", word_of_choice)
        
hangman()
play_again = input("\nPlay again? (y/n): ").lower()
if play_again == "y":
    hangman()


            

     
    
    
    