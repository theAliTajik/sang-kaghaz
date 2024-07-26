'''import pygame
import sys

# مقداردهی اولیه Pygame
pygame.init()

# تنظیمات صفحه
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("نمونه دکمه در Pygame")

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# تعریف فونت
font = pygame.font.Font(None, 36)

def draw_button(screen, rect, text):
    pygame.draw.rect(screen, BLUE, rect)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def main():
    button_rect = pygame.Rect(300, 250, 200, 50)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("دکمه فشرده شد!")

        screen.fill(WHITE)
        draw_button(screen, button_rect, "دکمه من")

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    '''
'''
# ۱ - Import library
import pygame
from pygame.locals import *
import sys

# ۲ - Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# تعریف فونت
font = pygame.font.Font(None, 36)

def draw_button(screen, rect, text):
    pygame.draw.rect(screen, BLUE, rect)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def main():
    button_rect = pygame.Rect(220, 200, 200, 50)
    running = True            
    
    # ۴ - keep looping through
    while running:
        # ۵ - clear the screen before drawing it again
        screen.fill(WHITE)
        
        # ۶ - draw the screen elements
        draw_button(screen, button_rect, "play")
        
        # ۷ - update the screen
        pygame.display.flip()
        
        # ۸ - loop through the events
        for event in pygame.event.get():
            # check if the event is the X button 
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  
                if button_rect.collidepoint(event.pos):
                    print("دکمه فشرده شد!")
    
    # اگر خارج از حلقه `while` هستیم، بازی را خاتمه می‌دهیم
    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()
'''
import random

game_list = ["rock", "paper", "scissor"]


player1 = input("Enter your decision: ")


player2 = random.choice(game_list)
print(f"camputer choice: {player2}")

if player1 == player2:
    print ("equal")
elif player1 == "rock":
    if player2 == "scissor":
        print ("player1 wins")
    else :
        print ("computer wins")
elif player1 == "paper":
    if player2 == "rock":
        print("player1 wins")
    else:
        print("computer wins")
elif player1 == "scissor":
    if player2 == "paper":
        print("player1 wins")
    else:
        print("computer wins")
else:
    print("invalid input!")


