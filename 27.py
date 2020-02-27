import pygame
import os
import sys


pygame.init()
FPS = 50
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
running = True
clock = pygame.time.Clock()
pygame.mixer.music.load("swa.mp3")
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()

def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image



def start_screen():

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)

def start_screen2():
    pygame.mixer.music.load("reveal.mp3")
    pygame.mixer.music.play(-1)

    fon = pygame.transform.scale(load_image('fon1.png'), (width, height))
    screen.blit(fon, (0, 0))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


def start_screen3():
    pygame.mixer.music.load("gameover.mp3")
    pygame.mixer.music.play(-1)

    fon = pygame.transform.scale(load_image('fon3.png'), (width, height))
    screen.blit(fon, (0, 0))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


def start_screen4():


    fon = pygame.transform.scale(load_image('instr.png'), (width, height))
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def start_screen5():

    fon = pygame.transform.scale(load_image('hist.png'), (width, height))
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def start_screen6():
    pygame.mixer.music.load("reveal.mp3")
    pygame.mixer.music.play(-1)

    fon = pygame.transform.scale(load_image('fon5.png'), (width, height))
    screen.blit(fon, (0, 0))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)



def start_screen10():
    pygame.mixer.music.load("des.mp3")
    pygame.mixer.music.play(-1)

    fon = pygame.transform.scale(load_image('fon4.png'), (width, height))
    screen.blit(fon, (0, 0))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)



def start_screen11():
    pygame.mixer.music.load("des.mp3")
    pygame.mixer.music.play(-1)

    fon = pygame.transform.scale(load_image('fon2.png'), (width, height))
    screen.blit(fon, (0, 0))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))


    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_images = {'wall': load_image('box.png'), 'empty': load_image('grass.png'), 'portal': load_image('portal.png'),
               'lava': load_image('lava.jpg'), 'piki': load_image('piki.png'), 'portal2': load_image('portal2.png'),
               'portal3': load_image('portal3.png'), 'door': load_image('door.png'), 'dor': load_image('dor.png'),
               'door2': load_image('door2.png'), 'dor2': load_image('dor2.png'), 'door3': load_image('door3.png'),
               'dor3': load_image('dor3.png'), 'tabl2': load_image('tabl2.png'), 'tabl3': load_image('tabl3.png'),
               'wall2': load_image('box2.png'), 'wall3': load_image('box3.png'), 'tabl': load_image('tabl.png'),
               'piki2': load_image('piki2.png'), 'piki3': load_image('piki3.png'),}
player_image = load_image('mario.png')
# основной персонаж
player = None
# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
piki_group = pygame.sprite.Group()
portal_group = pygame.sprite.GroupSingle()
portal2_group = pygame.sprite.GroupSingle()
portal3_group = pygame.sprite.GroupSingle()
door_group = pygame.sprite.GroupSingle()
dor_group = pygame.sprite.GroupSingle()
door2_group = pygame.sprite.GroupSingle()
dor2_group = pygame.sprite.GroupSingle()
door3_group = pygame.sprite.GroupSingle()
dor3_group = pygame.sprite.GroupSingle()
tabl_group = pygame.sprite.GroupSingle()
tabl2_group = pygame.sprite.GroupSingle()
tabl3_group = pygame.sprite.GroupSingle()
lava_group = pygame.sprite.Group()
tile_width = tile_height = 50


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)



class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        if tile_type == 'wall':
            self.add(walls_group)
        if tile_type == 'wall2':
            self.add(walls_group)
        if tile_type == 'wall3':
            self.add(walls_group)
        if tile_type == 'portal':
            self.add(portal_group)
        if tile_type == 'portal2':
            self.add(portal2_group)
        if tile_type == 'portal3':
            self.add(portal3_group)
        if tile_type == 'piki':
            self.add(piki_group)
        if tile_type == 'piki2':
            self.add(piki_group)
        if tile_type == 'piki3':
            self.add(piki_group)
        if tile_type == 'door':
            self.add(door_group)
        if tile_type == 'dor':
            self.add(dor_group)
        if tile_type == 'tabl':
            self.add(tabl_group)
        if tile_type == 'door2':
            self.add(door2_group)
        if tile_type == 'door3':
            self.add(door3_group)
        if tile_type == 'dor3':
            self.add(dor3_group)
        if tile_type == 'dor2':
            self.add(dor2_group)
        if tile_type == 'tabl2':
            self.add(tabl2_group)
        if tile_type == 'tabl3':
            self.add(tabl3_group)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)


    def update(self):
        self.image = player_image



    def move(self, x, y):
        self.rect = self.image.get_rect().move(self.rect.x + x * tile_width, tile_height * y + self.rect.y)





