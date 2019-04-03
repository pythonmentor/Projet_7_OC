import json

class Parser:

    def __init__(self, sentence):
        self.sentence = sentence

    def clean(self):
        self.transform_to_lowercase()
        self.remove_apostrophes
    
    def transform_to_lowercase(self, sentence):
        self.sentence = str(sentence)
        self.sentence = self.sentence.lower()
        return self.sentence

    def remove_apostrophes(self):
        """"""
        pass

    def remove_stop_words(self):
        """
        Permet d'ouvrir le fichier json et de filtré les mots dans une liste
        """
        with open('stop_words.json', 'r') as f:
            stop_words = json.load(f)

        cleaned_words = []
        # remove the stop_words from the sent
        for word in stop_words:
            if word not in stop_words:
                cleaned_words.append(word)
