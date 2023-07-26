# your code goes here!
import pdb
class Anagram():
    def __init__(self, word, list = []):
        self.list = list
        self.word = word

    def get_list(self):
        return self._list

    def set_list(self, list):
        self._list = list

    def get_word(self):
        return self._word
    
    def set_word(self, word):
        self._word = word

    def match(self, list):
        my_list = []
        for ele in list:
            if(sorted(self.word) == sorted(ele)):
                my_list += [ele]
        return my_list
        
    list = property(get_list, set_list)
    word = property(get_word, set_word)