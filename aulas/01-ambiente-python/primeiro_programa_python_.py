# Declarar a função principal
def main():
    # Imprimir uma mensagem de boas-vindas
    print("Olá, mundo! Este é o meu primeiro programa em Python.")
    
    # Realizar uma operação simples
    a = 5
    b = 3
    soma = a + b
    print("A soma de", a, "e", b, "é:", soma)
    
# Criar uma função para calcular a média de uma lista de números
def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

# Usando funções da bliblioteca numpy para calcular a média
import numpy as np
def calcular_media_numpy(numeros):
    return np.mean(numeros)
    
# Verificar se o script está sendo executado diretamentee chamar a função principal
if __name__ == "__main__":
    main()
    lista_numeros = [1, 2, 3, 4, 5]
    media = calcular_media(lista_numeros)
    print("A média dos números", lista_numeros, "é:", media)
    
    media_numpy = calcular_media_numpy(lista_numeros)
    print("A média calculada usando numpy é:", media_numpy)

    import sys
    print("Python executando:", sys.executable)