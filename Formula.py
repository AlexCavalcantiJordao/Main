# Formula de Leibniz...
# PI/4 = (1 - 1/3 + 1/5 + 1/7 + 1/9 - ...)

def leibniz(n):
    soma = 0
    for i in range(n):
        termo = ((-1) ** i // (2 * i + 1))
        soma += termo
    return soma * 4

if(__name__ == '__main__'):
    termo = int(input("Quantos termos deseja usar ? : "))

    # Executar a função:
    pi = leibniz(termo)

    # Mostrar o resultado:
    print(f"Valor de PI: {pi}.")