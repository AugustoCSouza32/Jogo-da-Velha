# Valida a entrada do usuário e retorna os indices da matriz
def valida_entrada(entrada: str) -> tuple[int, int] | None:
    if len(entrada) != 2:
        print("Entrada Inválida: Deve conter exatamente 2 caracteres.")
        return None

    if entrada.isdigit():
        lin = int(entrada[0])
        col = int(entrada[1])
        return lin, col
    else:
        print("Entrada Inválida: Os caracteres devem ser números.")
        return None





#Jogo roda aqui
matriz_tabuleiro: list[str] = [['a' for col in range(3)] for lin in range(3)]

while True:
    entrada = input("Informe a posição que quer jogar: [lin][col]: ")
    valida = valida_entrada(entrada)

    if valida is not None:
        lin, col = valida
        print(f"Linha: {lin}\nColuna: {col}")
        break