def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                xx = x
                yy = y
            elif level[y][x] == '*':
                Tile('portal', x, y)
            elif level[y][x] == '=':
                Tile('lava', x, y)
            elif level[y][x] == '-':
                Tile('piki', x, y)
            elif level[y][x] == '!':
                Tile('door', x, y)
            elif level[y][x] == '?':
                Tile('empty', x, y)
                Tile('tabl', x, y)
    # вернем игрока, а также размер поля в клетках
    new_player = Player(xx, yy)
    return new_player, x, y


def generate_level2(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall2', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                xx = x
                yy = y
            elif level[y][x] == '*':
                Tile('portal2', x, y)
            elif level[y][x] == '=':
                Tile('lava', x, y)
            elif level[y][x] == '-':
                Tile('piki2', x, y)
            elif level[y][x] == '!':
                Tile('door2', x, y)
            elif level[y][x] == '?':
                Tile('empty', x, y)
                Tile('tabl2', x, y)
    # вернем игрока, а также размер поля в клетках
    new_player = Player(xx, yy)
    return new_player, x, y


def generate_level3(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall3', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                xx = x
                yy = y
            elif level[y][x] == '*':
                Tile('portal3', x, y)
            elif level[y][x] == '=':
                Tile('lava', x, y)
            elif level[y][x] == '-':
                Tile('piki3', x, y)
            elif level[y][x] == '?':
                Tile('empty', x, y)
                Tile('tabl3', x, y)
            elif level[y][x] == '!':
                Tile('door3', x, y)
    # вернем игрока, а также размер поля в клетках
    new_player = Player(xx, yy)
    return new_player, x, y


def generate_level4(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                xx = x
                yy = y
            elif level[y][x] == '*':
                Tile('portal3', x, y)
            elif level[y][x] == '=':
                Tile('lava', x, y)
            elif level[y][x] == '-':
                Tile('piki', x, y)
            elif level[y][x] == '?':
                Tile('empty', x, y)
                Tile('tabl', x, y)
            elif level[y][x] == '!':
                Tile('dor', x, y)
    # вернем игрока, а также размер поля в клетках
    new_player = Player(xx, yy)
    return new_player, x, y

def generate_level5(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall2', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                xx = x
                yy = y
            elif level[y][x] == '*':
                Tile('portal3', x, y)
            elif level[y][x] == '=':
                Tile('lava', x, y)
            elif level[y][x] == '-':
                Tile('piki2', x, y)
            elif level[y][x] == '?':
                Tile('empty', x, y)
                Tile('tabl2', x, y)
            elif level[y][x] == '!':
                Tile('dor2', x, y)
    # вернем игрока, а также размер поля в клетках
    new_player = Player(xx, yy)
    return new_player, x, y


def generate_level6(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall3', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                xx = x
                yy = y
            elif level[y][x] == '*':
                Tile('portal3', x, y)
            elif level[y][x] == '=':
                Tile('lava', x, y)
            elif level[y][x] == '-':
                Tile('piki3', x, y)
            elif level[y][x] == '?':
                Tile('empty', x, y)
                Tile('tabl3', x, y)
            elif level[y][x] == '!':
                Tile('dor3', x, y)
    # вернем игрока, а также размер поля в клетках
    new_player = Player(xx, yy)
    return new_player, x, y

player, level_x, level_y = generate_level(load_level('map.txt'))
camera = Camera()
start_screen()
start_screen5()
start_screen4()
running = True
pygame.mixer.music.load("rui.mp3")
pygame.mixer.music.play(-1)
camera.update(player)
f = 0


while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:


            if event.key == pygame.K_LEFT:
                player_image = load_image('mario2.png')
                player.update()
                player.move(-1, 0)
                if pygame.sprite.spritecollideany(player, walls_group):
                    player.move(1, 0)
            elif event.key == pygame.K_RIGHT:
                player_image = load_image('mario3.png')
                player.update()
                player.move(1, 0)
                if pygame.sprite.spritecollideany(player, walls_group):
                    player.move(-1, 0)
            elif event.key == pygame.K_DOWN:
                player_image = load_image('mario.png')
                player.update()
                player.move(0, 1)
                if pygame.sprite.spritecollideany(player, walls_group):
                    player.move(0, -1)

            elif event.key == pygame.K_UP:
                player_image = load_image('mario6.png')
                player.update()
                player.move(0, -1)
                if pygame.sprite.spritecollideany(player, walls_group):
                    player.move(0, 1)


    camera.update(player);

    for sprite in all_sprites:
        camera.apply(sprite)

    if pygame.sprite.spritecollideany(player, portal2_group):
        for sprite in all_sprites:
            sprite.kill()
        player, level_x, level_y = generate_level3(load_level('map3.txt'))
        camera = Camera()
        running = True
        pygame.mixer.music.load("undertale.mp3")
        pygame.mixer.music.play(-1)


    if pygame.sprite.spritecollideany(player, piki_group):
        for sprite in all_sprites:
            sprite.kill()
        start_screen3()


    if pygame.sprite.spritecollideany(player, portal_group):
        for sprite in all_sprites:
            sprite.kill()
        player, level_x, level_y = generate_level2(load_level('map2.txt'))
        camera = Camera()
        running = True
        pygame.mixer.music.load("uwa.mp3")
        pygame.mixer.music.play(-1)


    if pygame.sprite.spritecollideany(player, portal3_group):
        for sprite in all_sprites:
            sprite.kill()
        if f == 1:
            start_screen10()
        elif f == 2:
            start_screen6()
        elif f == 3:
            start_screen2()
        else:
            start_screen11()


    if pygame.sprite.spritecollideany(player, tabl_group):
        f += 1
        print(f)
        for sprite in tabl_group:
            sprite.kill()


    if pygame.sprite.spritecollideany(player, tabl2_group):
        f += 1
        print(f)
        for sprite in tabl2_group:
            sprite.kill()


    if pygame.sprite.spritecollideany(player, tabl3_group):
        f += 1
        print(f)
        for sprite in tabl3_group:
            sprite.kill()


    if pygame.sprite.spritecollideany(player, door_group):
        for sprite in all_sprites:
            sprite.kill()

        player, level_x, level_y = generate_level4(load_level('room.txt'))
        camera = Camera()
        running = True



    if pygame.sprite.spritecollideany(player, dor_group):
        for sprite in all_sprites:
            sprite.kill()

        player, level_x, level_y = generate_level(load_level('mappp.txt'))
        camera = Camera()
        running = True




    if pygame.sprite.spritecollideany(player, door2_group):
        for sprite in all_sprites:
            sprite.kill()

        player, level_x, level_y = generate_level5(load_level('room2.txt'))
        camera = Camera()
        running = True




    if pygame.sprite.spritecollideany(player, dor2_group):
        for sprite in all_sprites:
            sprite.kill()

        player, level_x, level_y = generate_level2(load_level('mappp2.txt'))
        camera = Camera()
        running = True



    if pygame.sprite.spritecollideany(player, door3_group):
        for sprite in all_sprites:
            sprite.kill()

        player, level_x, level_y = generate_level6(load_level('room3.txt'))
        camera = Camera()
        running = True



    if pygame.sprite.spritecollideany(player, dor3_group):
        for sprite in all_sprites:
            sprite.kill()

        player, level_x, level_y = generate_level3(load_level('mappp3.txt'))
        camera = Camera()
        running = True


    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()