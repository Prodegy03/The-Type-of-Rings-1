from xml.etree.ElementTree import tostring
import arcade


class entity(arcade.Sprite):
    eIdCounter: int = 0

    def __init__(self, filename: str, position: tuple[float, float]):
        super().__init__(filename=filename)

        self.eID: str = str(entity.eIdCounter)
        self.set_position(position[0], position[1])

        entity.eIdCounter += 1
