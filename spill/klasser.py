import pygame
import random
from os import path


def stein_saks_papir(type1: int, type2: int) -> int:
    """
    Tar inn to tall der 0 == stein, 1 == saks, 2 == papir
    Retunerer tallet til vinneren
    """

    if type1 == 0:
        if type2 == 2:
            return type2
        return type1
    if type1 == 1:
        if type2 == 0:
            return type2
        return type1
    if type1 == 2:
        if type2 == 1:
            return type2
        return type1


class Bilder:
    def __init__(self):
        pass

    def last_bilder(self, storrelse: int):
        self.stein = pygame.image.load(path.join("ressurser", "stein.png"))
        self.saks = pygame.image.load(path.join("ressurser", "saks.png"))
        self.papir = pygame.image.load(path.join("ressurser", "papir.png"))
        self.bilder: list[pygame.Surface] = [self.stein, self.saks, self.papir]
        for i, bilde in enumerate(self.bilder):
            self.bilder[i] = pygame.transform.smoothscale(
                bilde, (storrelse, storrelse))


bilder = Bilder()


class SpillBrett:
    def __init__(self, vindu: pygame.Surface, antall=100, storrelse=30):
        self.storrelse = storrelse
        self.vindu = vindu
        self.bredde = self.vindu.get_width()
        self.hoyde = self.vindu.get_height()
        bilder.last_bilder(self.storrelse)
        self.spillobjekter: list[SpillObjekt] = [
            SpillObjekt(self) for i in range(antall)]

    def logikk(self):
        for spillobjekt in self.spillobjekter:
            spillobjekt.logikk()

    def tegn(self):
        for spillobjekt in self.spillobjekter:
            spillobjekt.tegn()


class SpillObjekt:
    def __init__(self, spillbrett: SpillBrett):
        self.spillbrett = spillbrett
        self.x = random.randint(
            0, self.spillbrett.bredde - self.spillbrett.storrelse)
        self.y = random.randint(
            0, self.spillbrett.hoyde - self.spillbrett.storrelse)
        self.xvel = 1 if random.random() > 0.5 else -1
        self.yvel = 1 if random.random() > 0.5 else -1
        self.type = random.randint(0, 2)

    def kolliderer(self, spillobjekt):
        if (
            abs(self.x - spillobjekt.x) < self.spillbrett.storrelse
            and abs(self.y - spillobjekt.y) < self.spillbrett.storrelse
        ):
            return True

    def logikk(self):
        self.x += self.xvel
        self.y += self.yvel

        if self.x + self.spillbrett.storrelse > self.spillbrett.bredde or self.x < 0:
            self.xvel = -self.xvel

        if self.y + self.spillbrett.storrelse > self.spillbrett.hoyde or self.y < 0:
            self.yvel = -self.yvel

        for spillobjekt in self.spillbrett.spillobjekter:
            if self.kolliderer(spillobjekt):
                self.type = stein_saks_papir(self.type, spillobjekt.type)

    def tegn(self):
        bilde = bilder.bilder[self.type]
        self.spillbrett.vindu.blit(bilde, (self.x, self.y))
