from __future__ import division
import pygame
from pygame import gfxdraw
import sys
import math
import robot
import layout
import mapper
import Pyro4

#Server connection
server = Pyro4.Proxy("PYRONAME:robot.server")    # use name server object lookup uri shortcut

#Init
pygame.init()
pygame.display.set_caption('Rescue Maze') #Window caption
pygame.mouse.set_visible(False) #Hide mouse cursor
screen = pygame.display.set_mode((layout.screen_width,layout.screen_height)) #Add pygame.FULLSCREEN as 2nd parameter of this function to get full-screen
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks() #Beginning match time 
FPS = 5 #Refreshing rate of the screen 
MAX_T = 480 #Match max duration, default 480 seconds

###Match parameters, changed real-time by the main program

robot_status = 'Exploring' #Can be 'Exploring', 'Lost' or whatever you want
robot_orientation = 2 #The orientation of the robot, integer number from 0 to 3
x_pos = 2 ##Robot coords in the matrix
y_pos = 2 ##
n_victims = 0 #Useless, simply shows on the screen the number of victims found
wall_map = [['3313','1133','3000','0000','0000','0000','0000','0000','0000','0000'], #THIS WILL BE CHANGED
	['3133','3131','3000','0000','0000','0000','0000','0000','0000','0000'], #Matrix containing walls informations, 4 chars string, starting from the left, going anti-clockwise
	['3111','1311','1323','2000','0000','0000','0000','0000','0000','0000'], #0 - unknown, 1 - No wall, 2 - Queued wall, 3 - Wall
	['3331','3003','0003','0000','0000','0000','0000','0000','0000','0000'],
	['0003','0000','0000','0000','0000','0000','0000','0000','0000','0000'],
	['0000','0000','0000','0000','0000','0000','0000','0000','0000','0000'],
	['0000','0000','0000','0000','0000','0000','0000','0000','0000','0000'],
	['0000','0000','0000','0000','0000','0000','0000','0000','0000','0000']]
node_map = [[2,2,0,0,0,0,0,0,0,0], #The exploration status of each cell,
	[2,2,0,0,0,0,0,0,0,0], #0 - unknown, 1 - exists/queued, 2 - explored
	[2,2,2,1,0,0,0,0,0,0],
	[2,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0]]

###End of match parameters

while True:

	#Retrieve data from server
	x_pos, y_pos = server.getRobotPosition()
	robot_orientation = server.getRobotOrientation()
		

	#Checking for events (Escape key, X button)
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			pygame.quit()
			sys.exit()

	#Window layout
	layout.draw_layout(screen, robot_status, n_victims, pygame.time.get_ticks(), start_time, MAX_T)

	#The map
	if(mapper.draw_map(screen, wall_map, node_map)==1):
		#The robot
		robot.draw_robot(screen, mapper.map_x_start, mapper.map_y_start, x_pos, y_pos, mapper.cell_size, robot_orientation, layout.light_blue)
	

	#RENDER
	pygame.display.update()
	clock.tick(FPS)
