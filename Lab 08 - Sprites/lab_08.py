import random
import arcade
import math

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Medal(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):

        """ Update the ball's position. """
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed


class Alien(arcade.Sprite):
    def update(self):
        self.center_y -= 1
        # See if we went off-screen
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):

        super().__init__(width, height)

        # Load the sounds from Game Assets for CMSC 150
        self.medal_collect_sound = arcade.load_sound("upgrade4.wav")
        self.alien_collide_sound = arcade.load_sound("lose5.wav")

        # Sprite lists
        self.player_list = None
        self.good_sprite_list = None
        self.bad_sprite_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None

    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.good_sprite_list = arcade.SpriteList()
        self.bad_sprite_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Craft speeder image from kenney.nl
        self.player_sprite = arcade.Sprite("craft_speederA_SE.png", SPRITE_SCALING / 2)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        for i in range(50):

            # Create the medal instance
            # Medal image from kenney.nl
            medal = Medal("flat_medal3.png", SPRITE_SCALING / 3)

            # Position the center of the circle the medal will orbit
            medal.circle_center_x = random.randrange(SCREEN_WIDTH)
            medal.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            medal.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            medal.circle_angle = random.random() * 2 * math.pi

            # Add the medal to the lists
            self.good_sprite_list.append(medal)

        for i in range(50):
            # Create the alien ship instance
            # Alien ship image from kenney.nl
            alien_ship = Alien("shipBlue_manned.png", SPRITE_SCALING / 3)

            # Position the alien ship
            alien_ship.center_x = random.randrange(SCREEN_WIDTH)
            alien_ship.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the alien ship to the lists
            self.bad_sprite_list.append(alien_ship)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()

        # Draw all the sprites.
        self.good_sprite_list.draw()
        self.player_list.draw()
        self.bad_sprite_list.draw()

        # Put the text on the screen.
        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        # Game over when medals have been collected
        if len(self.good_sprite_list) == 0:
            arcade.draw_text("Game Over", 50, 400, arcade.color.WHITE, 125)

    def on_mouse_motion(self, x, y, dx, dy):

        if len(self.good_sprite_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.good_sprite_list.update()

        # Game continues until medals are all collected
        if len(self.good_sprite_list) > 0:
            self.bad_sprite_list.update()

            # Generate a list of good sprites that collided with the player.
            hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)

            # Loop through each colliding sprite, remove it, and add to the score.
            for medal in hit_list:
                self.score += 1
                arcade.play_sound(self.medal_collect_sound)
                medal.remove_from_sprite_lists()

            # Generate a list of bad sprites that collided with the player
            hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite_list)

            for alien_ship in hit_list:
                self.score -= 1
                arcade.play_sound(self.alien_collide_sound)
                alien_ship.remove_from_sprite_lists()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()
