
    import pygame 

            #Main func 
    def main() : 
                        #Init PyGame 
                        pygame.init()

                        #Creating Screen
                        screen = pygame.display.set_mode((800,600))
                        
                        #Init title and logo
                        pygame.display.set_caption('Space Pirates')
                        icon = pygame.image.load("pirate.png")
                        pygame.display.set_icon(icon )

                        x = 50
                        y = 50
                        width = 60
                        height = 40
                        vel = 5
			screen_dim = 500
                        
                        #Game Loop
                        running = True
                        
                        while running: 
                                pygame.time.delay(100)	

                                for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                                running = False

                            keys = pygame.key.get_pressed()
                            
                            
                            

                            if keys[pygame.K_LEFT] and x > vel:
                                    x -= vel

                            if keys[pygame.K_RIGHT] and x < screen_dim - width - height:
                                    x += vel

                            if keys[pygame.K_UP] and y < vel:	
                                    y -= vel
             
                            if keys[pygame.K_DOWN] and y > screen_dim - width - height :	
                                    y += vel
                            
                            screen.fill((0,0,0)) 
                            pygame.draw.rect(screen, (255,0,0),(x,y,width,height) )
                            pygame.display.update()
                    
                    pygame.quit()





            main()
                    
                

