class MenuScene:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 74)
        self.title = self.font.render("Simple Game", True, (255, 255, 255))
        self.start_text = self.font.render("Press Enter to Start", True, (255, 255, 255))
        self.quit_text = self.font.render("Press Q to Quit", True, (255, 255, 255))

    def display(self):
        self.game.screen.fill((0, 0, 0))
        self.game.screen.blit(self.title, (self.game.screen.get_width() // 2 - self.title.get_width() // 2, 100))
        self.game.screen.blit(self.start_text, (self.game.screen.get_width() // 2 - self.start_text.get_width() // 2, 300))
        self.game.screen.blit(self.quit_text, (self.game.screen.get_width() // 2 - self.quit_text.get_width() // 2, 400))
        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.change_scene("play")
                if event.key == pygame.K_q:
                    self.game.running = False