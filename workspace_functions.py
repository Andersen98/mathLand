import sys

import pygame

def check_events():
	"""respond to keypresses and mouse events"""
	for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        		sys.exit()


def update_screen(ml_settings,screen, cartesian_plane):
	"""Update images on the screen and flip the new screen."""
 	#Redraw the dcreen during each pass through the loop
    	screen.fill(ml_settings.bg_color)

	#Draw the cartesian plane
	cartesian_plane.draw(ml_settings,screen)

        
    	#Make the most recetly drawn screen visible
    	pygame.display.flip()
