import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da tela
largura = 800
altura = 600
tamanho_celula = 20

# Definição das cores
cor_fundo = (0, 0, 0)
cor_cobra = (0, 255, 0)
cor_comida = (255, 0, 0)

# Criação da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')

# Relógio para controle de FPS
relogio = pygame.time.Clock()

# Função para desenhar a cobra
def desenhar_cobra(cobra):
    for posicao in cobra:
        pygame.draw.rect(tela, cor_cobra, (posicao[0], posicao[1], tamanho_celula, tamanho_celula))

# Função para gerar uma nova posição para a comida
def gerar_comida():
    x = random.randint(0, largura - tamanho_celula)
    y = random.randint(0, altura - tamanho_celula)
    return (x // tamanho_celula * tamanho_celula, y // tamanho_celula * tamanho_celula)

# Função principal do jogo
def jogo_snake():
    # Posição inicial da cobra
    cobra = [(largura // 2, altura // 2)]
    direcao = 'direita'

    # Geração da primeira comida
    comida = gerar_comida()

    # Variáveis para controle do jogo
    jogo_acabou = False
    while not jogo_acabou:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_acabou = True

            # Verifica as teclas pressionadas para controlar a direção da cobra
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w and direcao != 'baixo':
                    direcao = 'cima'
                elif evento.key == pygame.K_s and direcao != 'cima':
                    direcao = 'baixo'
                elif evento.key == pygame.K_a and direcao != 'direita':
                    direcao = 'esquerda'
                elif evento.key == pygame.K_d and direcao != 'esquerda':
                    direcao = 'direita'

        # Movimentação da cobra
        if direcao == 'cima':
            nova_posicao = (cobra[0][0], cobra[0][1] - tamanho_celula)
        elif direcao == 'baixo':
            nova_posicao = (cobra[0][0], cobra[0][1] + tamanho_celula)
        elif direcao == 'esquerda':
            nova_posicao = (cobra[0][0] - tamanho_celula, cobra[0][1])
        elif direcao == 'direita':
            nova_posicao = (cobra[0][0] + tamanho_celula, cobra[0][1])

        # Verifica se a cobra colidiu com as bordas da tela
        if nova_posicao[0] < 0 or nova_posicao[0] >= largura or nova_posicao[1] < 0 or nova_posicao[1] >= altura:
            jogo_acabou = True

        # Verifica se a cobra colidiu com o próprio corpo
        if nova_posicao in cobra[1:]:
            jogo_acabou = True

        # Adiciona a nova posição da cabeça da cobra
        cobra.insert(0, nova_posicao)

        # Verifica se a cobra comeu a comida
        if cobra[0] == comida:
            comida = gerar_comida()
        else:
            cobra.pop()

        # Preenche o fundo da tela com a cor de fundo
        tela.fill(cor_fundo)

        # Desenha a comida
        pygame.draw.rect(tela, cor_comida, (comida[0], comida[1], tamanho_celula, tamanho_celula))

        # Desenha a cobra
        desenhar_cobra(cobra)

        # Atualiza a tela
        pygame.display.update()

        # Define a velocidade do jogo
        relogio.tick(10)

    # Encerra o Pygame
    pygame.quit()

# Inicia o jogo
jogo_snake()