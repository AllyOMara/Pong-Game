import pygame
import random

# Setup
pygame.init()
BLACK                       = (0, 0, 0)
WHITE                       = (255, 255, 255)
GREY                        = (128, 128, 128)
screen_size                 = (800, 500)
screen                      = pygame.display.set_mode(screen_size)
lower_bound                 = 350
upper_bound                 = 0
player_1_y                  = 150
player_1_x                  = 20
player_1_up                 = pygame.K_w
player_1_down               = pygame.K_s
player_1_score              = 0
player_2_y                  = 150
player_2_x                  = 760
player_2_up                 = pygame.K_UP
player_2_down               = pygame.K_DOWN
player_2_score              = 0
ball_x                      = 375
ball_y                      = 235
ball_speed_x                = 11 # This is kept constant to ensure equal timing between each hit
ball_speed_y                = 6 # This is changed to vary gameplay (randomly generated)
running                     = False
FPS                         = 50
fpsClock                    = pygame.time.Clock()
player_move_units           = 50
start                       = False
font                        = pygame.font.Font(None, 60)
score_font                  = pygame.font.Font(None, 160)
clock                       = pygame.time.Clock()
starting_text               = font.render("Press any button to start", True, (255, 255, 255))
fullscreen_reminder         = font.render("Press ctrl to toggle fullscreen", True, (255, 255, 255))
text_rect_starter           = starting_text.get_rect(center=(400, 400))
text_rect_reminder          = fullscreen_reminder.get_rect(center=(400, 450))
player_1_score_text         = score_font.render(f"{player_1_score}", True, (128, 128, 128))
player_2_score_text         = score_font.render(f"{player_2_score}", True, (128, 128, 128))
text_player_2_score_text    = player_2_score_text.get_rect(center=(900, 50))
text_player_1_score_text    = player_1_score_text.get_rect(center=(400, 50))
ball_start_side             = random.randint(1, 2)
title_screen                = True
pong_title_screen_text      = font.render("PONG", True, (255, 255, 255))
text_rect_title_screen      = pong_title_screen_text.get_rect(center = (400,100))
start                       = font.render("start", True, (255, 255, 255))
rect_start                  = pong_title_screen_text.get_rect(center = (400,200))
how_to                      = font.render("PONG", True, (255, 255, 255))
how_to_rect                 = pong_title_screen_text.get_rect(center = (400,100))
title_option                = 1
player_selection_y          = 200
title_op_1                  = font.render("Start Game", True, (255, 255, 255))
title_op_2                  = font.render("Information", True, (255, 255, 255))
title_op_3                  = font.render("Quit Game", True, (255, 255, 255))
info_controls_p1            = font.render("Player 1 movement: w and s", True, (255, 255, 255))
info_controls_p2            = font.render("Player 2 movement: up and down", True, (255, 255, 255))
info_controls_quit          = font.render("Press esc to quit", True, (255, 255, 255))
player_1_score_text         = score_font.render(f"{player_1_score}", True, (128, 128, 128))
player_2_score_text         = score_font.render(f"{player_2_score}", True, (128, 128, 128))
text_player_2_score_text    = player_2_score_text.get_rect(center=(900, 50))
text_player_1_score_text    = player_1_score_text.get_rect(center=(400, 50))
info_screen                 = False
ball_start_angle            = random.randint(1, 2) # For variation at the beginning of the game
pygame.display.set_caption("Pong")
if ball_start_side      == 1:
    player_turn         = "left"
elif ball_start_side    == 2:
    player_turn         = "right"
if ball_start_angle     == 1:
    ball_y_direction    = "down"
elif ball_start_angle   == 2:
    ball_y_direction    = "up"
screen.fill(BLACK)

