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

robot_status = 'Default' #Can be 'Exploring', 'Lost' or whatever you want
robot_orientation = 0 #The orientation of the robot, integer number from 0 to 3
x_pos = 0 ##Robot coords in the matrix
y_pos = 0 ##
n_victims = 0 #Useless, simply shows on the screen the number of victims found
elapsed_time = 0
wall_map = []
node_map = []

###End of match parameters

while True:

	#Retrieve data from server
	x_pos, y_pos = server.getRobotPosition()
	robot_orientation = server.getRobotOrientation()
	robot_status = server.getRobotStatus()
	n_victims = server.getVictimsNumber()
	elapsed_time = server.getElapsedTime()
	wall_map = server.getWallMap()
	node_map = server.getNodeMap()

	#Checking for events (Escape key, X button)
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			pygame.quit()
			sys.exit()

	#Window layout
	layout.draw_layout(screen, robot_status, n_victims, elapsed_time, MAX_T)

	#The map
	if(mapper.draw_map(screen, wall_map, node_map)==1):
		#The robot
		robot.draw_robot(screen, mapper.map_x_start, mapper.map_y_start, x_pos, y_pos, mapper.cell_size, robot_orientation, layout.light_blue)
	

	#RENDER
	pygame.display.update()
	clock.tick(FPS)
