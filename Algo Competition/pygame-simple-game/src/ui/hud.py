class HUD:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.health = 100

    def update(self, score, health):
        self.score = score
        self.health = health

    def draw(self):
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        health_text = self.font.render(f'Health: {self.health}', True, (255, 255, 255))
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(health_text, (10, 50))