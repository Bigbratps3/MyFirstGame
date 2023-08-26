import pygame
import time
import random
pygame.font.init()

Width, Height = 1000, 700
pygame.init()
WIN = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("DODGE")

sprite = pygame.transform.scale(pygame.image.load("sprite.png"), (Width, Height))

PLAYER_Width = 40
PLAYER_Height = 60
PLAYER_VEL = 10
STAR_Width = 10
STAR_Height = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, stars):
    WIN.blit(sprite, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    text_width, text_height = FONT.size(f"Time: {round(elapsed_time)}s")
    text_x = (Width - text_width) // 2
    
    WIN.blit(time_text, (text_x, 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(300, Height - PLAYER_Height,
                          PLAYER_Width, PLAYER_Height)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
                star_x = random.randint(0, Width - STAR_Width)
                star = pygame.Rect(star_x, -STAR_Height,
                                    STAR_Width, STAR_Height)
                stars.append(star)

                star_add_increment = max(200, star_add_increment - 50)
                star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
               break
            


        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL
        if keys[pygame.K_d] and player.x + PLAYER_VEL + PLAYER_Width <= Width:
                player.x += PLAYER_VEL
        if keys[pygame.K_w] and player.y - PLAYER_VEL >= 0:
                player.y -= PLAYER_VEL
        if keys[pygame.K_s] and player.y + PLAYER_VEL + PLAYER_Height <= Height:
                player.y += PLAYER_VEL
        
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > Height:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
            break

                
        if hit:
            lost_text = FONT.render("YOU LOSE!", 1, "white" )
            WIN.blit(lost_text, (Width/2 - lost_text.get_width()/2, Height/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
            
        draw(player, elapsed_time, stars)
        
        
            
        
        

if __name__ == "__main__":
    main()