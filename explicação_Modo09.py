def aula_tratamento_erros():
    print("---Desafio 1: Divisão---")

try:
    Numerador = int(input("Digita o numerador:"))
    denominador = int(input("Digita o denominador:"))
    resultado = Numerador / denominador
    
except ValueError:
    print("Erro: Digita apenas números inteiros!")
except ZeroDivisionError:
    print("Erro Não podes dividir por zero.")
except Exception as erro:
    print(f"Erro inesperado: {erro}")
else:
    print("Sucesso! Resultado: {resultado}")
finally:
    print("---Fim da Divisão---")
    aula_tratamento_erros()
    ...