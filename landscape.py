import pygame
import sys 

# starting pygame
pygame.init()

# Size of display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# color
White = (255, 255, 255)
blue = (135, 206, 250)
green = (34, 139, 34)
yellow = (255, 255, 0)
gray = (169, 169, 169)
brown= (150,75,0)

# Cloud position
cloud_x = 100
cloud_y = 50
cloud_d = 200
cloud_e = 100
cloud_m = 320
cloud_n = 60

# Draw background
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(blue)  

    # Draw sun
    pygame.draw.circle(screen, yellow, (100, 100), 50)

    # Draw mountains
    pygame.draw.polygon(screen, gray, [(0, 400), (200, 200), (400, 400)])
    pygame.draw.polygon(screen, gray, [(200, 400), (400, 200), (600, 400)])
    pygame.draw.polygon(screen, gray, [(400, 400), (600, 250), (800, 400)])

    # Draw ground
    pygame.draw.rect(screen, green, [0,400,800,400])
 
    # Draw house
    pygame.draw.rect(screen, brown, [350,350,125,125])
    pygame.draw.polygon(screen, brown, [(350, 350), (410, 250), (475, 350)])
    pygame.draw.rect(screen, yellow, (385, 375, 50, 100))
    pygame.draw.circle(screen, brown, (420, 430), 5)
    
    # Draw moving cloud
    pygame.draw.circle(screen, White, (cloud_x, cloud_y), 30)
    cloud_x += 0.5  # Move cloud to the right
    if cloud_x > WIDTH + 200:  
        cloud_x = -200
    
    pygame.draw.circle(screen, White, (cloud_x+25, cloud_y-20), 30)
    cloud_x += 0.5 # Move cloud to the right
    if cloud_x > WIDTH + 200: 
        cloud_x = 200

    pygame.draw.circle(screen, White, (cloud_x+50, cloud_y), 30)
    cloud_x += 0.5  # Move cloud to the right
    if cloud_x > WIDTH + 200:  
        cloud_x = -200

    pygame.draw.circle(screen, White, (cloud_d, cloud_e), 30)
    cloud_d += 0.5  # Move cloud to the right
    if cloud_d > WIDTH + 200:  
        cloud_d = -200
    elif WIDTH + 200
        cloud_d = -200
    
    pygame.draw.circle(screen, White, (cloud_d+25, cloud_e-20), 30)
    cloud_d += 0.5 # Move cloud to the right
    if cloud_d > WIDTH + 200: 
        cloud_d = 200

    pygame.draw.circle(screen, White, (cloud_d+50, cloud_e), 30)
    cloud_d += 0.5  # Move cloud to the right
    if cloud_d > WIDTH + 200:  
        cloud_d = -200
 
    pygame.draw.circle(screen, White, (cloud_m, cloud_n), 30)
    cloud_m += 0.5  # Move cloud to the right
    if cloud_m > WIDTH + 200:  
        cloud_m = -200
    
    pygame.draw.circle(screen, White, (cloud_m+25, cloud_n-20), 30)
    cloud_m += 0.5 # Move cloud to the right
    if cloud_m > WIDTH + 200: 
        cloud_m = 200

    pygame.draw.circle(screen, White, (cloud_m+50, cloud_n), 30)
    cloud_m += 0.5  # Move cloud to the right
    if cloud_m > WIDTH + 200:  
        cloud_m = -200

    pygame.display.flip()
    clock.tick(60)