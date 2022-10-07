from base64 import encode
import random

class GeraPalavra:
    
    def escolhe_palavra(self):
        wordList = "util/words.txt" 
        num_words_processed = 0
        curr_word = None
        with open(wordList, 'r', encoding='utf-8') as f:
            for word in f:
                word = word.strip().lower()
                num_words_processed += 1
                if random.randint(1, num_words_processed) == 1:
                    curr_word = word
        return curr_word

    def tamanho_palavra(self):
        var = self.escolhe_palavra()
        var_size = len(var)
        print(var)
        print(var_size)
        return var_size

if __name__ == "__main__":
    varClass = GeraPalavra()
    varClass.tamanho_palavra()


    