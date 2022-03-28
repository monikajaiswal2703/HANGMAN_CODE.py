import random


def load_word():
    # word_list=["navgurukul","learning","kindness"]
    
    """Ye function kaafi jayada words ko load karne mai help karega"""
    WORDLIST_FILENAME = "/home/riya/Desktop/HANGMAN.PY/word.text"
    print ("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    word_list = str.split(line)
    print ("  ", len(word_list), "words loaded.\n")
    return word_list

def choose_word():
    word_list=load_word()
    secret_word=random.choice(word_list)
    secret_word=secret_word.lower()

    return secret_word
