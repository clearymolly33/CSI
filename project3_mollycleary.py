import random
words = ['moxie', 'apple', 'youth', 'empty', 'angel']
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6
def display_word():
  displayed = ''
  for letter in secret_word:
    if letter in guessed_letters:
      displayed += letter + ' '
    else:
      displayed += '_ '
  print('Secret word:')
  print(displayed)
def check_game_status():
  all_guessed = True
  for letter in secret_word:
    if letter not in guessed_letters:
      all_guessed = False
  if all_guessed:
    final_word = ''
    for letter in secret_word:
      final_word += letter + ' '
    print('Congratulations! You guessed the word!')
    print('Final word:')
    print(final_word)
    return True
  elif incorrect_guesses == max_guesses:
    print('Game over! You lost.')
    print('The secret word was: ' + secret_word)
    return True
  else:
    return False
def play_game():
  global incorrect_guesses
  game_over = False
  while not game_over:
    display_word()
    print('Guessed letters:', guessed_letters)
    print('Incorrect guesses remaining:', max_guesses - incorrect_guesses)
    guess = input('Enter a letter: ').strip().lower()
    if guess == '' or len(guess) > 1:
      print('Please enter a single letter.')
    elif guess in guessed_letters:
      print('You already guessed that letter. Try another one!')
    else:
      guessed_letters.append(guess)
      if guess in secret_word:
        print('Correct guess!')
      else:
        incorrect_guesses += 1
        print('Incorrect guess!')
      game_over = check_game_status()
    print()
if __name__ == '__main__':
  play_game()