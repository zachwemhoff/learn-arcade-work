"""
Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

CHARACTER_SCALING = 0.5

PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        self.player_sprite = None

        self.physics_engine = None

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        image_source = "character.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        map_name = "test_map.tmx"
        platform_layer_name = "Walls"
        coin_layer_name = "Coins"

        my_map = arcade.tilemap.read_tmx(map_name)
        self.wall_list = arcade.tilemap.process_layer(my_map,
                                                      platform_layer_name,
                                                      0.5)

        self.coin_list = arcade.tilemap.process_layer(my_map, coin_layer_name,
                                                      0.5)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)

        # Create Ground
        for x in range(0, 1250, 64):
            wall = arcade.Sprite("boxCrate_double.png", 0.5)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        wall = arcade.Sprite("boxCrate_double.png", 0.5)
        wall.center_x = 512
        wall.center_y = 300
        wall.angle = 45
        self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        # Code to draw the screen goes here
        self.player_list.draw()
        self.wall_list.draw()
        self.coin_list.draw()

    def on_update(self, delta_time):
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = 30

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
