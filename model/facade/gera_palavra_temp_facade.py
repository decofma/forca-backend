from util.word_gen import GeraPalavra

class CriaPalvraTemp:   
    

    def gera_palavra_temp(self):
        palavra_temp = GeraPalavra().escolhe_palavra()
        with open('arquivo_palavra_temp.txt', 'w', encoding='utf-8') as temp:
            temp.write(palavra_temp)

if __name__ == "__main__":
    varClass = CriaPalvraTemp()
    varClass.gera_palavra_temp()
