"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """Finds random words from a dictionary file with one word per line"""

    def __init__(self, path):
        """ Initializes dictionary list, calling make_word_list() and prints number of words parsed from file """
        try:
            self.word_list = self.make_word_list(path)
            if(type(self) == 'WordFinder'):
                print(f"{len(self.word_list)} words in file")
        except FileNotFoundError as exc:
            print("Invalid file path")

    def make_word_list(self,path):
        """ Populates and returns list of lines from file, removing line break characters """
        file_obj = open(path,'r')
        word_list = []
        for line in file_obj:
            line = line.replace('\n','')
            word_list.append(line)
        file_obj.close()
        return word_list

    def random(self):
        """ Returns random word from list"""
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """Finds random words from a categorized dictionary file with potential spaces and comments"""

    def __init__(self,path):
        super().__init__(path)
        self.adjust_word_list()

    def adjust_word_list(self):
        count = len(self.word_list) - 1
        while count >= 0:
            line = self.word_list[count]
            if not line or line.startswith('#'):
                self.word_list.pop(count)
            count-=1
        print(f"{len(self.word_list)} words in file")


    


