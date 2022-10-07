from word_gen_facede import GeraPalavra


class RecebeLetra:   
    
    def ler_arquivo_temp(self):

        arquivo = "arquivo_palavra_temp.txt"

        with open(arquivo, 'r', encoding='utf-8') as f:
            for word in f:
                word = word.strip().lower()
                palavra_da_rodada = word

        return palavra_da_rodada

    def jogada(self, param):
        tentativa = 0
        acertos = 0
        erro = True
        letra = param
        chances = 7
        palavra_retorno = None
        

        palavra_secreta = self.ler_arquivo_temp()

        palavra_retorno = []
        for k in enumerate(palavra_secreta):
            if k:
                palavra_retorno.append("_")
        palavra = palavra_secreta
        palavraOculta = palavra_retorno
        
        for i, char in enumerate(palavra):
            if char == letra:
                erro = False
                palavraOculta[i] = letra
                acertos += 1
                              

                if acertos == enumerate(palavra):
                    return ('vitoria')
        if erro == True:
            tentativa += 1
            if tentativa == chances:
                return('derrota')
        

if __name__ == "__main__":
    varClass = RecebeLetra()
    varClass.jogada("r")
