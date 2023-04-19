import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("Music Player")

pygame.mixer.music.load("song.mp3")

pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                pygame.mixer.music.load("song.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_b:
                pygame.mixer.music.load("song.mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    pygame.display.update()