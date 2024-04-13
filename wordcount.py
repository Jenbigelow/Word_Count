"""Count words in file."""

def counts_words(file):
    the_file = open(file)
    word_count = {}
    non_alpha_chars = [',','?','*','.','[',']','"','(',')','!']
    for line in the_file:
        words = line.rstrip().split(" ")
        for word in words:
            for letter in word:
                if letter in non_alpha_chars:
                    del letter
                    if word.isalpha():
                        word = word.lower()
                #  if the word only contains alphabetical characters
                        word_count[word] = word_count.get(word, 0) + 1
                #  Add the word and its count to dictionary


    print(word_count)
    return word_count

    

counts_words("test.txt")
# counts_words("twain.txt")

            # Iterating over each word from the list of words
            # for letter in word:
                # Iterates over each letter in a word
                # if letter == non_alpha_chars:
                    # If the letter is a special character
                    # del letter
                    # delete the letter