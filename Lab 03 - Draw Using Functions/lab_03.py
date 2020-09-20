# Import the "arcade" library
import arcade

# Open up a window.
arcade.open_window(800, 600, "Drawing With Functions")


def draw_house(x, y):
    """Draw the House"""

    # House Base
    arcade.draw_lrtb_rectangle_filled(x, x + 300, y, y - 50, arcade.color.DIM_GRAY)

    # Bottom Half
    arcade.draw_lrtb_rectangle_filled(x, x + 300, y + 225, y, arcade.color.WHITE)

    # Roof
    arcade.draw_triangle_filled(x + 155, y + 325, x - 10, y + 225, x + 310, y + 225, arcade.color.FERN_GREEN)

    # Front Door
    arcade.draw_rectangle_filled(x + 155, x + 175, y - 110, y - 60, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x + 155, x + 175, y - 115, y - 65, arcade.color.SEASHELL)

    # Doorknob
    arcade.draw_circle_filled(x + 165, y + 50, 5, arcade.color.DIM_GRAY)


def draw_window(x, y):
    """Draw the windows"""

    # Left Window
    arcade.draw_rectangle_filled(x, 260, y, y + 10, arcade.color.FERN_GREEN)
    arcade.draw_rectangle_filled(x, 260, y - 10, y, arcade.color.SEASHELL)


def draw_tree(x, y):
    """Draw the trees"""

    # Triangle Top Tree
    arcade.draw_rectangle_filled(x, 180, y, y + 40, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(x, y + 460, x - 30, 210, x + 30, 210, arcade.csscolor.DARK_GREEN)


def draw_cloud(x, y):
    """Draw the clouds"""

    # Draw cloud
    arcade.draw_circle_filled(x, y, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x + 20, y + 10, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x, y + 20, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x - 20, y + 10, 30, arcade.csscolor.WHITE)


def main():

    # Set the background color
    arcade.set_background_color((38, 201, 255))

    # Get ready to draw
    arcade.start_render()

    # Draw the grass
    arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.FOREST_GREEN)

    # Draw a sun
    arcade.draw_circle_filled(700, 500, 80, (255, 244, 41))

    draw_house(25, 150)
    draw_window(90, 30)
    draw_window(260, 30)
    draw_tree(370, 20)
    draw_tree(450, 20)
    draw_tree(530, 20)
    draw_tree(620, 20)
    draw_cloud(200, 540)
    draw_cloud(350, 500)
    draw_cloud(65, 495)

    # Finish drawing and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
