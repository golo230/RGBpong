import pygame, sys, random
import numpy as np
import matplotlib.pyplot as plt

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        if sounderror == 0:
            pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1
    
    if ball.left <= 0:
        if sounderror == 0:
            pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        if sounderror == 0:
            pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()
    
    if ball.colliderect(player) and ball_speed_x > 0:
        if sounderror == 0:
            pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 10:
            ball_speed_y *= -1

    if ball.colliderect(opponent) and ball_speed_x < 0:
        if sounderror == 0:
            pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 10:
            ball_speed_y *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y, score_time
    pygame.draw.rect(screen, bg_color, (screen_width/2,screen_height/2 + 20, 32, 32))
    ball.center = (screen_width/2, screen_height/2)

    current_time = pygame.time.get_ticks()
    
    if current_time - score_time < 700:
        number_three = game_font.render("3", False, accent_color)
        screen.blit(number_three, (screen_width / 2 - 10, screen_height / 2 + 20))
    
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, accent_color)
        screen.blit(number_two, (screen_width / 2 - 10, screen_height / 2 + 20))
    
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, accent_color)
        screen.blit(number_one, (screen_width / 2 - 10, screen_height / 2 + 20))
    
    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None

def difficulty():
    if player_score - opponent_score >= 4:
        return 11
    elif player_score - opponent_score >= 7:
        return 14
    elif player_score - opponent_score >= 10:
        return 17
    elif player_score - opponent_score <= -4:
        return 5
    else:
        return 7

def set_theme():
    global bg_color, accent_color
    if theme_num == 0:
        bg_color = (0, 0, 0)
        accent_color = (0, 0, 0)
    if theme_num == 1:
        bg_color = pygame.Color("#2F373F")
        accent_color = (200, 200, 200)
    if theme_num == 2:
        bg_color = (0, 0, 0)
        accent_color = (0, 127, 0)
    if theme_num == 3:
        bg_color = (0, 0, 0)
        accent_color = (255, 255, 255)
    if theme_num == 4:
        bg_color = (255, 255, 255) # TODO?
        accent_color = (0, 0, 0)
    if theme_num == 5:
        bg_color = pygame.Color("#00539cff")
        accent_color = pygame.Color("#ffd662ff")
    if theme_num == 6:
        bg_color = pygame.Color("#343148ff") # TODO
        accent_color = pygame.Color("#d7c49eff")
    if theme_num == 7:
        bg_color = pygame.Color("#333333")
        accent_color = pygame.Color("#ff7f00")
    if theme_num == 8:
        bg_color = pygame.Color("#89abe3ff") # TODO
        accent_color = pygame.Color("#fcf6f5ff")
    if theme_num == 9:
        bg_color = pygame.Color("#3c1053ff") # TODO
        accent_color = pygame.Color("#df6589ff")

# Setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("RGBPong")

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30) # coordinates (0,0) is at top left
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Colors
bg_color = pygame.Color("#2F373F")
accent_color = (200, 200, 200)

# Variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)
score_time = True
theme_num = 1

# Sound
sounderror = 0
try:
    pong_sound = pygame.mixer.Sound("pong.ogg")
    score_sound = pygame.mixer.Sound("score.ogg")
    music_sound = pygame.mixer.Sound("music.ogg")
except:
    print("ERROR: could not load sounds")
    sounderror = 1

music = 0
versus = -1

menu_call = 1

def menu_loop():
    global menu_call, score_time
    quit_button = pygame.Rect(screen_width/2 - 125, screen_height/2+50, 250, 50)
    play_button = pygame.Rect(screen_width/2 - 125, screen_height/2-50, 250, 50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and quit_button.collidepoint(event.pos)) or pygame.key.get_pressed()[pygame.K_q]:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and play_button.collidepoint(event.pos):
                print("success")
                menu_call = 0
                break

        screen.fill(bg_color)

        text_color = pygame.Color("#000000")
        quit_color = pygame.Color("#0002ff")
        title_color = pygame.Color("#ff2d00")
        play_color = pygame.Color("#00ff02")

        pygame.draw.rect(screen, play_color, play_button)
        pygame.draw.rect(screen, quit_color, quit_button)
        pygame.draw.rect(screen, accent_color, player)
        pygame.draw.rect(screen, accent_color, opponent)

        play_text = game_font.render("PLAY", False, text_color)
        screen.blit(play_text, (screen_width/2 - 40, screen_height/2-40))
        quit_text = game_font.render("QUIT", False, text_color)
        screen.blit(quit_text, (screen_width/2 - 40, screen_height/2+60))
        
        title_text = game_font.render("RGBPong", False, title_color)
        screen.blit(title_text, (screen_width/2 - 80, screen_height/2-200))
        pygame.display.flip() # updates window
        clock.tick(60) # limits to 60 ticks

        if menu_call == 0:
            score_time = pygame.time.get_ticks()
            break

