import pygame, numpy, sys
#from button import Button

WIDTH = 400
HEIGHT = 300
BACKGROUND = (0, 0, 0)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.center = [startx, starty]
        self.vsp = 0 # скорость вертикального перемещения
        self.gravity = 1

        #self.play_button = Button(self, "Play")

        #self.game_active = False
        pygame.display.set_caption("2D AVgame [для выхода нажми Q]")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Player(Sprite):
    def __init__(self, startx, starty):
        super().__init__("image/player_idle1.png", startx, starty)
        self.stand_image = self.image
        self.jump_image = pygame.image.load("image/player_jump.png")

        self.walk_cycle = [pygame.image.load(f"image/player_run_{i:0>2}.png") for i in range(1,12)]
        self.animation_index = 0
        self.facing_left = False

        self.speed = 4
        self.jumpspeed = 20
        self.gravity = 1

        self.min_jumpspeed = 1
        self.prev_key = pygame.key.get_pressed()
    
    def jump_animation(self):
        self.image = self.jump_image
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

    def walk_animation(self):
        self.image = self.walk_cycle[self.animation_index]
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

        if self.animation_index < len(self.walk_cycle)-1:
            self.animation_index += 1
        else:
            self.animation_index = 0

    def update(self, boxes):
        hsp = 0 # скорость горизонтального перемещения

        onground = self.check_collision(0, 1, boxes)

        key = pygame.key.get_pressed()

        self.move(hsp, self.vsp, boxes)

        if key[pygame.K_LEFT]:
            self.facing_left = True
            self.walk_animation()
            self.move(-self.speed, 0, boxes)
        elif key[pygame.K_RIGHT]:
            self.facing_left = False
            self.walk_animation()
            self.move(self.speed, 0, boxes)
        else:
            self.image = self.stand_image
       
        if key[pygame.K_UP] and onground:
            self.vsp = -self.jumpspeed
        
        if key[pygame.K_q]:
            sys.exit()

        # variable height jumping
        if self.prev_key[pygame.K_UP] and not key[pygame.K_UP]:
            if self.vsp < -self.min_jumpspeed:
                self.vsp = -self.min_jumpspeed
        
        self.prev_key = key

        if self.vsp < 10 and not onground: # 9.8 округлено до 10
            self.vsp += self.gravity
        
        if self.vsp > 0 and onground:
            self.vsp = 0
    
    def check_collision(self, x, y, boxes):
        self.rect.move_ip([x,y])
        collide = pygame.sprite.spritecollideany(self, boxes)
        self.rect.move_ip([-x,-y])
        return collide
    
    def move(self, x, y, boxes):
        dx = x
        dy = y
        while self.check_collision(0, dy, boxes):
            dy -= numpy.sign(dy)

        while self.check_collision(dx, dy, boxes):
            dx -= numpy.sign(dx)

        self.rect.move_ip([dx,dy])
    
class Box(Sprite):
    def __init__(self, startx, starty):
        super().__init__("image/blue.png", startx, starty)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player(100, 200)
    
    boxes = pygame.sprite.Group()

    for bx in range(0,400,70):
        boxes.add(Box(bx,300))

    boxes.add(Box(200,230))
    boxes.add(Box(100,70))

    while True:
        pygame.event.pump()
        player.update(boxes)

        screen.fill(BACKGROUND)
        player.draw(screen)
        boxes.draw(screen)
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()