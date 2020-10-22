
import random
import arcade
import os

SPRITE_SCALING = 1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Load sound from Game Assets for CMSC 150
        self.football_collect_sound = arcade.load_sound("coin1.wav")

        # Set the working directory
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.player_list = None

        # Set up the player
        self.score = 0
        self.footballs_left = 35
        self.player_sprite = None

        self.football_list = None
        self.wall_list = None

        self.physics_engine = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.football_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.footballs_left = 35
        # Clip art image from pinterest.com
        self.player_sprite = arcade.Sprite("football-player.png", 0.2)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of walls
        for x in range(0, 1200, 64):
            for y in range(80, 1650, 150):
                # Randomly skip a box so the player can find a way through
                # Wall pattern image from kenny.nl
                if random.randrange(8) > 0:
                    wall = arcade.Sprite("platformPack_tile001.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
        # Outer wall image from kenny.nl
        for x in range(-60, 1300, 30):
            wall = arcade.Sprite("platformPack_tile040.png", 0.7)
            wall.center_x = x
            wall.center_y = 1650
            self.wall_list.append(wall)
        for y in range(-40, 1650, 30):
            wall = arcade.Sprite("platformPack_tile040.png", 0.7)
            wall.center_x = x
            wall.center_y = y
            self.wall_list.append(wall)
        for x in range(-60, 1300, 30):
            wall = arcade.Sprite("platformPack_tile040.png", 0.7)
            wall.center_x = x
            wall.center_y = -40
            self.wall_list.append(wall)
        for y in range(-40, 1650, 30):
            wall = arcade.Sprite("platformPack_tile040.png", 0.7)
            wall.center_x = -60
            wall.center_y = y
            self.wall_list.append(wall)

            # --- Manually place walls
            # Flag image from kenny.nl
            # Manually create and position a box at 300, 150
            wall = arcade.Sprite("flag_black.png", 2.5)
            wall.center_x = 300
            wall.center_y = 150
            self.wall_list.append(wall)

            # Manually create and position a box at 1000, 270
            wall = arcade.Sprite("flag_black.png", 2.5)
            wall.center_x = 1000
            wall.center_y = 310
            self.wall_list.append(wall)

            # Manually create and position a box at 100, 575
            wall = arcade.Sprite("flag_black.png", 2.5)
            wall.center_x = 100
            wall.center_y = 605
            self.wall_list.append(wall)

            # Manually create and position a box at
            wall = arcade.Sprite("flag_black.png", 2.5)
            wall.center_x = 1100
            wall.center_y = 910
            self.wall_list.append(wall)

        for i in range(35):
            football = arcade.Sprite("ball_football.png", 2)
            # Make sure footballs don't go on top of walls or other footballs
            done = False
            while not done:
                football.center_x = random.randrange(-10, 1100)
                football.center_y = random.randrange(-50, 1400)
                hit_list = arcade.check_for_collision_with_list(football, self.wall_list)
                football_hit_list = arcade.check_for_collision_with_list(football, self.football_list)
                if len(hit_list) == 0 and len(football_hit_list) == 0:
                    done = True

            self.football_list.append(football)

        # Set the background color
        arcade.set_background_color(arcade.color.BLEU_DE_FRANCE)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites
        self.wall_list.draw()
        self.player_list.draw()
        self.football_list.draw()

        # Put the text on the screen
        output = "Footballs Left: " + str(self.footballs_left)
        arcade.draw_text(output, self.view_left, self.view_bottom + 15, arcade.color.WHITE, 14)
        output = "Score: " + str(self.score)
        arcade.draw_text(output, self.view_left, self.view_bottom, arcade.color.WHITE, 14)

        # Game over when medals have been collected
        if len(self.football_list) == 0:
            arcade.draw_text("Game Over", 150, 500, arcade.color.WHITE, 125)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Game continues until footballs are all collected
        if len(self.football_list) > 0:

            # Generate a list of sprites that collided with the player.
            hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.football_list)

            # Loop through each colliding sprite, remove it, and add to the score.
            for football in hit_list:
                self.score += 1
                self.footballs_left -= 1
                arcade.play_sound(self.football_collect_sound)
                football.remove_from_sprite_lists()

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
