import pygame

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

X = 400
Y = 400

display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Drawing')
display_surface.fill(white)

pygame.draw.ellipse(display_surface, blue,(120, 120, 180, 180), 5)
pygame.draw.polygon(display_surface, blue,
                    [(210, 130), (290, 210),
                     (210, 290), (130, 210)], 5)
pygame.draw.polygon(display_surface, blue,
                    [(160, 110), (270, 110),
                     (330, 210), (270, 308), (160, 308), (90, 210)], 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()