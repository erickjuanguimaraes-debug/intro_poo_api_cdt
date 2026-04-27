class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100

    def fazer_chamadas(self, custo_bateria):
        print(f"\n--- Chamada no {self.modelo} ---")

        try:
            custo = int(custo_bateria)
            self.bateria -= custo
        except TypeError:
            print("ERRO: O custo da bateria deve ser um número!")
        except ValueError:
            print("ERRO: O custo da bateria deve ser um número válido!")
        else:
            print(f"Sucesso! bateria atual: {self.bateria}%")
        finally:
            print("Sistema finalizado.")



meu_celular = Celular("Samsung", "S24")
meu_celular.fazer_chamadas("10")