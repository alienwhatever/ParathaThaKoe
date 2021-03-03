# show message to player

def showMessage(pygame, sys, size):
    pygame.init()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Paratha Tha Koe")

    text = pygame.font.Font('./font/super-legend-boy-font/SuperLegendBoy-4w8Y.ttf', 35)
    msg = text.render('You Lose', True, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(msg, (200, 215))

        pygame.display.flip()
        pygame.display.update()
