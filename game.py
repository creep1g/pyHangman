from word_picker import WordPicker


class Hangman(WordPicker):

    def __init__(self, player_num=1, difficulty=1):
        self.player_num = player_num
        self.difficulty = difficulty

        if difficulty < 2:
            max_len = 6
        else:
            max_len = 0

        WordPicker.__init__(self, max_len)
        self.__current_word = []
        self.__guessed_letters = []
        self.__correct_guesses = []
        self.__board = []

    def new_word(self):
        '''Asks WordPicker for a new word'''
        new_word = WordPicker.get_word(self)
        for i in new_word:
            self.__current_word.append(i.lower())
        self.__guessed_letters = []
        self.__correct_letters = []
        self.__generate_board()

    def print_board(self):
        '''Returns a list of undescores representing each letter in a word'''
        return "".join(self.__board)

    def check_guess(self, guess):
        '''Compares guessed letter to current word'''
        self.__guessed_letters.append(guess)
        if guess in self.__current_word:
            self.__correct_guesses.append(guess)
            self.__update_board()
        else:
            return None

    def __update_board(self):
        '''Adds letters to board'''
        for i, char in enumerate(self.__current_word):
            if char in self.__correct_guesses:
                self.__board[i] = char

    def get_guessed(self):
        '''Return guessed letters'''
        return self.__guessed_letters

    def get_wrong(self):
        '''Returns bad guesses'''
        wrong = []
        for char in self.__guessed_letters:
            if char not in self.__correct_guesses:
                wrong.append(char)
        return wrong

    def get_correct(self):
        '''Returns correct guesses'''
        return self.__correct_guesses

    def get_word_length(self):
        '''returns word length'''
        return len(self.__current_word)

    def __generate_board(self):
        '''Adds blanks to board'''
        for i in self.__current_word:
            self.__board.append("_")
