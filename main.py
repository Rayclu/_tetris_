import pygame
import tetrisC
import representacion
import persistencia

pygame.init()

def DetectCom():
    pass

def DetecTec():
    pass

def pause():
    """
    
        Pause the game and draw the string. This function
        also calls the flip function which draws the string on the screen.
        
        # Draw the string to the center of the screen.
        self.print_center(["PAUSE","Press \"p\" to continue"])
    """
    
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = False
    pygame.display.flip()

def exit(running):
    pass
    """
    if pause(paused) == true:
        for envent.type in pygame.event.get():
            if event.type==pygame.keydown and event.key == pygame.k_esc:
                running=false
                return running
    """
def reset():
    pass
    """
    
    if pause(paused) == true:
        for envent.type in pygame.event.get():
            if event.type==pygame.keydown and event.key == pygame.k_r:
                
                
    """



def main():
    pass