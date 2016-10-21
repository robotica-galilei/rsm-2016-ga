import math
import pygame
from pygame import gfxdraw

def rotate_point(origin, point, angle):
	ox, oy = origin
	px, py = point
	qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
	qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
	return qx, qy

def generate_cursor(c_size, c_orient, x0, y0):
	robot_cursor = [(c_size, c_size), (0, int(c_size/2)), (c_size, 0), (int(c_size*3/4), int(c_size/2)), (c_size, c_size)]
	cursor_rot = []	
	for i in robot_cursor:
		cursor_rot.append(rotate_point((int(c_size/2), int(c_size/2)),i,-c_orient*math.pi/2))
	cursor_fin = []
	for i in range(0,len(robot_cursor)):
		cursor_fin.append((cursor_rot[i][0] + x0, cursor_rot[i][1] + y0))
	return cursor_fin


def draw_robot(draw_surface, x0,y0, x_coord, y_coord, cell_size, orientation, robot_color):
	cursor_size = cell_size * 2 / 3
	robot_pointlist = generate_cursor(cursor_size, orientation, x0 + x_coord*cell_size + cell_size/2 - cursor_size/2, y0 + y_coord*cell_size + cell_size/2 - cursor_size/2)
	pygame.gfxdraw.aapolygon(draw_surface, robot_pointlist, robot_color)
	pygame.gfxdraw.filled_polygon(draw_surface, robot_pointlist, robot_color)
