import pygame
# Initialzing
pygame.init()

# Setting up FPS
FPS = 30
clock = pygame.time.Clock()
# Colors
backgroundColor=(255,255,255)
# screen
screenWidth, screenHeight = 1820, 999
displaySurface = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Efficient MOBA!")
# Game Loop
isRunning = True
while isRunning:
    time_delta = clock.tick(FPS) / 1000.0 # Time since last loop
    displaySurface.fill(backgroundColor)
    # User interface events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
              isRunning = False
    # Action Keys, Mouse
    pressed_keys = pygame.key.get_pressed()
    mx, my = pygame.mouse.get_pos()

    pygame.draw.circle(displaySurface, (177,117,17), (100, 100), 100, 0) #(r, g, b) is color, (x, y) is center, R is radius and w is the thickness of the circle border.

    # Update display
    pygame.display.update()
