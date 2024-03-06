import pygame
import opdracht6Class   

pygame.init()
pygame.display.set_caption('Assignment 6')
running = True

background = pygame.image.load(r"veld.png") 
background_width, background_height = background.get_width(), background.get_height()
frame = pygame.display.set_mode((background_width, background_height))

# Set up player
x_player, y_player, player_speed = background_width//2, background_height//2, 5
player_image = pygame.image.load(r"speler.png")

obstacles = []
obstacle_image = pygame.image.load(r"obstakel.png")

clock = pygame.time.Clock()
FPS = 60

while running:
    
    # ACTION 1: Process user inputs
    pygame.event.pump()
    keys = pygame.key.get_pressed()

    can_move, movement = True, (0, 0)
    if keys[pygame.K_a]:        
        movement = (-player_speed, 0)
    elif keys[pygame.K_d]:        
        movement = (player_speed, 0)
    elif keys[pygame.K_w]:      
        movement = (0, -player_speed)
    elif keys[pygame.K_s]:     
        movement = (0, player_speed)

    # If left mouse button is pressed, place an obstacle (by creating it as a Rect and adding it to the list).
    if pygame.mouse.get_pressed()[0]:
        mouse_position = pygame.mouse.get_pos()
        x_obstacle, y_obstacle = mouse_position[0]-obstacle_image.get_width()//2, mouse_position[1]-obstacle_image.get_height()//2
        obstacle = pygame.Rect(x_obstacle, y_obstacle, obstacle_image.get_width(), obstacle_image.get_height())
        obstacles.append(obstacle)

    # Quit the game when the close button is pressed.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ACTION 2: Modify game state
    clock.tick(FPS)  # Maintain a constant frame rate.

    # Check if the player is allowed to move with the determined movement in ACTION 1.
    new_x_player = x_player + movement[0]
    new_y_player = y_player + movement[1]

    # If the new position puts the player outside the frame boundaries, movement is not allowed.
    if (new_x_player < 0) or (new_x_player + player_image.get_width() > background_width):
        can_move = False
    if (new_y_player < 0) or (new_y_player + player_image.get_height() > background_height):
        can_move = False

    # If the new position would place the player in an obstacle, movement is not allowed.
    player_rect = pygame.Rect(new_x_player, new_y_player, player_image.get_width(), player_image.get_height())
    if player_rect.collidelist(obstacles) != -1:
        can_move = False

    if can_move:  # If the player is still allowed to move after checks, move the player to the new position.
        x_player = new_x_player
        y_player = new_y_player

    # ACTION 3: Draw & display frame
    frame.blit(background, (0, 0))  # Clear the frame by filling it with white.

    frame.blit(player_image, (x_player, y_player))  # Draw the player.
    for obstacle in obstacles:
        frame.blit(obstacle_image, (obstacle[0], obstacle[1]))  # Draw obstacles.

    pygame.display.flip()  # Display the frame

pygame.quit()