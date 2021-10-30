import pygame
import os

#main charicter sprite
class Jonno(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.x = x
        self.y = y
        
        #direction charicter is faceing
        self.direction = "f"
        self.sprite = 0
        self.cycle_direction = 1
        #list of sprites for main charicter
        self.sprites_left = []
        self.sprites_right = []
        self.sprites_back = []
        self.sprites_front = []
        #curect walk cycle lenth
        self.cycle_time = 0
        #interval between walking sprites
        self.interval = 0.2
        
        #load charicter sprites
        self.Johnno_walk_L_1 = pygame.image.load(os.path.join("data","Character Sprites", "Johnno_left_walk1.png"))
        self.Johnno_walk_L_1 = self.Johnno_walk_L_1.convert_alpha()
        self.sprites_left.append(self.Johnno_walk_L_1)
            
        self.Johnno_stand_L = pygame.image.load(os.path.join("data","Character Sprites", "Johnno_left_standing.png"))
        self.Johnno_stand_L = self.Johnno_stand_L.convert_alpha()
        self.sprites_left.append(self.Johnno_stand_L)
            
        self.Johnno_walk_L_2 = pygame.image.load(os.path.join("data","Character Sprites", "Johnno_left_walk2.png"))
        self.Johnno_walk_L_2 = self.Johnno_walk_L_2.convert_alpha()
        self.sprites_left.append(self.Johnno_walk_L_2)

        self.Johnno_walk_R_1 = pygame.image.load(os.path.join("data","Character Sprites", "Johnno_right_walk1.png"))
        self.Johnno_walk_R_1 = self.Johnno_walk_R_1.convert_alpha()
        self.sprites_right.append(self.Johnno_walk_R_1)

        self.Johnno_stand_R = pygame.image.load(os.path.join("data","Character Sprites", "Johnno_right_standing.png"))
        self.Johnno_stand_R = self.Johnno_stand_R.convert_alpha()
        self.sprites_right.append(self.Johnno_stand_R)

        self.Johnno_walk_R_2 = pygame.image.load(os.path.join("data","Character Sprites", "Johnno_right_walk2.png"))
        self.Johnno_walk_R_2 = self.Johnno_walk_R_2.convert_alpha()
        self.sprites_right.append(self.Johnno_walk_R_2)

        self.Johnno_walk_B_1 = pygame.image.load(os.path.join("data","Character Sprites", "Johnno_back_walk1.png"))
        self.Johnno_walk_B_1 = self.Johnno_walk_B_1.convert_alpha()
        self.sprites_back.append(self.Johnno_walk_B_1)

        self.Johnno_stand_B = pygame.image.load(os.path.join("data","Character Sprites", "Johnno_back_standing.png"))
        self.Johnno_stand_B = self.Johnno_stand_B.convert_alpha()
        self.sprites_back.append(self.Johnno_stand_B)

        self.Johnno_walk_B_2 = pygame.image.load(os.path.join("data","Character Sprites", "Johnno_back_walk2.png"))
        self.Johnno_walk_B_2 = self.Johnno_walk_B_2.convert_alpha()
        self.sprites_back.append(self.Johnno_walk_B_2)

        self.Johnno_walk_F_1 = pygame.image.load(os.path.join("data","Character Sprites", "Johnno_front_walk1.png"))
        self.Johnno_walk_F_1 = self.Johnno_walk_F_1.convert_alpha()
        self.sprites_front.append(self.Johnno_walk_F_1)

        self.Johnno_stand_F = pygame.image.load(os.path.join("data","Character Sprites", "Johnno_front_standing.png"))
        self.Johnno_stand_F = self.Johnno_stand_F.convert_alpha()
        self.sprites_front.append(self.Johnno_stand_F)

        self.Johnno_walk_F_2 = pygame.image.load(os.path.join("data","Character Sprites", "Johnno_front_walk2.png"))
        self.Johnno_walk_F_2 = self.Johnno_walk_F_2.convert_alpha()
        self.sprites_front.append(self.Johnno_walk_F_2)


    
    def update(self):
        
        #get keys that are being pressed
        pressedkeys = pygame.key.get_pressed()
        if pressedkeys[pygame.K_a] and not pressedkeys[pygame.K_d]:
            #add time since last frame to cycle_time
            self.cycle_time += game.sec
            if self.direction != "l":
                self.direction = "l"
                self.sprite= 0
                self.cycle_direction = 1
            if self.cycle_time > self.interval:
                self.sprite+= 1 * self.cycle_direction
                self.cycle_time = 0
                if self.sprite == len(self.sprites_left)-1 or self.sprite == 0:
                    self.cycle_direction *= -1
            game.screen.blit(self.sprites_left[self.sprite],(self.x,self.y))
        
        elif pressedkeys[pygame.K_d] and not pressedkeys[pygame.K_a]:
            self.cycle_time += game.sec
            if self.direction != "r":
                self.direction = "r"
                self.sprite= 0
                self.cycle_direction = 1
            if self.cycle_time > self.interval:
                self.sprite += 1 * self.cycle_direction
                self.cycle_time = 0
                if self.sprite == len(self.sprites_right)-1 or self.sprite == 0:
                    self.cycle_direction *= -1
            game.screen.blit(self.sprites_right[self.sprite],(self.x,self.y))
            
        elif pressedkeys[pygame.K_w] and not pressedkeys[pygame.K_s]:
            self.cycle_time += game.sec
            if self.direction != "b":
                self.direction = "b"
                self.sprite= 0
                self.cycle_direction = 1
            if self.cycle_time > self.interval:
                self.sprite+= 1 * self.cycle_direction
                self.cycle_time = 0
                if self.sprite == len(self.sprites_back)-1 or self.sprite == 0:
                    self.cycle_direction *= -1
            game.screen.blit(self.sprites_back[self.sprite],(self.x,self.y))
    
        elif pressedkeys[pygame.K_s] and not pressedkeys[pygame.K_w]:
            self.cycle_time += game.sec
            if self.direction != "f":
                self.direction = "f"
                self.sprite= 0
                self.cycle_direction = 1
            if self.cycle_time > self.interval:
                self.sprite+= 1 * self.cycle_direction
                self.cycle_time = 0
                if self.sprite == len(self.sprites_front )-1 or self.sprite == 0:
                    self.cycle_direction *= -1
            game.screen.blit(self.sprites_front[self.sprite],(self.x,self.y))
            
        else:
            if self.direction == "f":
                game.screen.blit(self.sprites_front[1],(self.x,self.y))
            elif self.direction == "b":
                game.screen.blit(self.sprites_back[1],(self.x,self.y))
            elif self.direction == "l":
                game.screen.blit(self.sprites_left[1],(self.x,self.y))
            elif self.direction == "r":
                game.screen.blit(self.sprites_right[1],(self.x,self.y))
        

class Main_game:
    def __init__(self,fps):
        #initolise pygame
        pygame.init()
        
        #get screen resolution
        Screen_info = pygame.display.Info()
        self.hight = Screen_info.current_h
        self.width = Screen_info.current_w
        
        #make screen
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        
        #make background
        self.background = pygame.image.load(os.path.join("data","Maps", "Map1_BG.png"))
        self.background = self.background.convert()
        
        self.back_x = self.width-5400/2
        self.back_y = self.hight-4950/2
        self.back_speed = 125
        
        #make sprite
        self.jonno = Jonno(self.width/2-40.5,self.hight/2-63)
        
        #get fps and make clock methiod
        self.fps = fps
        self.sec = 0
        self.clock = pygame.time.Clock()
    #main game     
    def run(self):
        
        #game loop
        running = True
        while running:
            self.sec = self.clock.tick(self.fps) / 1000.0
            
            #event handleing(to exit currently)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            pressedkeys = pygame.key.get_pressed()
            if pressedkeys[pygame.K_w]:
                self.back_y += self.back_speed * self.sec
            if pressedkeys[pygame.K_s]:
                self.back_y -= self.back_speed * self.sec
            if pressedkeys[pygame.K_a]:
                self.back_x += self.back_speed * self.sec
            if pressedkeys[pygame.K_d]:
                self.back_x -= self.back_speed * self.sec
                
            
            #adds backgound to the screen
            self.screen.blit(self.background, (self.back_x,self.back_y))
            
            self.jonno.update()
            
            #updates screen
            pygame.display.update()
        
        #ends program
        pygame.quit()

#runs game
game = Main_game(30)
game.run()
        
        