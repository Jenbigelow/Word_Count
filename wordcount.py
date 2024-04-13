"""Count words in file."""

def counts_words(file):
    the_file = open(file)
    word_count = {}

    for line in the_file:
        words = line.rstrip().split(" ")
        for word in words:
            word = remove_special_characters(word)
            if word.isalpha:
                word = word.lower()
                #  if the word only contains alphabetical characters
                word_count[word] = word_count.get(word, 0) + 1
                #  Add the word and its count to dictionary


    print(word_count)
    return word_count

    
def remove_special_characters(word):
    non_alpha_chars = [',','?','*','.','[',']','"','(',')','!', '_']
    for letter in word:
        if letter in non_alpha_chars:
            word = word.replace(letter, '')
    return word


counts_words(input("Enter text:"))
# counts_words("twain.txt")

            # Iterating over each word from the list of words
            # for letter in word:
                # Iterates over each letter in a word
                # if letter == non_alpha_chars:
                    # If the letter is a special character
                    # del letter
                    # delete the letter