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
	
	#Game Loop
	running = True
	
	while running: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
         
	screen.fill((255,255,255))
	pygame.display.update()


main()
	
	
