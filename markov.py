from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path)
    text = contents.read()

    return text


def make_chains(text_string):
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
    for i in range(len(text_list) - 2):
        #print text_list[i], text_list[i + 1]
        #if we get back a zero from:
        word_tuple = (text_list[i], text_list[i + 1]) 
        tuple_key = chains.get(word_tuple, 0)
        #print tuple_key
        if tuple_key == 0:
            chains[word_tuple] = [text_list[i + 2]]

        else:
            chains[word_tuple].append(text_list[i + 2])
            #print "found it, again"
    for each in chains:
        print each, chains[each]
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
