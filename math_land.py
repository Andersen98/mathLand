import sys

import pygame

from settings import Settings
import workspace_functions as ws_f
from math_lib.cartesian_plane import Cartesian_Plane
from math_lib.environment import Environment
from math_lib.vector import Vector

def run_game():
    #initialize program, settings and create screen object
    #comment for first commit sina
    pygame.init()
    ml_settings = Settings()
    screen = pygame.display.set_mode((ml_settings.screen_width, ml_settings.screen_height))
    pygame.display.set_caption("Math Land")
    #Initialize mathematical environment
    environment = Environment()
    #Environment origin is set to center of screen
<<<<<<< HEAD
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
=======
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

        #def not being a jerk

        
>>>>>>> 9933647b90916a4cd01fbdeab7d8ff9e0d60ce58
run_game()
