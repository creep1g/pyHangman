'''Class that parses txt file off words and removes invalid or bad'''
import random


class WordPicker(object):

    def __init__(self, max_word_len=0):
        self.word_list = []
        self.max_word_len = max_word_len
        self.rand_max = 0
        self.file_obj = self.__open_file()
        self.__fill_word_list()

    @staticmethod
    def __open_file():
        '''pens valid_words.txt if it is not found print error'''
        try:
            file_obj = open("valid_words.txt", "r")
            return file_obj
        except FileNotFoundError:
            print("File not found")
            return None

    def __fill_word_list(self):
        '''Pares through word file and adds each word to word list'''
        if self.max_word_len == 0:
            self.max_word_len = 9999

        for word in self.file_obj:
            if len(word) > self.max_word_len:
                continue
            else:
                self.word_list.append(word)
                self.rand_max += 1

    def get_word(self):
        '''Returns a random word'''
        word = self.word_list[random.randint(0, self.rand_max)].strip()
        return word
