import pygame
import layout

def show_error(draw_surface):
    draw_surface.fill(layout.black)
    label1 = layout.render_text("Connection error, closing.", layout.white, layout.black, layout.big_font)
    l1w, l1h = label1.get_size()
    draw_surface.blit(label1, (layout.screen_width/2 - l1w/2, layout.screen_height/2 - l1h/2))