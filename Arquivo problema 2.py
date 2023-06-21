import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
COR_FUNDO = (0, 0, 0)
COR_COBRA = (0, 255, 0)
COR_COMIDA = (255, 0, 0)

# Dimensões da janela do jogo
largura = 640
altura = 480

# Configuração da janela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game")

# Relógio para controlar os frames por segundo
relogio = pygame.time.Clock()

# Tamanho da cobrinha e da comida
tamanho = 20

# Fonte para exibir a pontuação
fonte = pygame.font.SysFont(None, 30)


def mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura / 2, altura / 2])


def jogo():
    # Posição inicial da cobrinha
    pos_x = largura / 2
    pos_y = altura / 2

    # Velocidade inicial da cobrinha
    delta_x = 0
    delta_y = 0

    # Lista para armazenar as partes do corpo da cobrinha
    corpo = []
    comprimento = 1

    # Posição aleatória da comida
    comida_x = round(random.randrange(0, largura - tamanho) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho) / 20.0) * 20.0

    # Variáveis para controlar o estado do jogo
    fim_jogo = False
    fim_loop = False

    while not fim_loop:
        while fim_jogo:
            tela.fill(COR_FUNDO)
            mensagem("Fim de Jogo! Pressione C para continuar ou S para sair.", COR_COBRA)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fim_loop = True
                    fim_jogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        fim_loop = True
                        fim_jogo = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_loop = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and delta_x != tamanho:
                    delta_x = -tamanho
                    delta_y = 0
                elif event.key == pygame.K_RIGHT and delta_x != -tamanho:
                    delta_x = tamanho
                    delta_y = 0
                elif event.key == pygame.K_UP and delta_y != tamanho:
                    delta_x = 0
                    delta_y = -tamanho
                elif event.key == pygame.K_DOWN and delta_y != -tamanho:
                    delta_x = 0
                    delta_y = tamanho

        if pos_x >= largura or pos_x < 0 or pos_y >= altura or pos_y < 0:
            fim_jogo = True

        pos_x += delta_x
        pos_y += delta_y

        tela.fill(COR_FUNDO)
        pygame.draw.rect(tela, COR_COMIDA, [comida_x, comida_y, tamanho, tamanho])

        cabeca = []
        cabeca.append(pos_x)
        cabeca.append(pos_y)
        corpo.append(cabeca)

        if len(corpo) > comprimento:
            del corpo[0]

        for parte in corpo[:-1]:
            if parte == cabeca:
                fim_jogo = True

        for segmento in corpo:
            pygame.draw.rect(tela, COR_COBRA, [segmento[0], segmento[1], tamanho, tamanho])

        pygame.display.update()

        if pos_x == comida_x and pos_y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho) / 20.0) * 20.0
            comprimento += 1

        relogio.tick(15)

    pygame.quit()


jogo()