import io
from pprint import pprint


class WordsFinder:

    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:

            with open(file_name, 'r', encoding='utf-8') as file:

                name = file.read().lower()
                punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for punct in punctuation:
                    name = name.replace(punct, '')

                all_words[file_name] = name.split()
        return all_words


    def find(self, word):
        places = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                places[name] = words.index(word.lower()) + 1
        return places


    def count(self, word):
        counters = {}

        for name, words in self.get_all_words().items():
            words_count = words.count(word.lower())
            counters[name] = words_count
        return counters


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