# Title Screen
while title_screen == True:
    # Display
    if info_screen == False:
        screen.fill(BLACK)
        screen.blit(pong_title_screen_text, text_rect_title_screen)
        screen.blit(title_op_1, (290, 200))
        screen.blit(title_op_2, (290, 275))
        screen.blit(title_op_3, (290, 350))
        pygame.draw.rect(screen, WHITE, (250, player_selection_y , 30, 30))
        pygame.display.flip()
    elif info_screen == True:
        screen.fill(BLACK)
        screen.blit(info_controls_p1, (25, 100))
        screen.blit(info_controls_p2, (25, 200))
        screen.blit(info_controls_quit, (25, 300))
        pygame.display.flip()
    # Choosing Menu Options
    for event in pygame.event.get():
        if title_option == 1:
            player_selection_y = 200
        if title_option == 2:
            player_selection_y = 275
        if title_option ==3 :
            player_selection_y = 350
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            # Toggle Fullscreen
            elif event.key == pygame.K_LCTRL:
                pygame.display.toggle_fullscreen()
                screen.blit(pong_title_screen_text, text_rect_title_screen)
            elif event.key == pygame.K_UP and title_option != 1:
                title_option = title_option - 1
            elif event.key == pygame.K_DOWN and title_option != 3:
                title_option = title_option + 1
            elif event.key == pygame.K_z or pygame.K_SPACE or pygame.K_RETURN:
                if title_option == 1:
                    title_screen    = False
                    start           = False
                elif title_option == 2 and info_screen == False:
                    info_screen = True
                elif title_option == 2 and info_screen == True:
                    info_screen = False
                elif title_option == 3:
                    pygame.quit()
            else:
                title_screen    = False
                start           = False
    
# Main Menu
screen.fill(BLACK)
pygame.draw.rect(screen, GREY, (385, 0, 10, 500))
pygame.draw.rect(screen, WHITE, (player_1_x, player_1_y, 20, 150))
pygame.draw.rect(screen, WHITE, (player_2_x, player_2_y, 20, 150))
pygame.draw.rect(screen, WHITE, (ball_x, ball_y , 30, 30))
screen.blit(starting_text, text_rect_starter)
screen.blit(fullscreen_reminder, text_rect_reminder)
pygame.display.flip()
fpsClock.tick(FPS)
while start == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            # Toggle Fullscreen
            elif event.key == pygame.K_LCTRL:
                pygame.display.toggle_fullscreen()
                screen.fill(BLACK)
                pygame.draw.rect(screen, GREY, (385, 0, 10, 500))
                pygame.draw.rect(screen, WHITE, (player_1_x, player_1_y, 20, 150))
                pygame.draw.rect(screen, WHITE, (player_2_x, player_2_y, 20, 150))
                pygame.draw.rect(screen, WHITE, (ball_x, ball_y , 30, 30))
                screen.blit(starting_text, text_rect_starter)
                screen.blit(fullscreen_reminder, text_rect_reminder)
                pygame.display.flip()
            else:
                start   = True
                running = True
begin_game = True

