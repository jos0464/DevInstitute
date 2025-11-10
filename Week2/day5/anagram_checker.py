# anagram_checker.py
import string

class AnagramChecker:
    def __init__(self, wordlist_file="words.txt"):
        """
        Charge la liste des mots depuis un fichier texte.
        Chaque mot est converti en minuscule pour comparaison insensible à la casse.
        """
        with open(wordlist_file, 'r') as file:
            self.words = set(line.strip().lower() for line in file)

    def is_valid_word(self, word):
        """
        Vérifie si le mot donné existe dans la liste des mots.
        """
        return word.lower() in self.words

    def is_anagram(self, word1, word2):
        """
        Vérifie si word1 et word2 sont des anagrammes.
        """
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        """
        Retourne une liste de tous les anagrammes du mot donné.
        """
        word = word.lower()
        anagrams = [w for w in self.words if self.is_anagram(word, w) and w != word]
        return anagrams
