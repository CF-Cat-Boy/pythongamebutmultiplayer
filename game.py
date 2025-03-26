import pygame
from time import time
def fall():
        global falling
        global speedx
        global speedy
        global running   
        global resistance
        global speedm
def getttlvl():
    global lvlnum
    global quitt
    global lvlcomp
getttlvl()
global lvlnum
global lvlcomp
lvlcomp = False
lvlnum = 1
fall()
global resistance
resistance = 0.75
def game():
    getttlvl()
    global lvlnum
    global quitt
    global lvlcomp
    lvlcomp = False
    quitt = False
    jumpforce = -10
    gravity = 2
    geled = False

    # Class for the orange dude
    class Player(object):
        def __init__(self):
            self.rect = pygame.Rect(64, 64, 24, 24)

        def move(self, dx, dy):
            
            # Move each axis separately. Note that this checks for collisions both times.
            if dx != 0:
                self.move_single_axis(dx, 0)
            if dy != 0:
                self.move_single_axis(0, dy)
        
        def move_single_axis(self, dx, dy):

            fall()
            global falling
            global speedx
            global speedy
            global running
            global resistance
            global speedm
            getttlvl()
            global lvlnum
            global quitt
            global lvlcomp
            s = 0
            slipspeed = 1.5
            slipres = 0.95

            # Move the rect
            if not (self.rect.x + dx) >= 1080 and not (self.rect.x + dx) <= 0:
                self.rect.x += dx
            if not (self.rect.y + dy) >= 720 and not (self.rect.y + dy) <= 0:
                self.rect.y += dy
            if (self.rect.x + dx) >= 1080 or (self.rect.x + dx) <= 0:
                speedx = 0
            if (self.rect.y + dy) >= 720 or (self.rect.y + dy) <= 0:
                speedy = 0

            # If you collide with a wall, move out based on velocity
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if dx > 0: # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                        speedx = 0
                    if dx < 0: # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                        speedx = 0
                    if dy > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                        speedy = 0
                        falling = 0
                    if dy < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom
                        speedy = 0
            for wall in slips:
                if self.rect.colliderect(wall.rect):
                    if dx > 0: # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                        speedx = 0
                        resistance = slipres
                        speedm = slipspeed
                    if dx < 0: # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                        speedx = 0
                        resistance = slipres
                        speedm = slipspeed
                    if dy > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                        speedy = 0
                        falling = 0
                        resistance = slipres
                        speedm = slipspeed
                    if dy < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom
                        speedy = 0
                        resistance = slipres
                        speedm = slipspeed
                else:
                    s += 1
            if s >= len(slips):
                s = 0
                resistance = 0.75
                speedm = 2.5

                    
            for wall in plats:
                if self.rect.colliderect(wall.rect):
                    if dx > 0: # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                        speedx = 0
                    if dx < 0: # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                        speedx = 0
                    if dy > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                        speedy = 0
                        falling = 0
                    if dy < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom
                        speedy = 0
            for wall in scaffs:
                if self.rect.colliderect(wall.rect):
                    if dy > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                        speedy = 0
                        falling = 0
            for wall in iscaffs:
                if self.rect.colliderect(wall.rect):
                    if dy < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom
                        speedy = 0
            '''for wall in lscaffs:
                if self.rect.colliderect(wall.rect):
                    if dx > 0: # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                        speedx = 0
            for wall in rscaffs:
                if dx < 0: # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                        speedx = 0'''
            for badwall in badwalls:
                if self.rect.colliderect(badwall.rect) and badwall.solid :
                    if dx > 0: # Moving right; Hit the left side of the wall
                        self.rect.right = badwall.rect.left
                        speedx = 0
                    if dx < 0: # Moving left; Hit the right side of the wall
                        self.rect.left = badwall.rect.right
                        speedx = 0
                    if dy > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = badwall.rect.top
                        speedy = 0
                        falling = 0
                    if dy < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = badwall.rect.bottom
                        speedy = 0
                    badwall.stable = False
            for gel in gels:
                if self.rect.colliderect(gel.rect):
                    gel.geled = True
                else:
                    gel.geled = False
            for wall in door1s:
                if not wall.open:
                    if self.rect.colliderect(wall.rect):
                        if dx > 0: # Moving right; Hit the left side of the wall
                            self.rect.right = wall.rect.left
                            speedx = 0
                        if dx < 0: # Moving left; Hit the right side of the wall
                            self.rect.left = wall.rect.right
                            speedx = 0
                        if dy > 0: # Moving down; Hit the top side of the wall
                            self.rect.bottom = wall.rect.top
                            speedy = 0
                            falling = 0
                        if dy < 0: # Moving up; Hit the bottom side of the wall
                            self.rect.top = wall.rect.bottom
                            speedy = 0
            for wall in door2s:
                if not wall.open:
                    if self.rect.colliderect(wall.rect):
                        if dx > 0: # Moving right; Hit the left side of the wall
                            self.rect.right = wall.rect.left
                            speedx = 0
                        if dx < 0: # Moving left; Hit the right side of the wall
                            self.rect.left = wall.rect.right
                            speedx = 0
                        if dy > 0: # Moving down; Hit the top side of the wall
                            self.rect.bottom = wall.rect.top
                            speedy = 0
                            falling = 0
                        if dy < 0: # Moving up; Hit the bottom side of the wall
                            self.rect.top = wall.rect.bottom
                            speedy = 0
            if self.rect.colliderect(end_rect):
                running = False
                if not lvlnum == 7:
                    if lvlcomp == False:
                        lvlcomp = True
                        lvlnum += 1
                        self.move(100, 100)
                        if lvlnum == 7:
                            quitt = True
            for kill in kills:
                if self.rect.colliderect(kill.rect):
                    running = False
            for killi in killis:
                if self.rect.colliderect(killi.rect):
                    running = False
            for left in lefts:
                if self.rect.colliderect(left.rect):
                    speedx -= 1
            for right in rights:
                if self.rect.colliderect(right.rect):
                    speedx += 1
            for up in ups:
                if self.rect.colliderect(up.rect):
                    speedy += -2
                    if dy > 0: # Moving down; Hit the top side of the wall
                        self.move_single_axis(0, -1)
            for key in key1s:
                if self.rect.colliderect(key.rect):
                    key.used = True
                    for door in door1s:
                        door.open = True
            for key in key2s:
                if self.rect.colliderect(key.rect):
                    key.used = True
                    for door in door2s:
                        door.open = True
            

    # Nice class to hold a wall rect
    class Wall(object):
        def __init__(self, pos):
            walls.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class Slip(object):
        def __init__(self, pos):
            slips.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class Kill(object):
        def __init__(self, pos):
            kills.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class Killi(object):
        def __init__(self, pos):
            killis.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class Left(object):
        def __init__(self, pos):
            lefts.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class Right(object):
        def __init__(self, pos):
            rights.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class Up(object):
        def __init__(self, pos):
            ups.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class FakeWall(object):
        def __init__(self, pos):
            fakewalls.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class BadWall(object):
        def __init__(self, pos):
            self.solid = True
            self.stable = True
            self.t1 = float
            self.t2 = float
            self.tt1 = False
            self.tt2 = False
            badwalls.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class Gel(object):
        def __init__(self, pos):
            self.geled = False
            gels.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
    class Scaff(object):
        def __init__(self, pos):
            scaffs.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 32, 8)
    class IScaff(object):
        def __init__(self, pos):
            iscaffs.append(self)
            self.rect = pygame.Rect(pos[0], pos[1]+24, 32, 8)
    class Key1(object):
        def __init__(self, pos):
            self.used = False
            key1s.append(self)
            self.rect = pygame.Rect(pos[0]+12, pos[1]+12, 8, 8)
    class Door1(object):
        def __init__(self, pos):
            self.open = False
            door1s.append(self)
            self.rect = pygame.Rect(pos[0]+12, pos[1], 8, 32)
    class Key2(object):
        def __init__(self, pos):
            self.used = False
            key2s.append(self)
            self.rect = pygame.Rect(pos[0]+12, pos[1]+12, 8, 8)
    class Door2(object):
        def __init__(self, pos):
            self.open = False
            door2s.append(self)
            self.rect = pygame.Rect(pos[0]+12, pos[1], 8, 32)
    class Plat(object):
        def __init__(self, pos):
            self.loopi = 1
            self.right = True
            self.vert = False
            self.dist = 384
            self.width = 96
            self.height = 16
            plats.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], self.width, self.height)

    def badwallloop():
        for badwall in badwalls:
            if not badwall.stable:
                if not badwall.tt1:
                        badwall.t1 = time()
                        badwall.tt1 = True
                if time()-badwall.t1 > 0.5:
                    badwall.solid = False
                    if not badwall.tt2:
                        badwall.t2 = time()
                        badwall.tt2 = True
                    if time()-badwall.t2 > 5:
                        badwall.solid = True
                        badwall.stable = True
                        badwall.tt2 = False
                        badwall.tt1 = False
    def platloop():
        for plat in plats:
            if plat.loopi >= plat.dist*2:
                plat.loopi = 1
            if plat.vert:
                if (plat.loopi <= plat.dist and plat.right) or (plat.loopi >= plat.dist and not plat.right):
                    plat.rect.y += 2
                if (plat.loopi >= plat.dist and plat.right) or (plat.loopi <= plat.dist and not plat.right):
                    plat.rect.y -= 2
            else:
                if (plat.loopi <= plat.dist and plat.right) or (plat.loopi >= plat.dist and not plat.right):
                    plat.rect.x += 2
                if (plat.loopi >= plat.dist and plat.right) or (plat.loopi <= plat.dist and not plat.right):
                    plat.rect.x -= 2
            plat.loopi += 1
                




    fall()
    global falling
    global speedx
    global speedy
    global running
    global resistance
    global speedm
    falling = 0
    speedx = 0
    speedy = 0
    running = False 
    resistance = 0.75
    speedm = 2.5

    # Initialise pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((1080, 720))

    clock = pygame.time.Clock()
    kills = []
    lefts = []
    rights = []
    ups = []
    walls = [] # List to hold the walls
    slips = []
    badwalls = []
    gels = []
    fakewalls = []
    scaffs = []
    iscaffs = []
    '''lscaffs = []
    rscaffs = []'''
    killis = []
    key1s = []
    door1s = []
    key2s = []
    door2s = []
    plats = []
    player = Player() # Create the player
    def lvl(num):
        test = [
        "                                  ",
        "                                  ",
        "                                  ",
        "                                 ⚑",
        "█████NNNNNNNNNNNNNNNNNNNN     ████",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        ]
        lvl1 = [
        "                ████              ",
        "                ▓▓▓▓              ",
        "                ████              ",
        "                                 ⚑",
        "██████   ████  ██ █ █  █  █   █ ██",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        ]
        lvl2 = [
        "█    █████████████████████████████",
        "█    █                           █",
        "█    █                           █",
        "█    █⚑                          █",
        "█    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███-█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    █                          ^█",
        "█    ████████                   ^█",
        "█    ▓>>>>>>>                   ^█",
        "█    ████████                   ^█",
        "█    <<<<<<<<                   ^█",
        "██████████████████████████████████"
        ]
        lvl3 = [
        "                                  ",
        "                                  ",
        "                                  ",
        "███████████████████████████       ",
        "                            ^^^^^^",
        "                           ^^^^^^^",
        "                           ^^^^^^^",
        "     █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
        "     █XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "     █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
        "                                  ",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ",
        "                                  ",
        "                                  ",
        "   ⚑                              ",
        "██████████████████████████████████",
        "                                  ",
        "                                  "
        ]
        lvl4 = [
        "              |       I           ",
        "      k       |       I           ",
        "     ---      |       I           ",
        "              |       I          ⚑",
        "█████████████████░█████████████████",
        "█░░░█░░░█░█░░░░░░░█░█░░░░░█░░░█░█░█",
        "█░███░█░█░█░█░███░█░█░█████░█░█░█░█",
        "█░░░░░█░█░░░█░░░█░█░░░░░░░░░█░█░░░█",
        "█░█░█░███░█░█████░███████░█░█░███░█",
        "█░█░█░█░░░█░█░░░░░█░░░░░░░█░█░░░░░█",
        "█████░█░█░█░███████░█░███████░███░█",
        "█░░░░░░░█░█░░░░░░░█░█░░░░░░░█░█░░░█",
        "█░███░█░█░█░█░█████░███░███████░███",
        "█░█░░░█░█░█░█░░░░░█░█░░░░░█░█░░░░░█",
        "█░███░█░█░█░███░███░███░███░█░█░███",
        "█░█░░░█░█░█░█░█░░░█░░░█░█░█░█░█░░░█",
        "█░███░███████░█░█████░█░█░█░█░███░█",
        "█░░░█░░░░░█░░░░░░░█░░░█░█░█░░░█░█░█",
        "█████░███████████░███░███░███░█░███",
        "█░█░░░░░█░░░█░░░█░░░█░░░░░░░█░█░░░█",
        "█░█████░█░█████░███████████░█░█░███",
        "█░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░K█",
        "███████████████████████████████████"
        ]
        lvl5 = [
        "                                  ",
        "                                  ",
        "                                  ",
        "                                 ⚑",
        "███=                          ████",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        ]
        lvl6 = [
        "                                  ",
        "                                  ",
        "                                  ",
        "                                 ⚑",
        "█████NNNNNNNNNNNNNNNNNNNN     ████",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "                                  ",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]

        if num == 0:
            return test
        if num == 1:
            return lvl1
        if num == 2:
            return lvl2
        if num == 3:
            return lvl3
        if num == 4:
            return lvl4
        if num == 5:
            return lvl5
        if num == 6:
            return lvl6
    x = y = 0
    for row in lvl(lvlnum):
        for col in row:
            if col == "█":
                Wall((x, y))
            if col == "▓":
                FakeWall((x, y))
            if col == "░":
                Gel((x, y))
            if col == "⚑":
                end_rect = pygame.Rect(x, y, 32, 32)
            if col == "X":
                Kill((x, y))
            if col == "x":
                Killi((x, y))
            if col == "<":
                Left((x, y))
            if col == ">":
                Right((x, y))
            if col == "▒":
                BadWall((x, y))
            if col == "-":
                Scaff((x, y))
            if col == "_":
                IScaff((x, y))
            if col == "^":
                Up((x, y))
            if col == "k":
                Key1((x, y))
            if col == "|":
                Door1((x, y))
            if col == "K":
                Key2((x, y))
            if col == "I":
                Door2((x, y))
            if col == "=":
                Plat((x, y))
            if col == "‖":
                Plat((x, y))
                plats[len(plats)-1].vert = True
            if col == "N":
                Slip((x, y))
            x += 32
        y += 32
        x = 0

    running = True
    while running:
        
        clock.tick(60)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        
        platloop()
        badwallloop()

        for gel in gels:
            if gel.geled:
                geled = True

        # Move the player if the space,a,d/up,left,right keys are pressed
        if not geled:
            falling = falling+1
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            speedx = speedx-speedm
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            speedx = speedx+speedm
        if key[pygame.K_F11]:
            if clock.tick(10)/2:
                pygame.display.toggle_fullscreen()
        if not geled:
            if key[pygame.K_SPACE] or key[pygame.K_UP]:
                if falling < 3:
                    speedy = speedy+jumpforce
        else:
            if key[pygame.K_w] or key[pygame.K_UP]:
                speedy = speedy-speedm
            if key[pygame.K_s] or key[pygame.K_DOWN]:
                speedy = speedy+speedm
        if key[pygame.K_ESCAPE]:
            quitt = True
            running = False

        speedx = speedx*resistance
        if not geled:
            speedy = speedy+gravity
        else:
            speedy = speedy*resistance
        player.move(speedx, speedy)
        geled = False
        # Draw the scene
        screen.fill((0, 0, 0))
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        for plat in plats:
            pygame.draw.rect(screen, (255, 255, 255), plat.rect)
        for door in door1s:
            if not door.open:
                pygame.draw.rect(screen, (255, 0, 0), door.rect)
        for key in key1s:
            if not key.used:
                pygame.draw.rect(screen, (255, 0, 0), key.rect)
        for door in door2s:
            if not door.open:
                pygame.draw.rect(screen, (0, 0, 255), door.rect)
        for key in key2s:
            if not key.used:
                pygame.draw.rect(screen, (0, 0, 255), key.rect)
        for fakewall in fakewalls:
            pygame.draw.rect(screen, (250, 250, 250), fakewall.rect)
        for kill in kills:
            pygame.draw.rect(screen, (255, 0, 0), kill.rect)
        for left in lefts:
            pygame.draw.rect(screen, (128, 128, 255), left.rect)
        for right in rights:
            pygame.draw.rect(screen, (255, 200, 0), right.rect)
        for up in ups:
            pygame.draw.rect(screen, (255, 0, 255), up.rect)
        for badwall in badwalls:
            if badwall.solid:
                pygame.draw.rect(screen, (128, 128, 128), badwall.rect)
        for gel in gels:
            pygame.draw.rect(screen, (60, 126, 143), gel.rect)
        for scaff in scaffs:
            pygame.draw.rect(screen, (188, 106, 60), scaff.rect)
        for iscaff in iscaffs:
            pygame.draw.rect(screen, (188, 106, 60), iscaff.rect)
        for slip in slips:
            pygame.draw.rect(screen, (128, 128, 255), slip.rect)
        '''for lscaff in lscaffs:
            pygame.draw.rect(screen, (188, 106, 60), lscaff.rect)
        for rscaff in rscaffs:
            pygame.draw.rect(screen, (188, 106, 60), rscaff.rect)'''
        pygame.draw.rect(screen, (0, 255, 0), end_rect)
        pygame.draw.rect(screen, (255, 128, 128), player.rect)
        pygame.display.flip()
    if quitt == False:
        game()
game()
pygame.quit()