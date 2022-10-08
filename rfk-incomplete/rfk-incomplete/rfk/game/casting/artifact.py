from game.casting.actor import Actor
from game.shared.point import Point

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact (Actor):
    def set_text(self,text):
        self.test = text

    def set_font_size(self,FONT_SIZE):
        self.FONT_SIZE = FONT_SIZE

    def set_color(self,color):
        self.color = color
    
    def set_position(self,position):
        self.position = position
    
    def set_message(self,message):
        self.message = message

    def __init__(self):
        """Constructs a new artifact."""
        self._message = ""
        self._velocity = Point(0,1)
        """Inherits __init__ from the Actor class"""
        super (). __init__ ()