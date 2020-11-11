file_in = open("dictionary.txt", "r")
file_out = open("valid_words.txt", "w")
import string

bad_chars = string.whitespace + string.punctuation


for word in file_in:
    for letter in word.split():

        if not letter.isalpha():
            continue

        else:
            file_out.write(word)
