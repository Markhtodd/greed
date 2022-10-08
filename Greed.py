import random
import os
from shared.color import Color
from shared.point import Point

class game:
    FRAME_RATE = 12
    MAX_X = 900
    MAX_Y = 600
    CELL_SIZE = 15
    FONT_SIZE = 15
    COLS = 60
    ROWS = 40
    CAPTION = "Greed"
    DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
    WHITE = Color(255, 255, 255)
    DEFAULT_ARTIFACTS = 40
    score = 0
    
    def __init__(self) -> None:
        # create the robot
        x = int(self.MAX_X / 2)
        y = int(self.MAX_Y / 2)
        position = Point(x, y)


    def create_screen(self):
        pass

    def start(self):
        while True:
            pass
