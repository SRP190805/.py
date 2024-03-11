import random
# this library helps in random selection of any data froma a given set of data

#this function defination gives the choice of words in the game 
# the choice function of module selects a word at random from the given list of words.
def choose_word():
    words = ["python", "programming", "computer", "algorithm", "code","abandoned","absence","accident","achievement","acknowledge"]
    return random.choice(words)

#this function takes two arguements one is the list of guessed letters and
# other is the randomly selected word from above function
#if the gueesed letter is in the word it will add it to a empty string inside declared inside the function
#for every letter guessed it is matched with the word and then the letter is added to the display
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

#now the main function holds the important aspects like input and fucntion calling
def main():
    # here a variable word is intialized and the function choose_word() is called which selects a random word from given data and returns it in the variable
    word = choose_word()
    #next we create a list of gueesed letters
    guessed_letters = []
    # we also need to specify number of aatempts
    attempts = 6

    print("Welcome to the Word Guessing Game!")
    print("You have 6 attempts to guess the word.")
    # after welcoming the player to the game we call the display_word() fucnctionwhich takes the word selected and the empty guesse letters list as arguement
    print(display_word(word, guessed_letters))

    # now as the attempts are fixed we loop it till te go zero
    while attempts > 0:
        #untill they go zero we constantly take input from the user to guess a letter
        guess = input("Guess a letter: ").lower()

        #now if the length of the guessed letter is less than or greater than one or the guessed letter is not an alphabet then we display
        #select a single alphabet and continue with the loop.
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        #now if the letter guessed is in the list then we would display
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        #we append the letter to the list guessed_letters 
        guessed_letters.append(guess)

        #now if the guessed letter is in the word then it's a good guess otherwise you will lose one attempt and that would be displayed.
        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        #now if the word guessed is correct we would dispaly it if it does not contain an empty space your guesss is correct
        #and you win!
        display = display_word(word, guessed_letters)
        print(display)

        if "_" not in display:
            print("Congratulations! You've guessed the word:", word)
            break

    # otherwise you lost!
    if "_" in display:
        print("Sorry, you've run out of attempts. The word was:", word)

main()
