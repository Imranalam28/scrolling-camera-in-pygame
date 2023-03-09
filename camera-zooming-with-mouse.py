import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Simple Game")

clock = pygame.time.Clock()

BACKGROUND_COLOR = (255, 255, 255)

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

player_x = WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2
player_y = WINDOW_HEIGHT - PLAYER_HEIGHT - 20

PLAYER_SPEED = 10

camera_offset_x = 0
zoom = 1.0

def get_scaled_size(size):
    return int(size * zoom)


RECTANGLE_COLOR_1 = (255, 0, 0)
RECTANGLE_COLOR_2 = (0, 0, 255)

rectangle_1 = pygame.Rect(200, 200, 100, 100)
rectangle_2 = pygame.Rect(500, 300, 150, 50)

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Handle events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_start_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                mouse_current_pos = pygame.mouse.get_pos()
                mouse_offset_x = mouse_current_pos[0] - mouse_start_pos[0]
                player_x -= mouse_offset_x
                mouse_start_pos = mouse_current_pos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                zoom += 0.1
                screen = pygame.display.set_mode((int(WINDOW_WIDTH * zoom), int(WINDOW_HEIGHT * zoom)))
            elif event.key == pygame.K_MINUS:
                zoom -= 0.1
                if zoom < 0.1:
                    zoom = 0.1
                screen = pygame.display.set_mode((int(WINDOW_WIDTH * zoom), int(WINDOW_HEIGHT * zoom)))


    # Draw the background
    screen.fill(BACKGROUND_COLOR)

    camera_offset_x = WINDOW_WIDTH // 2 - player_x - PLAYER_WIDTH // 2

    # Draw the static rectangles
    rectangle_1_draw_pos = pygame.Rect(get_scaled_size(rectangle_1.x + camera_offset_x),
                                    get_scaled_size(rectangle_1.y),
                                    get_scaled_size(rectangle_1.width),
                                    get_scaled_size(rectangle_1.height))
    pygame.draw.rect(screen, RECTANGLE_COLOR_1, rectangle_1_draw_pos)

    rectangle_2_draw_pos = pygame.Rect(get_scaled_size(rectangle_2.x + camera_offset_x),
                                        get_scaled_size(rectangle_2.y),
                                        get_scaled_size(rectangle_2.width),
                                        get_scaled_size(rectangle_2.height))
    pygame.draw.rect(screen, RECTANGLE_COLOR_2, rectangle_2_draw_pos)


    # Draw the player
    player_rect = pygame.Rect(get_scaled_size(player_x + camera_offset_x),
                          get_scaled_size(player_y),
                          get_scaled_size(PLAYER_WIDTH),
                          get_scaled_size(PLAYER_HEIGHT))

    pygame.draw.rect(screen, (0, 0, 0), player_rect)


    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(30)
