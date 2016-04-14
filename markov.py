from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path)
    text = contents.read()

    return text


def make_chains(text_string, size_of_tuple):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    chains = {}
    # Split by whitespace
    text_list = text_string.split()
    #loop over every 2 word pair making tuples
    for i in range(len(text_list) - size_of_tuple):
        #print text_list[i], text_list[i + 1]
        #if we get back a zero from:
        #start with 1 word tuple
        tuple_list = []
        for index_number in range(size_of_tuple):
            tuple_list.append(text_list[i + index_number])
        word_tuple = tuple(tuple_list)
        #word_tuple = (text_list[i], text_list[i + 1]) 
        #re-define tuple based on argv input  
        tuple_key = chains.get(word_tuple, 0)
        #print tuple_key
        if tuple_key == 0:
            chains[word_tuple] = [text_list[i + size_of_tuple]]

        else:
            chains[word_tuple].append(text_list[i + size_of_tuple])

        #print word_tuple
            #print "found it, again"
    #for each in chains:
        #print each, chains[each]
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    #pick a random key 
    #poem_list = []
    random_key_choice = choice(chains.keys() )
    # print random_key_choice
    #first_word, second_word = random_key_choice
    #poem_list = [first_word, second_word]

    poem_list = list(random_key_choice)

    while chains.get(random_key_choice, 0) != 0:
        #pick a random value for that key
        print random_key_choice
        random_value = choice(chains[random_key_choice])
        # print random_value
        poem_list.append(random_value)

        #taking tuple, making it into list
        tuple_list = list(random_key_choice)
        #pop [0] in that list list.pop(0)
        tuple_list.pop(0)
        #append [0] to tuple list
        tuple_list.append(random_value)
        #convert to tuple
        # first_word, second_word = random_key_choice
        random_key_choice = tuple(tuple_list)
    #take the second word from the key and the value to make a new key
    #rinse repeat until error
    #print poem_list
    text = " ".join(poem_list)

    return text


input_path = (sys.argv[1])

size_of_tuple = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, size_of_tuple)

# Produce random text
random_text = make_text(chains)

print random_text
