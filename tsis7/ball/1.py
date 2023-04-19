import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ball")

ball_color = (255, 0, 0)
ball_radius = 25
ball_position = [screen.get_width() // 2, screen.get_height() // 2]
ball_speed = 20

def draw_ball():
    pygame.draw.circle(screen, ball_color, ball_position, ball_radius)

running = True
while running:
    screen.fill((255, 255, 255))

    draw_ball()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_position[1] -= ball_speed
            elif event.key == pygame.K_DOWN:
                ball_position[1] += ball_speed
            elif event.key == pygame.K_LEFT:
                ball_position[0] -= ball_speed
            elif event.key == pygame.K_RIGHT:
                ball_position[0] += ball_speed

    ball_position[0] = max(ball_position[0], ball_radius)
    ball_position[0] = min(ball_position[0], screen.get_width() - ball_radius)
    ball_position[1] = max(ball_position[1], ball_radius)
    ball_position[1] = min(ball_position[1], screen.get_height() - ball_radius)

    pygame.display.update()

pygame.quit()