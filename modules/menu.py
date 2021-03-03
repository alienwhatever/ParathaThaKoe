def menu(pygame, sys, size):
    pygame.init()

    # colors
    black = 0, 0, 0
    white = 255, 255, 255
    bgColor = 255, 111, 8 # button background color

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Paratha Tha Koe")

    # create objects
    bg = pygame.image.load('./img/paratha.jpeg') # load background image

    mainCharacter = pygame.image.load('./img/MainCharacter.png')
    mainCharacterRect = mainCharacter.get_rect()
    mainCharacterRect.x = 1
    mainCharacterRect.y = -100
    mainCharacterAnimationSpeed =  0.1
    mainCharacterAnimationSpeedMinus = -1
    mainCharacterAnimation = mainCharacterAnimationSpeed

    # buttons
    # buttons are 100 Y away from each other

    buttonFont = pygame.font.SysFont('Corbel', 35)
    playButton = buttonFont.render('Play', True, white)
    playButtonX = 100
    playButtonY = 130

    exitButton = buttonFont.render('Exit', True, white)
    exitButtonX = 100
    exitButtonY = playButtonY + 100

    creditButton = buttonFont.render('Credits', True, white)
    creditButtonX = 100
    creditButtonY = exitButtonY + 100

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            # detect mouse click and check if user click on a button
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                # If user click on Plau button
                if mouse[0] >= playButtonX - 25 and mouse[0] <= playButtonX - 25 + 100: # 100 is width of playButtonX
                    # does user clicked cordinates also match with y
                    if mouse[1] >= playButtonY - 15 and mouse[1] <= playButtonY - 15 + 50: # 50 is height of playButtonY
                        # user clicked the button
                        return 'play'

                # If user click on Exit button
                if mouse[0] >= exitButtonX - 25 and mouse[0] <= exitButtonX - 25 + 100: # 100 is width of exitButtonX
                    # does user clicked cordinates also match with y
                    if mouse[1] >= exitButtonY - 15 and mouse[1] <= exitButtonY - 15 + 50: # 50 is height of exitButtonY
                        # user clicked the button
                        sys.exit()

                # If user click on Credits button
                if mouse[0] >= creditButtonX - 25 and mouse[0] <= creditButtonX - 25 + 125: # 100 is width of creditButtonX
                    # does user clicked cordinates also match with y
                    if mouse[1] >= creditButtonY - 15 and mouse[1] <= creditButtonY - 15 + 50: # 50 is height of creditButtonY
                        # user clicked the button
                        return 'Credits'



        screen.blit(bg, (0, 0)) # draw background image

        # animation
        mainCharacterRect.y += mainCharacterAnimation

        if(mainCharacterRect.y == 0): mainCharacterAnimation = mainCharacterAnimationSpeedMinus
        if(mainCharacterRect.y == -100): mainCharacterAnimation = mainCharacterAnimationSpeed
        # print(mainCharacterRect.y)

        # display objects
        screen.blit(mainCharacter, mainCharacterRect)

        # buttons
        pygame.draw.rect(screen, bgColor, [playButtonX - 25, playButtonY - 15, 100, 50]) # x Y width height
        screen.blit(playButton, (playButtonX, playButtonY)) # x, y

        pygame.draw.rect(screen, bgColor, [exitButtonX - 25, exitButtonY - 15, 100, 50]) # x Y width height
        screen.blit(exitButton, (exitButtonX, exitButtonY)) # x, y

        pygame.draw.rect(screen, bgColor, [creditButtonX - 25, creditButtonY - 15, 125, 50]) # x Y width height
        screen.blit(creditButton, (creditButtonX, creditButtonY)) # x, y

        pygame.display.flip()
        pygame.display.update()
