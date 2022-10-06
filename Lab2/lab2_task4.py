import string
import os


class ProcessFile:

    def __init__(self, file_name):
        if not os.path.exists(file_name):
            raise FileNotFoundError("File not found")
        self.file_name = file_name

    def calculate_chars(self):
        with open(self.file_name, "r") as file:
            not_chars = string.whitespace
            return sum(len(line) - line.count(char) for char in not_chars for line in file)

    def calculate_words(self):
        with open(self.file_name, "r") as file:
            not_chars = string.whitespace
            words_num = 0
            ind = 0
            for line in file:
                for char in line:
                    if char not in not_chars:
                        if not ind:
                            words_num += 1
                            ind = 1
                    else:
                        ind = 0
            return words_num

    def calculate_sentences(self):
        with open(self.file_name, "r") as file:
            end_of_sentence = ("!", ".", "?")
            sentences_num = 0
            ind = 0
            for line in file:
                for char in line:
                    if char in end_of_sentence:
                        if not ind:
                            sentences_num += 1
                            ind = 1
                    else:
                        ind = 0
            return sentences_num


file1 = ProcessFile("test1.txt")
print(file1.calculate_chars())
print(file1.calculate_words())
print(file1.calculate_sentences())