while True:
    if menu_call == 1:
        menu_loop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("score.txt", "a") as file1:
                if player_score != 0 or opponent_score != 0:
                    file1.write(f"Player's Score: {player_score}\n")
                    file1.write(f"Opponent's Score: {opponent_score}\n\n")
                    print("Stats saved successfully!")
            with open("wlr.txt", "a") as file2:
                if player_score > opponent_score:
                    file2.write("1\n")
                elif player_score < opponent_score:
                    file2.write("-1\n")
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7          
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_p:
                player_wins = 0
                opponent_wins = 0
                with open("wlr.txt", "r") as file:
                    for line in file:
                        if line == "1\n":
                            player_wins += 1
                        else:
                            opponent_wins += 1
                    mylabels = ["Your Wins", "Opponent's Wins"]
                    if player_wins != 0 or opponent_wins != 0:
                        plt.pie(np.array([player_wins, opponent_wins]), labels=mylabels)
                        plt.legend()
                        plt.show()
            if event.key == pygame.K_c:
                with open("wlr.txt", "w") as file3:
                    pass
                with open("score.txt", "w") as file4:
                    pass
                print("Stats cleared")
        if pygame.key.get_pressed()[pygame.K_1]: # default
            theme_num = 1
        if pygame.key.get_pressed()[pygame.K_2]: # Matrix
            theme_num = 2
        if pygame.key.get_pressed()[pygame.K_3]: # classic
            theme_num = 3
        if pygame.key.get_pressed()[pygame.K_4]: # reverse classic
            theme_num = 4
        if pygame.key.get_pressed()[pygame.K_5]: # Berkeley
            theme_num = 5
        if pygame.key.get_pressed()[pygame.K_6]: # mellow
            theme_num = 6
        if pygame.key.get_pressed()[pygame.K_7]: # half life
            theme_num = 7
        if pygame.key.get_pressed()[pygame.K_8]: # cloud in the sky
            theme_num = 8
        if pygame.key.get_pressed()[pygame.K_9]: # purple
            theme_num = 9
        if pygame.key.get_pressed()[pygame.K_0]: # blackout (joke scheme)
            theme_num = 0
        if pygame.key.get_pressed()[pygame.K_q]:
            pygame.quit()
            sys.exit()
        if pygame.key.get_pressed()[pygame.K_v]:
            if versus != 1:
                versus = 1
                print("Versus Mode Activated")
                opponent_speed = 0
        if pygame.key.get_pressed()[pygame.K_x]:
            if versus != -1:
                versus = -1
                opponent_speed = 7
                print("AI Mode Activated")
        if versus == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    opponent_speed += 7
                if event.key == pygame.K_w:
                    opponent_speed -= 7          
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    opponent_speed -= 7
                if event.key == pygame.K_w:
                    opponent_speed += 7
    
    while music == 0 and sounderror == 0:
        pygame.mixer.Sound.play(music_sound)
        music += 1

    set_theme()
    ball_animation()
    player_animation()
    if versus == -1:
        opponent_ai()
        opponent_speed = difficulty()
    else:
        opponent_animation()

    screen.fill(bg_color) # drawn first
    pygame.draw.aaline(screen, accent_color, (screen_width/2, 0), (screen_width/2, screen_height))
    pygame.draw.rect(screen, accent_color, player)
    pygame.draw.rect(screen, accent_color, opponent)
    pygame.draw.ellipse(screen, accent_color, ball)

    if score_time:
        ball_restart()

    player_text = game_font.render(f"{player_score}", False, accent_color)
    screen.blit(player_text, (660, 470))
    opponent_text = game_font.render(f"{opponent_score}", False, accent_color)
    screen.blit(opponent_text, (600, 470))

    pygame.display.flip() # updates window
    clock.tick(60) # limits to 60 ticks