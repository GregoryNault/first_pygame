import pygame, os
WIDTH, HEIGHT = 900, 500
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

VEL = 5

FPS = 60

BORDER = pygame.Rect(WIDTH/2 -5, 0, 10, HEIGHT)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First PYGAME window!")

# import spaceship images, use os to define path (or you can copy the file path)
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_red.png'))
# resize and rotate images
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(red, yellow):
    WIN.fill(WHITE)
    # Use blit to put images/test (surfaces) onto the screen.
    # Drawing on a screen has the top left corner set at (0,0), images anchor point is top left of image.
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    # the red.x, red.y means you are setting the position to the red rectangle created. When you move the rectangle
    # you will move the spaceship because they are attached.
    # normally you would put pixel coordinates: WIN.blit(item, (100, 200)) for example.
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))
    pygame.draw.rect(WIN, BLACK, BORDER)
    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:  # move yellow LEFT using 'a' key.
        yellow.x -= VEL
    if keys_pressed[pygame.K_d]:  # move yellow RIGHT using 'd' key.
        yellow.x += VEL
    if keys_pressed[pygame.K_w]:  # move yellow UP using 'w' key.
        yellow.y -= VEL
    if keys_pressed[pygame.K_s]:  # move yellow DOWN using 's' key.
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    print("hi")

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Any keys that are pressed are assigned to the keys_pressed variable
        keys_pressed = pygame.key.get_pressed()

        # The keys pressed is passed to this function which handles movement for the yellow/red player.
        yellow_handle_movement(keys_pressed, yellow)
        #red_handle_movement(keys_pressed, red)

        draw_window(red, yellow)




    pygame.quit()


if __name__ == "__main__":
    main()

