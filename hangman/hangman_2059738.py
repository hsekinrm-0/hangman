# Coding Challenge 3, hangman.py
# Name:Nikesh Shrestha
# Student No: 2059738

# Hangman game

import random
import sys

word1 = open("words.txt", 'r')
word1.close()

responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]


def load_words():
    """
    Generate a list of valid words. Words are strings of lowercase letters.
    Returns a list of valid words.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    wordlist = []
    print("Loading word list from file...")
    # fh : file
    fh = open("words.txt")
    # line: string
    # wordlist: list of strings
    content = fh.read()
    for line in content.split():
        wordlist.append(line)
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_random_word(wordlist):

    '''
    wordlist(list): list of words(strings)
    Returns a word from wordlist at random
    '''
    return random.choice(wordlist)


wordlist=load_words()

def is_word_guessed(g_word,letters_guessed):
    """
    g_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of g_word are in letters_guessed; False otherwise
    """

    c = 0
    for i in letters_guessed:
        if i in g_word:
            c += 1
    if c == len(g_word):
        return True
    else:
        return False




def get_guessed_word(g_word, letters_guessed):
    '''

    g_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
             what letters in g_word have been guessed so far.

    '''

    s = []
    for i in g_word:
        if i in letters_guessed:
            s.append(i)
    ans = ''
    for i in g_word:
        if i in s:
            ans += i
        else:
            ans += '_ '
    return ans





def get_remaining_letters(letters_guessed):
    '''
    letters_guessed: list (of strings), which letters have been guessed
    returns: string, comprised of letters that haven't been guessed yet.
    '''
    import string
    ans = list(string.ascii_lowercase)
    for i in letters_guessed:
        ans.remove(i)
    return ''.join(ans)






def hangman(g_word):
    '''
    g_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the g_word contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''

    print(responses[0].format(len(g_word)))
    print("-------------")


    global letters_guessed
    error = 0
    letters_guessed = []

    while 6 - error > 0:

        if is_word_guessed(g_word, letters_guessed):
            print("-------------")
            print(responses[1])
            break

        else:
            print(responses[4].format( 6 - error))
            print(responses[5].format(get_remaining_letters(letters_guessed)))
            guess = str(input("Please guess a letter: ")).lower()

            if guess in letters_guessed:
                print(responses[8].format(get_guessed_word(g_word, letters_guessed)))

            elif guess in g_word and guess not in letters_guessed:
                letters_guessed.append(guess)
                print(responses[6].format(get_guessed_word(g_word, letters_guessed)))

            else:
                letters_guessed.append(guess)
                error += 1
                print(responses[7].format(get_guessed_word(g_word, letters_guessed)))

        if 6 - error == 0:
            print("------------------")
            print(responses[3].format(g_word))
            break

        else:
            continue




def welcome():

    print("Welcome to Hangman Ultimate Edition")
    g_word=choose_random_word(wordlist).lower()
    hangman(g_word)

welcome()

if __name__ == "__main__":
    pass



