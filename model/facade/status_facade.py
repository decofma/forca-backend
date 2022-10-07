from gera_palavra_temp_facade import CriaPalvraTemp

class RecebeStatusGame:
    def trata_status(self, param):
        parametro = param

        if parametro == 0:
            print("Jogo encerrado", parametro)
            return ("Jogo encerrado")

        if parametro == 1:
            CriaPalvraTemp().gera_palavra_temp()
            print("Jogo iniciado", parametro)
            return ("jogo iniciado")
        
if __name__ == "__main__":
    varClass = RecebeStatusGame()
    varClass.trata_status(1)
