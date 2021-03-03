# creditpage

def creditpage(pygame, sys, size):

    pygame.init()
    text_color = (255, 255, 255)

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Paratha Tha Koe")

    text = pygame.font.Font('./font/super-legend-boy-font/SuperLegendBoy-4w8Y.ttf', 9)

    creditTitle = "Credits"
    credit = text.render(creditTitle, True, text_color)

    # credits
    credit1 = text.render("./img/bomb.png : http://pngimg.com/image/24081", True, text_color)
    credit2 = text.render("./img/MainCharacter.png : From a facebook user/page", True, text_color)
    credit3 = text.render("./img/paratha.jpeg : https://upload.wikimedia.org/wikipedia/commons/f/fc/Alooparatha.jpg", True, text_color)

    # to add more credits add more credit variable here and add more 'screen.blit'
    # credits are 30 y away from each other

    screen.fill((0, 0, 0)) # background color

    screen.blit(credit, (0, 0)) # title

    # credits
    screen.blit(credit1, (0, 30)) # x, y
    screen.blit(credit2, (0, 60))
    screen.blit(credit3, (0, 90))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        pygame.display.flip()
