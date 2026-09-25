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

# Função que cria a matriz, valida a posição da jogada e insere o valor no tabuleiro.
# Retorna a matriz com os valores inseridos, retorna se a posição é inválida.
def insere_jogada(lin:int, col:int,jogador:str):
    matriz_tabuleiro: list[list[str | None]] = [[None for c in range(3)] for l in range(3)]

    if matriz_tabuleiro[lin][col] is not None:
        print("Posição oculpada! Tente outra casa.")
        return None
    else:
        matriz_tabuleiro[lin][col] = jogador
        return matriz_tabuleiro

# Função que verifica qual é o jogador e alterna as jogadas.
def trocar_jogador(jogador:str):
    if jogador == 'X':
        return 'O'
    else:
        return 'X'

# Função que vincula o jogador com a peça dele no jogo.
def jogadores (jogador_1:str, jogador_2:str, jogador:str):
    jogador_x = jogador_1
    jogador_o = jogador_2

    if jogador == 'X':
        return jogador_x
    else:
        return jogador_o

# Função que verifica a vitória ou empate
def verifica_vitoria(tabuleiro:list[list[str|None]]):
    cont_x = 0
    cont_o = 0
    vitoria = False
    for lin in range(3):
        for col in range(3):
            if tabuleiro[lin][col] == 'X':
                cont_x += 1
            elif tabuleiro[lin][col] == 'O':
                cont_o += 1
        if cont_x == 3:
            vitoria = True
            return lin, vitoria
        
        cont_x = 0
        cont_o = 0
             

             
#Jogo roda aqui
while True:
    entrada = input("Informe a posição que quer jogar: [lin][col]: ")
    valida = valida_entrada(entrada)

    if valida is not None:
        lin, col = valida
        print(f"Linha: {lin}\nColuna: {col}")
        break
