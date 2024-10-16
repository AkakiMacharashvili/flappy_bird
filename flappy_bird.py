#extensions
#1) [0.5pt] Add background image
#2) [0.5pt] Add bird image
#3) [1pt] End screen - Instead of closing the application on colliding, display the ending screen with the result: win/lose.
#4) [0.5pt] Replay - Ask if the player wants to replay the game and if so start over. For example: if the player presses the space bar, you can start the game again.

import pygame




class Bird:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.speed = 0
        self.color = (255, 0, 0)
        bird_path = "enter photo path for bird"
        self.img = pygame.image.load(bird_path).convert_alpha()

        self.img = pygame.transform.rotozoom(self.img, 0, 0.05)

    def update(self):
        # Jump
        self.posY -= self.speed
        self.speed -= 1

    def render(self, screen):
        # Draw Image
        self.w, self.h = self.img.get_rect().size
        screen.blit(self.img, (self.posX - self.w / 2, self.posY - self.h / 2))


class App:

    def __init__(self):
        self.running = False
        self.clock = None
        self.screen = None
        self.ball = None

    def run(self):
        self.init()
        while self.running:
            self.update()
            self.render()
        while True:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT or keys[pygame.K_n]:
                    quit()
                elif keys[pygame.K_y]:
                    self.run()
            self.end()

    def init(self):
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("fluppyBird")
        background_path = "enter path for background"
        self.back = pygame.image.load(background_path).convert()
        self.back = pygame.transform.rotozoom(self.back, 0, 4.3)
        self.clock = pygame.time.Clock()

        self.running = True

        self.ball = Bird(10, 250)

    def update(self):
        self.events()

        self.ball.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # Keyboard
        keys = pygame.key.get_pressed()
        left, right, middle = pygame.mouse.get_pressed()
        if keys[pygame.K_SPACE] or left:
            self.ball.speed = 10

        self.ball.posX += 3
        self.ball.posY += 1
        if self.ball.posX >= 1180 or self.ball.posY <= 20 or self.ball.posY >= 780:
            self.running = False

        if 315 >= self.ball.posX >= 275 and self.ball.posY >= 370:
            self.running = False

        if 475 >= self.ball.posX >= 435 and self.ball.posY <= 230:
            self.running = False

        if 620 >= self.ball.posX >= 580 and self.ball.posY >= 320:
            self.running = False

        if 740 >= self.ball.posX >= 700 and self.ball.posY <= 165:
            self.running = False

        if 835 >= self.ball.posX >= 795 and self.ball.posY >= 220:
            self.running = False


    def render(self):
        self.screen.fill((0, 0, 0))

        self.ball.render(self.screen)

        self.screen.blit(self.back, (0, 0))

        self.ball.render(self.screen)
        pygame.draw.rect(self.screen, (255, 0, 255), pygame.Rect(300, 400, 10, 350))
        pygame.draw.rect(self.screen, (255, 0, 255), pygame.Rect(450, 0, 10, 200))
        pygame.draw.rect(self.screen, (255, 0, 255), pygame.Rect(590, 350, 10, 350))
        pygame.draw.rect(self.screen, (255, 0, 255), pygame.Rect(700, 0, 10, 175))
        pygame.draw.rect(self.screen, (255, 0, 255), pygame.Rect(800, 250, 10, 450))

        pygame.display.flip()
        self.clock.tick(60)

    def cleanUp(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()
        pygame.font.init()
        font = pygame.font.SysFont("roman", 35)
        str1 = ""
        if self.ball.posX >= 1180:
            str1 = "YOU WON"
        else:
            str1 = "YOU LOST"
        end_surface = font.render(
            str1 + ", Do you want to play again (y/n)?", True, (0, 255, 0))
        rect = end_surface.get_rect()
        rect.midtop = (1200 / 2, 700 / 2)
        self.screen.blit(end_surface, rect)
        pygame.display.flip()




    def end(self):
        self.screen.fill((0, 0, 0))

        pygame.font.init()
        font = pygame.font.SysFont("roman", 35)
        str1 = ""
        if self.ball.posX >= 1180:
            str1 = "YOU WON"
        else:
            str1 = "YOU LOST"
        end_surface = font.render(
            str1 + ", Do you want to play again (y/n)?", True, (0, 255, 0))
        rect = end_surface.get_rect()
        rect.midtop = (1200 / 2, 700 / 2)
        self.screen.blit(end_surface, rect)
        pygame.display.flip()


if __name__ == "__main__":
    app = App()
    app.run()
