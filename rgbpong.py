import pygame, sys, random
# import matplotlib.pyplot as plt TODO: reimplement stats

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1
    
    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()
    
    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 10:
            ball_speed_y *= -1

    if ball.colliderect(opponent) and ball_speed_x < 0:
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
    if player_score - opponent_score >= 7:
        return 14
    if player_score - opponent_score <= -4:
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
pong_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")
music_sound = pygame.mixer.Sound("music.ogg")
music = 0
versus = -1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
        if pygame.key.get_pressed()[pygame.K_1]: # default
            theme_num = 1
        if pygame.key.get_pressed()[pygame.K_2]: # Matrix
            theme_num = 2
        if pygame.key.get_pressed()[pygame.K_0]:
            theme_num = 0
        if pygame.key.get_pressed()[pygame.K_v]:
            versus = 1
            print("Versus Mode Activated")
            opponent_speed = 0
        if pygame.key.get_pressed()[pygame.K_x]:
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
    
    while music == 0:
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