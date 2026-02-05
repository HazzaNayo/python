class Game:
    def __init__(self):
        self.running = True
        self.current_scene = None

    def start(self):
        self.setup()
        while self.running:
            self.handle_events()
            self.update()
            self.render()

    def setup(self):
        # Initialize the first scene here
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        if self.current_scene:
            self.current_scene.update()

    def render(self):
        if self.current_scene:
            self.current_scene.render()
        pygame.display.flip()

    def change_scene(self, new_scene):
        self.current_scene = new_scene
        self.current_scene.setup()