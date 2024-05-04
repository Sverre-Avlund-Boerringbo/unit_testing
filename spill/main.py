import pygame
from klasser import SpillBrett

BREDDE = 720
HOYDE = 640
FPS = 30

vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

spillbrett = SpillBrett(vindu)

fortsett = True
while fortsett:
    dt = klokke.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fortsett = False

    keys = pygame.key.get_pressed()

    spillbrett.logikk()
    if keys[pygame.K_SPACE]:
        for i in range(5):
            spillbrett.logikk()

    vindu.fill((0, 0, 0))
    spillbrett.tegn()

    pygame.display.flip()

pygame.quit()
