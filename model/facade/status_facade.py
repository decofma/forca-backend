from model.facade.gera_palavra_temp_facade import CriaPalvraTemp

class RecebeStatusGame:
    def trata_status(self, param: dict):
        parametro = param

        if parametro["status"] == 0:
            print("Jogo encerrado", parametro)
            return ("Jogo encerrado")

        if parametro["status"] == 1:
            CriaPalvraTemp().gera_palavra_temp()
            print("Jogo iniciado", parametro)
            return ("jogo iniciado")
        
