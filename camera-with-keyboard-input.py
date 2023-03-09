import pygame

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the caption of the window
pygame.display.set_caption("My Simple Game")

# Create the clock object
clock = pygame.time.Clock()

# Set the background color
BACKGROUND_COLOR = (255, 255, 255)

# Set the player size
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

# Set the player initial position
player_x = WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2
player_y = WINDOW_HEIGHT - PLAYER_HEIGHT - 20

# Set the player speed
PLAYER_SPEED = 10

# Set the camera offset
camera_offset_x = 0

# Set the static rectangle colors
RECTANGLE_COLOR_1 = (255, 0, 0)
RECTANGLE_COLOR_2 = (0, 0, 255)

# Set the static rectangle positions and sizes
rectangle_1 = pygame.Rect(200, 200, 100, 100)
rectangle_2 = pygame.Rect(500, 300, 150, 50)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                player_x += PLAYER_SPEED

    # Update the camera offset
    camera_offset_x = WINDOW_WIDTH // 2 - player_x - PLAYER_WIDTH // 2

    # Draw the background
    screen.fill(BACKGROUND_COLOR)

    # Draw the static rectangles
    rectangle_1_draw_pos = rectangle_1.move(camera_offset_x, 0)
    pygame.draw.rect(screen, RECTANGLE_COLOR_1, rectangle_1_draw_pos)
    
    rectangle_2_draw_pos = rectangle_2.move(camera_offset_x, 0)
    pygame.draw.rect(screen, RECTANGLE_COLOR_2, rectangle_2_draw_pos)

    # Draw the player
    player_rect = pygame.Rect(player_x + camera_offset_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    pygame.draw.rect(screen, (0, 0, 0), player_rect)

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(30)
