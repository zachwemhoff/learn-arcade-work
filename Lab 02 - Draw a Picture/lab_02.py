# Import the "arcade" library
import arcade

# Open up a window.
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color((38, 201, 255))

# Get ready to draw
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.FOREST_GREEN)

# --- Draw the House ---

# House Base
arcade.draw_lrtb_rectangle_filled(25, 325, 150, 100, arcade.color.DIM_GRAY)

# Bottom Half
arcade.draw_lrtb_rectangle_filled(25, 325, 375, 150, arcade.color.WHITE)

# Left-Middle Window
arcade.draw_rectangle_filled(90, 260, 30, 40, arcade.color.FERN_GREEN)
arcade.draw_rectangle_filled(90, 260, 20, 30, arcade.color.SEASHELL)

# Right-Middle Window
arcade.draw_rectangle_filled(260, 260, 30, 40, arcade.color.FERN_GREEN)
arcade.draw_rectangle_filled(260, 260, 20, 30, arcade.color.SEASHELL)

# Roof
arcade.draw_triangle_filled(180, 475, 15, 375, 335, 375, arcade.color.FERN_GREEN)

# Front Door
arcade.draw_rectangle_filled(180, 200, 40, 90, arcade.color.BLACK)
arcade.draw_rectangle_filled(180, 200, 35, 85, arcade.color.SEASHELL)

# Doorknob
arcade.draw_circle_filled(190, 200, 5, arcade.color.DIM_GRAY)

# --- Draw the Trees ---

# Circle Top Tree
arcade.draw_rectangle_filled(370, 180, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(370, 210, 30, arcade.csscolor.DARK_GREEN)

# Arc Top Tree
arcade.draw_rectangle_filled(450, 180, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(450, 210, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Triangle Top Tree
arcade.draw_rectangle_filled(530, 180, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(530, 480, 500, 210, 560, 210, arcade.csscolor.DARK_GREEN)

# Pentagon Top Tree
arcade.draw_rectangle_filled(620, 180, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((620, 260),
                            (600, 220),
                            (590, 180),
                            (650, 180),
                            (640, 220)
                            ),
                           arcade.csscolor.DARK_GREEN)

# Draw a sun
arcade.draw_circle_filled(700, 500, 80, ((255, 244, 41)))

# --- Draw the Clouds ---

# Draw right cloud
arcade.draw_circle_filled(350, 500, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(370, 510, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(350, 520, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(330, 510, 30, arcade.csscolor.WHITE)

# Draw middle cloud
arcade.draw_circle_filled(200, 540, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(220, 550, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(200, 560, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(180, 550, 30, arcade.csscolor.WHITE)

# Draw Left Cloud
arcade.draw_circle_filled(65, 495, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(85, 505, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(65, 515, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(45, 505, 30, arcade.csscolor.WHITE)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()