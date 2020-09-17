# Import the "arcade" library
import arcade

# Open up a window.
arcade.open_window(800, 600, "Drawing With Functions")


def draw_house(x, y):
    """Draw the House"""

    # House Base
    arcade.draw_lrtb_rectangle_filled(25, 325, 150 + x, 100 + y, arcade.color.DIM_GRAY)

    # Bottom Half
    arcade.draw_lrtb_rectangle_filled(25, 325, 375 + x, 150 + y, arcade.color.WHITE)

    # Roof
    arcade.draw_triangle_filled(180 + x, 475 + y, 15 + x, 375 + y, 335 + x, 375 + y, arcade.color.FERN_GREEN)

    # Front Door
    arcade.draw_rectangle_filled(180, 200, 40 + x, 90 + y, arcade.color.BLACK)
    arcade.draw_rectangle_filled(180, 200, 35 + x, 85 + y, arcade.color.SEASHELL)

    # Doorknob
    arcade.draw_circle_filled(190 + x, 200 + y, 5, arcade.color.DIM_GRAY)


def draw_windows(x, y):
    """Draw the windows"""

    # Left Window
    arcade.draw_rectangle_filled(90, 260, 30 + x, 40 + y, arcade.color.FERN_GREEN)
    arcade.draw_rectangle_filled(90, 260, 20 + x, 30 + y, arcade.color.SEASHELL)

    # Right Window
    arcade.draw_rectangle_filled(260, 260, 30 + x, 40 + y, arcade.color.FERN_GREEN)
    arcade.draw_rectangle_filled(260, 260, 20 + x, 30 + y, arcade.color.SEASHELL)


def draw_trees(x, y):
    """Draw the trees"""

    # Circle Top Tree
    arcade.draw_rectangle_filled(370, 180, 20 + x, 60 + y, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(370 + x, 210 + y, 30, arcade.csscolor.DARK_GREEN)

    # Arc Top Tree
    arcade.draw_rectangle_filled(450, 180, 20 + x, 60 + y, arcade.csscolor.SIENNA)
    arcade.draw_arc_filled(450, 210, 60 + x, 100 + y, arcade.csscolor.DARK_GREEN, 0, 180)

    # Triangle Top Tree
    arcade.draw_rectangle_filled(530, 180, 20 + x, 60 + y, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(530 + x, 480 + y, 500 + x, 210 + y, 560 + x, 210 + y, arcade.csscolor.DARK_GREEN)

    # Pentagon Top Tree
    arcade.draw_rectangle_filled(620, 180, 20 + x, 60 + y, arcade.csscolor.SIENNA)
    arcade.draw_polygon_filled(((620 + x, 260 + y),
                                (600 + x, 220 + y),
                                (590 + x, 180 + y),
                                (650 + x, 180 + y),
                                (640 + x, 220 + y)
                                ),
                               arcade.csscolor.DARK_GREEN)


def draw_clouds(x, y):
    """Draw the clouds"""

    # Draw right cloud
    arcade.draw_circle_filled(350 + x, 500 + y, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(370 + x, 510 + y, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(350 + x, 520 + y, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(330 + x, 510 + y, 30, arcade.csscolor.WHITE)

    # Draw middle cloud
    arcade.draw_circle_filled(200 + x, 540 + y, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(220 + x, 550 + y, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(200 + x, 560 + y, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(180 + x, 550 + y, 30, arcade.csscolor.WHITE)

    # Draw Left Cloud
    arcade.draw_circle_filled(65 + x, 495 + y, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(85 + x, 505 + y, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(65 + x, 515 + y, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(45 + x, 505 + y, 30, arcade.csscolor.WHITE)


def main():

    # Set the background color
    arcade.set_background_color((38, 201, 255))

    # Get ready to draw
    arcade.start_render()

    # Draw the grass
    arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.FOREST_GREEN)

    # Draw a sun
    arcade.draw_circle_filled(700, 500, 80, (255, 244, 41))

    draw_house(0, 0)
    draw_windows(10, 10)
    draw_trees(0, 0)
    draw_clouds(5, 5)

    # Finish drawing and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
