# Criar a função principal do programa
def main():
    # Imprimir uma mensagem de boas-vindas
    print("Olá, mundo! Este é o meu primeiro programa em Python.")
    
# Criar função para calcular a média de uma lista de números
def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

# Criar uma função para calcular a média de uma lista de números
# usando a biblioteca numpy
import numpy as np
def calcular_media_numpy(numeros):
    if len(numeros) == 0:
        return 0
    return np.mean(numeros)
    
# Verificar se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
    # Exemplo de uso da função calcular_media
    numeros = [10, 20, 30, 40, 50]
    media = calcular_media(numeros)
    print(f"A média dos números {numeros} é: {media}")
    
    media_numpy = calcular_media_numpy(numeros)
    print(f"A média dos números {numeros} usando numpy é: {media_numpy}")
    
    # Obter dois números do usuário e calcular a soma
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    print(f"A soma de {num1} e {num2} é: {soma}")
    