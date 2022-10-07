from pickle import NONE


class RecebeLetra: 

    def __init__(self):
        self.contador = 0 
        self.tentativa = 0
        self.acertos = 0
        self.chances = 7

    def ler_arquivo_temp(self):

        arquivo = "arquivo_palavra_temp.txt"

        with open(arquivo, 'r', encoding='utf-8') as f:
            for word in f:
                word = word.strip().lower()
                palavra_da_rodada = word

        return palavra_da_rodada

    def oculta_palavra(self):
        palava_oculta = None
        palava_oculta = []
        palavra = self.ler_arquivo_temp()
        for k in enumerate(palavra):
            if k:
                palava_oculta.append("_")
        return palava_oculta


    def jogada(self, param: dict):
        letra     = param["letter"]
        status    = ""
        palavra   = self.ler_arquivo_temp()
        print("***********************************")
        print ("log jogada palavra", palavra, type(palavra))
        print("***********************************")
        oculto    = self.oculta_palavra        
        
        for i, char in enumerate(palavra):
            print("***********************************")
            print ("log jogada i e char", i, char)
            print("***********************************")
            if char == letra:
                oculto[i] = letra
                self.acertos = self.acertos + 1
                print("log acertos", self.acertos)
                return 'acerto'  
            else:
                self.tentativa = self.tentativa + 1
                print("log tentativa", self.tentativa)
                return 'erro'

        if self.tentativa == self.chances:
            status == "Derrota"
            

        if self.acertos == enumerate(palavra):                
            status == "Vitoria"
            
         

if __name__ == "__main__":
    varClass = RecebeLetra()
    varClass.jogada("r")
