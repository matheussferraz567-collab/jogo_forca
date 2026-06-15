# BIBLIOTECA PARA FUNÇÕES E ESCOLHA ALEATÓRIA
import random


# FUNÇÃO RESPONSÁVEL POR PREPARAR O JOGO
# Aqui são criadas a palavra secreta, a palavra oculta e o conjunto de tentativas
def iniciar_jogo():

    palavras = ["COELHO", "JOANINHA", "DINOSSAURO"]

    # Escolhe uma palavra aleatória da lista
    palavra_secreta = random.choice(palavras)

    # Apenas para testes durante o desenvolvimento
    print(palavra_secreta)

    # Lista que irá mostrar as letras descobertas
    palavra_oculta = []

    # Cria os "_" de acordo com o tamanho da palavra
    for letra in palavra_secreta:
        palavra_oculta.append("_")

    print(palavra_oculta)

    # Set usado para evitar letras repetidas
    letras_tentativas = set()

    return palavra_secreta, palavra_oculta, letras_tentativas


# RECEBE OS DADOS INICIAIS DO JOGO
palavra_secreta, palavra_oculta, letras_tentativas = iniciar_jogo()


# FUNÇÃO RESPONSÁVEL POR PROCESSAR A LETRA DIGITADA
def processar_tentativa(letra, palavra_secreta, palavra_oculta, letras_tentativas):

    # Verifica se a letra já foi utilizada anteriormente
    if letra in letras_tentativas:
        print("Você já tentou essa letra!")
        return

    # Adiciona a letra no conjunto de tentativas
    letras_tentativas.add(letra)

    # Verifica se a letra existe na palavra secreta
    if letra in palavra_secreta:

        # Percorre toda a palavra para atualizar as posições corretas
        for posicao, caractere in enumerate(palavra_secreta):

            if caractere == letra:
                palavra_oculta[posicao] = letra

    else:
        print("Letra incorreta!")


# LOOP PRINCIPAL DO JOGO
# Mantém a partida funcionando até o jogador descobrir toda a palavra
while True:

    # Mostra a palavra oculta atualizada
    print(" ".join(palavra_oculta))

    # Recebe a letra digitada pelo jogador
    letra = input("Digite uma letra: ").upper()

    # Chama a função que processa a tentativa
    processar_tentativa(
        letra,
        palavra_secreta,
        palavra_oculta,
        letras_tentativas
    )

    # Verifica se ainda existem "_" na palavra
    if "_" not in palavra_oculta:
        print("Parabéns! Você venceu!")
        print("Palavra:", palavra_secreta)
        break
    

