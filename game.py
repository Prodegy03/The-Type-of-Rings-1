import arcade
from data_classes.game_data import game_data
from data_classes.level_data import level_data
from gameArchitecture.dataManager import data_manager
from gameArchitecture.level import level


class Game:
    def __init__(self):

        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600

        self.gameWindow = arcade.Window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.gameData: game_data = data_manager.load_game_data

        self.active_level: level = level(
            data_manager.level_dummy_data(), self.on_level_exit
        )
        self.active_level.setup()

        # arcade.set_background_color()
        self.gameWindow.show_view(self.active_level)

        arcade.run()

    # Use this to save data when a level closes.
    def on_level_exit(self, save_data: list):
        self.gameWindow.close()


game = Game()
