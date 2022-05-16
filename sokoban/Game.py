import pygame
from Player import Player
from Board import Board

class Game:
    def __init__(self, board):
        # RUNNING définit si le jeu est lancé
        self.RUNNING = False
        # Screen stock l'objet de la fenêtre pygame
        self.screen = 0
        # Définition de la taille de la fenêtre
        self.SIZE = (600, 600)
        # Attribution du terrain
        self.BOARD = Board(board, self.SIZE)
        # Attribution du player
        self.PLAYER = Player(self.BOARD)
        
        self.sprites = []

        self.logo = None

    def run(self):
        # Run lance le jeu
        self.RUNNING = True
        # Initialisation de pygame
        pygame.init()
        # Chargements des assets
        self.load()

        # Initialisation de la fenêtre et attribution de l'objet à self.screen
        self.screen = pygame.display.set_mode(self.SIZE)
        # Changement du titre de la fenêtre
        pygame.display.set_caption('Simpsoban')
        pygame.display.set_icon(self.logo)
        self.draw_board()

        # Lancement de la boucle du jeu
        while self.RUNNING:
            # Mise à jour des sprites
            pygame.display.flip()
            # Traitement des évènements de PyGame
            for event in pygame.event.get():
                # Check si l'user quitte le jeu
                if event.type == pygame.QUIT:
                    self.RUNNING = False
                # Évenements clavier
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.PLAYER.move('left')
                    if event.key == pygame.K_RIGHT:
                        self.PLAYER.move('right')
                    if event.key == pygame.K_UP:
                        self.PLAYER.move('up')
                    if event.key == pygame.K_DOWN:
                        self.PLAYER.move('down')
                    self.draw_board()
                        

    def draw_board(self):

        y = x = 0
        for r in range(self.BOARD.ROWS):
            self.screen.blit(self.sprites[0], (x, y))
            x = 0
            for c in range(self.BOARD.COLS):
                self.screen.blit(self.sprites[0], (x, y))
                x += self.BOARD.ROW_WIDTH
            y += self.BOARD.COL_WIDTH

        y = x = 0

        for r in range(len(self.BOARD.board)):
            x = 0
            for c in range(len(self.BOARD.board[r])):
                if self.BOARD.board[r][c] != 0:
                    self.screen.blit(self.sprites[self.BOARD.board[r][c]], (x, y))
                if self.BOARD.board[r][c] == 2:
                    self.PLAYER.pos = (r, c)
                x += self.BOARD.ROW_WIDTH
            y += self.BOARD.ROW_WIDTH


    def load(self):
        print("Loading...")

        self.logo = pygame.image.load('./assets/logo.png')

        wall = pygame.image.load('./assets/wall.png')
        wall = pygame.transform.scale(wall, (self.BOARD.ROW_WIDTH, self.BOARD.COL_WIDTH))
        
        ground = pygame.image.load('./assets/ground.png')
        ground = pygame.transform.scale(ground, (self.BOARD.ROW_WIDTH, self.BOARD.COL_WIDTH))
        
        player = pygame.image.load('./assets/front-homer.png')
        player = pygame.transform.scale(player, (self.BOARD.ROW_WIDTH, self.BOARD.COL_WIDTH))
        
        donut = pygame.image.load('./assets/donut.png')
        donut = pygame.transform.scale(donut, (self.BOARD.ROW_WIDTH, self.BOARD.COL_WIDTH))

        cart = pygame.image.load('./assets/cart.png')
        cart = pygame.transform.scale(cart, (self.BOARD.ROW_WIDTH, self.BOARD.COL_WIDTH))

        self.sprites = [
            ground,
            wall,
            player,
            donut,
            cart
        ]

        print("Finished :)")