from pickle import NONE


class RecebeLetra:  
    
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
        lacunas   = 0
        tentativa = 0
        acertos   = 0
        letra     = param["letter"]
        status    = ""
        chances   = 7
        palavra   = self.ler_arquivo_temp
        oculto    = self.oculta_palavra        
        
        for i, char in enumerate(palavra):
            if char == letra:
                oculto[i] = letra
                acertos = acertos + 1
                print("log acertos", acertos)
                return 'acerto'  
            else:
                tentativa = tentativa + 1
                print("log tentativa", tentativa)
                return 'erro'

        if tentativa == chances:
            status == "Derrota"
            

        if acertos == enumerate(palavra):                
            status == "Vitoria"
            
        

# if __name__ == "__main__":
#     varClass = RecebeLetra()
#     varClass.jogada("r")
