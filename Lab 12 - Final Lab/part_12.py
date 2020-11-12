"""
Sprite with Moving Platforms

"""
# Some beginning code from arcade.academy, Moving Platforms
# Other code adapted from previous labs and arcade.academy
import arcade
import os
import random

SPRITE_SCALING = 1.0

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
COIN_COUNT = 10
SCREEN_TITLE = "Final Lab: Collecting Coins and Avoiding Enemies Game"
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALING)
TILE_SCALING = 0.5
CHARACTER_SCALING = TILE_SCALING * 2

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = SPRITE_PIXEL_SIZE * SPRITE_SCALING
RIGHT_MARGIN = 4 * SPRITE_PIXEL_SIZE * SPRITE_SCALING

# Physics
MOVEMENT_SPEED = 10 * SPRITE_SCALING
JUMP_SPEED = 28 * SPRITE_SCALING
GRAVITY = .9 * SPRITE_SCALING

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]


class PlayerCharacter(arcade.Sprite):
    """ Player Sprite"""
    def __init__(self):

        # Set up parent class
        super().__init__()

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING

        # Track our state
        self.jumping = False
        self.climbing = False

        # --- Load Textures ---
        # Image From kenny.nl
        main_path = "adventurer"

        # Load textures for idle standing
        self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")
        self.jump_texture_pair = load_texture_pair(f"{main_path}_jump.png")
        self.fall_texture_pair = load_texture_pair(f"{main_path}_fall.png")

        # Load textures for walking
        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{main_path}_walk1.png")
            self.walk_textures.append(texture)

        # Set the initial texture
        self.texture = self.idle_texture_pair[0]

    def update_animation(self, delta_time: float = 1/60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Jumping animation
        if self.change_y > 0:
            self.texture = self.jump_texture_pair[self.character_face_direction]
            return
        elif self.change_y < 0:
            self.texture = self.fall_texture_pair[self.character_face_direction]
            return

        # Idle animation
        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture][self.character_face_direction]


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.all_sprites_list = None
        self.all_wall_list = None
        self.static_wall_list = None
        self.moving_wall_list = None
        self.player_list = None
        self.coin_list = None
        self.flag_list = None

        # Set up the player
        self.score = 0
        self.coins_left = 10
        self.player_sprite = None
        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0
        self.end_of_map = 0
        self.game_over = False

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_wall_list = arcade.SpriteList()
        self.static_wall_list = arcade.SpriteList()
        self.moving_wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.flag_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.coins_left = 10
        self.player_sprite = PlayerCharacter()
        self.player_sprite.center_x = 2 * GRID_PIXEL_SIZE
        self.player_sprite.center_y = 3 * GRID_PIXEL_SIZE
        self.player_list.append(self.player_sprite)

        # Create floor
        # Image from kenny.nl: kenny_simplifiedplatformer.zip
        for i in range(30):
            wall = arcade.Sprite("platformPack_tile001.png", 2)
            wall.bottom = 0
            wall.center_x = i * GRID_PIXEL_SIZE
            self.static_wall_list.append(wall)
            self.all_wall_list.append(wall)

        # Create platform side to side
        # Image from kenny.nl: kenny_simplifiedplatformer.zip
        wall = arcade.Sprite("platformPack_tile001.png", SPRITE_SCALING)
        wall.center_y = 3 * GRID_PIXEL_SIZE
        wall.center_x = 3 * GRID_PIXEL_SIZE
        wall.boundary_left = 2 * GRID_PIXEL_SIZE
        wall.boundary_right = 5 * GRID_PIXEL_SIZE
        wall.change_x = 2 * SPRITE_SCALING

        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)

        # Create platform side to side
        # Image from kenny.nl: kenny_simplifiedplatformer.zip
        wall = arcade.Sprite("platformPack_tile001.png", SPRITE_SCALING)
        wall.center_y = 3 * GRID_PIXEL_SIZE
        wall.center_x = 7 * GRID_PIXEL_SIZE
        wall.boundary_left = 5 * GRID_PIXEL_SIZE
        wall.boundary_right = 9 * GRID_PIXEL_SIZE
        wall.change_x = -2 * SPRITE_SCALING

        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)

        # Create platform side to side
        # Image from kenny.nl: kenny_simplifiedplatformer.zip
        wall = arcade.Sprite("platformPack_tile001.png", SPRITE_SCALING)
        wall.center_y = 4 * GRID_PIXEL_SIZE
        wall.center_x = 1500
        wall.boundary_left = 1100
        wall.boundary_right = 1400
        wall.change_x = -2 * SPRITE_SCALING

        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)

        # Create platform moving up and down
        # Image from kenny.nl: kenny_simplifiedplatformer.zip
        wall = arcade.Sprite("platformPack_tile001.png", SPRITE_SCALING)
        wall.center_y = 5 * GRID_PIXEL_SIZE
        wall.center_x = 5 * GRID_PIXEL_SIZE
        wall.boundary_top = 8 * GRID_PIXEL_SIZE
        wall.boundary_bottom = 4 * GRID_PIXEL_SIZE
        wall.change_y = 2 * SPRITE_SCALING

        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)

        # Create platform moving up and down
        # Image from kenny.nl: kenny_simplifiedplatformer.zip
        wall = arcade.Sprite("platformPack_tile001.png", SPRITE_SCALING)
        wall.center_y = 5 * GRID_PIXEL_SIZE
        wall.center_x = 2200
        wall.boundary_top = 550
        wall.boundary_bottom = 350
        wall.change_y = 2 * SPRITE_SCALING

        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)

        # Add Platforms for player to jump on
        # Image from kenny.nl: kenny_simplifiedplatformer.zip
        # Place boxes inside a loop
        for x in range(1500, 2000, 64):
            wall = arcade.Sprite("platformPack_tile001.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 350
            self.all_wall_list.append(wall)
        for x in range(2750, 3225, 64):
            wall = arcade.Sprite("platformPack_tile001.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 375
            self.all_wall_list.append(wall)

        # Outer wall image from kenny.nl
        # from kenny_simplifiedplatformer.zip
        for x in range(-60, 1300, 30):
            wall = arcade.Sprite("platformPack_tile040.png", 1.0)
            wall.center_x = x
            wall.center_y = 1650
            self.static_wall_list.append(wall)
            self.all_wall_list.append(wall)
        for y in range(0, 375, 30):
            wall = arcade.Sprite("platformPack_tile040.png", 1.0)
            wall.center_x = 3755
            wall.center_y = y
            self.static_wall_list.append(wall)
            self.all_wall_list.append(wall)
        for y in range(550, 1650, 30):
            wall = arcade.Sprite("platformPack_tile040.png", 1.0)
            wall.center_x = 3755
            wall.center_y = y
            self.static_wall_list.append(wall)
            self.all_wall_list.append(wall)
        for y in range(0, 1650, 30):
            wall = arcade.Sprite("platformPack_tile040.png", 1.0)
            wall.center_x = -60
            wall.center_y = y
            self.static_wall_list.append(wall)
            self.all_wall_list.append(wall)

        # Place Coins
        # Coin image from kenny.nl
        for i in range(COIN_COUNT):
            coin = arcade.Sprite("coin_01.png", .3)

            # Position the coin
            coin.center_x = random.randrange(50, 3700)
            coin.center_y = random.randrange(150, 650)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Place Flags
        # Flag from kenny_platformerkit2, kenny.nl
        flag = arcade.Sprite("flag_NW.png", .7)
        # Position the flag
        flag.center_x = 3750
        flag.center_y = 440
        # Add the flag to the list
        self.flag_list.append(flag)

        self.physics_engine = \
            arcade.PhysicsEnginePlatformer(self.player_sprite,
                                           self.all_wall_list,
                                           gravity_constant=GRAVITY)

        # Set the background color
        arcade.set_background_color(arcade.color.BLUEBERRY)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

        self.game_over = False

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the sprites.
        self.static_wall_list.draw()
        self.moving_wall_list.draw()
        self.all_wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        self.flag_list.draw()

        # Put the score on the screen.
        output = "Coins Left: " + str(self.coins_left)
        arcade.draw_text(output, self.view_left, self.view_bottom + 15, arcade.color.WHITE, 14)
        output = "Score: " + str(self.score)
        arcade.draw_text(output, self.view_left, self.view_bottom, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()
        self.coin_list.update()

        # Update animations
        if self.physics_engine.can_jump():
            self.player_sprite.can_jump = False
        else:
            self.player_sprite.can_jump = True

        self.player_list.update_animation(delta_time)

        # Update Coin List
        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            self.score += 1
            self.coins_left -= 1
            coin.remove_from_sprite_lists()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN
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

        # If we need to scroll, go ahead and do it.
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