# Game Loop
while running:
    # Between Rounds
    while begin_game == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    elif event.key == pygame.K_LCTRL:
                        pygame.display.toggle_fullscreen()
                        screen.fill(BLACK)
                        pygame.draw.rect(screen, GREY, (385, 0, 10, 500))
                        pygame.draw.rect(screen, WHITE, (player_1_x, player_1_y, 20, 150))
                        pygame.draw.rect(screen, WHITE, (player_2_x, player_2_y, 20, 150))
                        pygame.draw.rect(screen, WHITE, (ball_x, ball_y , 30, 30))
                        screen.blit(starting_text, text_rect_starter)
                        screen.blit(fullscreen_reminder, text_rect_reminder)
                        screen.blit(player_1_score_text, text_player_1_score_text)
                        screen.blit(player_2_score_text, text_player_2_score_text)
                        pygame.display.flip()
                    else:
                        begin_game = True
    while begin_game == True:
        for event in pygame.event.get():
            # Quits
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                # Player Movement
                if event.key == player_1_up:
                    if player_1_y < upper_bound:
                        player_1_y == player_1_y
                    elif player_1_y > upper_bound:
                        player_1_y = player_1_y - player_move_units
                if event.key == player_1_down:
                    if player_1_y > lower_bound:
                        player_1_y = player_1_y
                    elif player_1_y < lower_bound:
                        player_1_y = player_1_y + player_move_units
                if event.key == player_2_up:
                    if player_2_y < upper_bound:
                        player_2_y == player_2_y
                    elif player_2_y > upper_bound:
                        player_2_y = player_2_y - player_move_units
                if event.key == player_2_down:
                    if player_2_y > lower_bound:
                        player_2_y = player_2_y
                    elif player_2_y < lower_bound:
                        player_2_y = player_2_y + player_move_units
        # Ball Movement
        if ball_y_direction == "up":
            if ball_y > 0:
                ball_y = ball_y - ball_speed_y
            elif ball_y <= 0:
                ball_y              = ball_y + ball_speed_y
                ball_y_direction    = "down"
        elif ball_y_direction == "down":
            if ball_y < 470:
                ball_y = ball_y + ball_speed_y
            elif ball_y >= 470:
                ball_y              = ball_y - ball_speed_y
                ball_y_direction    = "up"
        # Collision With Player 1
        if player_turn == "left":
            if ball_x > 0:
                if 20 <= ball_x <= 40 and player_1_y - 30 <= ball_y <= player_1_y + 150:
                    if player_1_y - 30 <= ball_y < player_1_y + 30:
                        ball_y_direction    = "up"
                        ball_speed_y        = random.randint(6,9)
                    elif player_1_y + 30 <= ball_y <= player_1_y + 90:
                        ball_speed_y = random.randint(1,4)
                    elif player_1_y + 90 < ball_y <= player_1_y + 150:
                        ball_y_direction    = "down"
                        ball_speed_y        = random.randint(6,9)
                    player_turn = "right"
                else:
                    ball_x = ball_x - ball_speed_x
            elif ball_x <= 0:
                player_2_score = player_2_score + 1
                player_1_y  = 150
                player_1_x  = 20
                player_2_y  = 150
                player_2_x  = 760
                ball_x      = 375
                ball_y      = 235
                begin_game  = False
            else:
                begin_game  = True
        # Collision With Player 2
        elif player_turn == "right":
            if 730 <= ball_x <= 750 and player_2_y - 30 <= ball_y <= player_2_y + 150:
                if player_2_y - 30 <= ball_y < player_2_y + 30:
                    ball_y_direction    = "up"
                    ball_speed_y        = random.randint(6,9)
                elif player_2_y + 30 <= ball_y <= player_2_y + 90:
                    ball_speed_y = random.randint(1,4)
                elif player_2_y + 90 < ball_y <= player_2_y + 150:
                    ball_y_direction    = "down"
                    ball_speed_y        = random.randint(6,9)
                player_turn = "left"
                ball_x      = ball_x - ball_speed_x
            if ball_x < 770:
                if 730 <= ball_x <= 750 and player_2_y - 15 <= ball_y <= player_2_y + 150:
                    random_ball_movement_x = random.randint(1, 2)
                    if random_ball_movement_x == 1:
                        ball_y_direction = "up"
                    elif random_ball_movement_x == 2:
                        ball_y_direction = "down"
                    ball_speed_y    = random.randint(1,10)
                    player_turn     = "left"
                    ball_x          = ball_x - ball_speed_x
                else:
                    ball_x = ball_x + ball_speed_x
            else:
                player_1_score = player_1_score + 1
                player_1_y  = 150
                player_1_x  = 20
                player_2_y  = 150
                player_2_x  = 760
                ball_x      = 375
                ball_y      = 235
                begin_game  = False
        # New Frame
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREY, (385, 0, 10, 500))
        player_1_score_text         = score_font.render(f"{player_1_score}", True, (128, 128, 128))
        player_2_score_text         = score_font.render(f"{player_2_score}", True, (128, 128, 128))
        text_player_2_score_text    = starting_text.get_rect(center=(900, 50))
        text_player_1_score_text    = fullscreen_reminder.get_rect(center=(400, 50))
        screen.blit(player_1_score_text, text_player_1_score_text)
        screen.blit(player_2_score_text, text_player_2_score_text)
        pygame.draw.rect(screen, WHITE, (ball_x, ball_y , 30, 30))
        pygame.draw.rect(screen, WHITE, (player_1_x, player_1_y, 20, 150))
        pygame.draw.rect(screen, WHITE, (player_2_x, player_2_y, 20, 150))
        pygame.display.flip()
        fpsClock.tick(FPS)

pygame.quit()