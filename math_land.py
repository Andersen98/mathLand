import sys

import pygame

from settings import Settings
import workspace_functions as ws_f
from cartesian_plane import Cartesian_Plane
from environment import Environment
from vector import Vector

def run_game():
	#initialize program, settings and create screen object
	pygame.init()
	ml_settings = Settings()
	screen = pygame.display.set_mode((ml_settings.screen_width, ml_settings.screen_height))
	pygame.display.set_caption("Math Land")

	#Initialize mathematical environment
	environment = Environment()
	environment.set_origin(Vector(screen.get_rect().centerx,screen.get_rect().centery))

	#Create Cartisian plane object
	cartesian_plane = Cartesian_Plane(environment)

  
    
	#Start main loop
	while True:
        
        	#Check for events
        	ws_f.check_events()
		
		#Update the environment
		
		

		#Update any objects on screen
		cartesian_plane.update(environment)

		#Draw the screen
		ws_f.update_screen(ml_settings, screen, cartesian_plane)

        
run_game()
