# CodeAlpha Internship Task 1
import random
print("Welcome to the hangman program")
words_list = ["cherry", "canoe", "granny", "lampholder", 'frenchfries']

word_choice = random.choice(words_list)
word_length = len(word_choice)

word_place_holder = word_length * [""]
print(word_place_holder)

guess_trial = 6 

# checks if the word_place_holder has not been filled completely!
while "".join(word_place_holder) != word_choice:
  user_guess = input(f"Enter a word: ").lower()
  # checks if the user_guess is in the random word chosen
  if user_guess in word_choice:
    for index, letter in enumerate(word_choice):
      if letter == user_guess:
        word_place_holder[index] = user_guess
    print(word_place_holder)
    print(f"You've got {guess_trial} trials left")
    print("Congratulations, you've made a correct guess!")
    # Checks if the user_guess is not in the random word chosen and deducts a trial from their number of trials
  elif user_guess not in word_choice:
    guess_trial -= 1
    print(word_place_holder)
    print(f"You've entered a wrong input, you've got {guess_trial} trials left!")
    # Checks if the user has not guess trial again
    if guess_trial == 0:
      print("Hey man, You've got no trials left")
      break

