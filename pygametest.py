import pygame
import sys


def desenhar_img_circle_vermelho(surface, coluna, linha):
    x = tabuleiro_x + (coluna + 1) * (tamanho_casa + margem) - 20 / 2
    y = tabuleiro_y + (linha + 1) * (tamanho_casa + margem) - 20 / 2
    imagem_redimensionada = pygame.transform.scale(imagem, (20, 20))
    tela.blit(imagem_redimensionada, (x,y))

# Função para desenhar o círculo vermelho
def desenhar_circulo_vermelho(surface, coluna, linha):
    x = tabuleiro_x + (coluna + 1) * (tamanho_casa + margem) - margem / 2
    y = tabuleiro_y + (linha + 1) * (tamanho_casa + margem) - margem / 2
    pygame.draw.circle(surface, cor_vermelha, [x, y], 4)

# Função para desenhar o sinal de "+" vermelho
def desenhar_sinal_mais_vermelho(surface, coluna, linha):
    x = tabuleiro_x + (coluna + 1) * (tamanho_casa + margem) - 5 / 2
    y = tabuleiro_y + (linha + 1) * (tamanho_casa + margem) - 5 / 2
    pygame.draw.line(surface, cor_vermelha, (x - 10, y), (x + 10, y), 2)  # Linha horizontal
    pygame.draw.line(surface, cor_vermelha, (x, y - 10), (x, y + 10), 2)  # Linha vertical

# Inicialização do Pygame
pygame.init()

# Configurações do tabuleiro
tamanho_casa = 38
margem = 4
nr_linhas = 9
nr_colunas = 9
largura, altura = nr_linhas * (tamanho_casa + margem) - margem, nr_colunas * (tamanho_casa + margem) - margem


pygame.display.set_caption("Exemplo de Imagem em Pygame")

# Carrega a imagem
imagem = pygame.image.load("/Users/goncalocosta/Desktop/fac/3ano/2semestre/IA/IA_proj/more.png")

# Obtém o retângulo da imagem para obter as dimensões
retangulo_imagem = imagem.get_rect()

# Cores
cor_branca = (255, 255, 255)
cor_cinza = (200, 200, 200)
cor_vermelha = (255, 0, 0)
cor_azul = (0, 0, 255)
cor_preto = (0, 0, 0)

# Criar a janela
tela = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tabuleiro de Xadrez")

# Pintar a parte de trás do ecrã de preto
tela.fill(cor_cinza)

# Calcular a posição do canto superior esquerdo do tabuleiro para centralizá-lo
tabuleiro_x = 800 // 2 - largura // 2
tabuleiro_y = 800 // 2 - altura // 2

# Loop principal
for linha in range(nr_linhas):
    for coluna in range(nr_colunas):
        if coluna == 0 or coluna == nr_colunas-1 or linha == 0 or linha == nr_linhas-1:
            cor = cor_preto  # Pinte as bordas laterais de preto
        else:
            cor = cor_branca
        pygame.draw.rect(tela, cor, [tabuleiro_x + coluna * (tamanho_casa + margem), tabuleiro_y + linha * (tamanho_casa + margem), tamanho_casa, tamanho_casa])

        # Adicionar divisão entre todas as casas
        pygame.draw.rect(tela, cor_cinza, [tabuleiro_x + coluna * (tamanho_casa + margem) + tamanho_casa, tabuleiro_y + linha * (tamanho_casa + margem), margem, tamanho_casa])
        pygame.draw.rect(tela, cor_cinza, [tabuleiro_x + coluna * (tamanho_casa + margem), tabuleiro_y + linha * (tamanho_casa + margem) + tamanho_casa, tamanho_casa, margem])

# Adicionar círculos vermelhos nos vértices, evitando os vértices indesejados
for linha in range(1,18):
    for coluna in range(1,18):
        if linha < nr_linhas-2 and coluna < nr_colunas-2:
            #desenhar_circulo_vermelho(tela, coluna, linha)
            #desenhar_sinal_mais_vermelho(tela, coluna, linha)
            desenhar_img_circle_vermelho(tela, coluna, linha)
            
# Atualizar a tela
pygame.display.flip()

# Loop do jogo
terminou = False
while not terminou:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminou = True

# Encerrar o Pygame
pygame.quit()
sys.exit()
