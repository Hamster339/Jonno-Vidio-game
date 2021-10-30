import pygame
import os
import sys

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

# 960 540

class Game(object):


    def __init__(self, width=1920, height= 1080, fps=30):

        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        
        self.background = pygame.image.load(os.path.join("data", "Map1_BG.png"))
        self.background = self.background.convert()
        
        self.Johnno_stand_F = pygame.image.load(os.path.join("data", "Johnno_front_standing.png"))
        self.Johnno_stand_F = self.Johnno_stand_F.convert_alpha()
        
        self.Johnno_stand_B = pygame.image.load(os.path.join("data", "Johnno_back_standing.png"))
        self.Johnno_stand_B = self.Johnno_stand_B.convert_alpha()
        
        self.Johnno_stand_L = pygame.image.load(os.path.join("data", "Johnno_left_standing.png"))
        self.Johnno_stand_L = self.Johnno_stand_L.convert_alpha()
        
        self.Johnno_stand_R = pygame.image.load(os.path.join("data", "Johnno_right_standing.png"))
        self.Johnno_stand_R = self.Johnno_stand_R.convert_alpha()
        
        self.Johnno_walk_F_1 = pygame.image.load(os.path.join("data", "Johnno_front_walk1.png"))
        self.Johnno_walk_F_1 = self.Johnno_walk_F_1.convert_alpha()
        
        self.Johnno_walk_F_2 = pygame.image.load(os.path.join("data", "Johnno_front_walk2.png"))
        self.Johnno_walk_F_2 = self.Johnno_walk_F_2.convert_alpha()
        
        self.Johnno_walk_B_1 = pygame.image.load(os.path.join("data", "Johnno_back_walk1.png"))
        self.Johnno_walk_B_1 = self.Johnno_walk_B_1.convert_alpha()
        
        self.Johnno_walk_B_2 = pygame.image.load(os.path.join("data", "Johnno_back_walk2.png"))
        self.Johnno_walk_B_2 = self.Johnno_walk_B_2.convert_alpha()
        
        self.Johnno_walk_L_1 = pygame.image.load(os.path.join("data", "Johnno_left_walk1.png"))
        self.Johnno_walk_L_1 = self.Johnno_walk_L_1.convert_alpha()
        
        self.Johnno_walk_L_2 = pygame.image.load(os.path.join("data", "Johnno_left_walk2.png"))
        self.Johnno_walk_L_2 = self.Johnno_walk_L_2.convert_alpha()
        
        self.Johnno_walk_R_1 = pygame.image.load(os.path.join("data", "Johnno_right_walk1.png"))
        self.Johnno_walk_R_1 = self.Johnno_walk_R_1.convert_alpha()
        
        self.Johnno_walk_R_2 = pygame.image.load(os.path.join("data", "Johnno_right_walk2.png"))
        self.Johnno_walk_R_2 = self.Johnno_walk_R_2.convert_alpha()
        
        
        self.backx = 0
        self.backy = 0
        self.speed = 200
        
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        
        self.cycletime = 0.0
        self.interval = 0.25
        self.step = True
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0
            seconds = milliseconds/1000.0
            
            text = ("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(self.clock.get_fps(), " "*5, self.playtime))
            pygame.display.set_caption(text)
            pygame.display.flip()
            
            self.screen.blit(self.background, (self.backx, self.backy))
            pressedkeys = pygame.key.get_pressed()
            
            if pressedkeys[pygame.K_w]:
                self.backy += self.speed * seconds
                self.cycletime += seconds
                if self.step == True:
                    self.screen.blit(self.Johnno_walk_B_1, (960,540))
                elif self.step == False:
                    self.screen.blit(self.Johnno_walk_B_2, (960,540))
                    
                if self.cycletime > self.interval:
                    self.step = not self.step
                    self.cycletime = 0
            
            elif pressedkeys[pygame.K_s]:
                self.backy -= self.speed * seconds
                self.cycletime += seconds
                
                if self.step == True:
                    self.screen.blit(self.Johnno_walk_F_1, (960,540))
                elif self.step == False:
                    self.screen.blit(self.Johnno_walk_F_2, (960,540))
                    
                if self.cycletime > self.interval:
                    self.step = not self.step
                    self.cycletime = 0
            
            elif pressedkeys[pygame.K_a]:
                self.backx += self.speed * seconds
                self.cycletime += seconds
                
                if self.step == True:
                    self.screen.blit(self.Johnno_walk_L_1, (960,540))
                elif self.step == False:
                    self.screen.blit(self.Johnno_walk_L_2, (960,540))
                    
                if self.cycletime > self.interval:
                    self.step = not self.step
                    self.cycletime = 0
            
            elif pressedkeys[pygame.K_d]:
                self.backx -= self.speed * seconds
                self.cycletime += seconds
                
                if self.step == True:
                    self.screen.blit(self.Johnno_walk_R_1, (960,540))
                elif self.step == False:
                    self.screen.blit(self.Johnno_walk_R_2, (960,540))
                    
                if self.cycletime > self.interval:
                    self.step = not self.step
                    self.cycletime = 0
                
            else:
                self.screen.blit(self.Johnno_stand_F, (960,540))
                       


        pygame.quit()


####

if __name__ == '__main__':

    # call with width of window and fps
    Game(0,0).run()