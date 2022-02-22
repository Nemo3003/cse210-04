class Color:
    """A color.

    The responsibility of Color is to hold and provide information about itself. Color has a few 
    convenience methods for comparing them and converting to a tuple.

    Attributes:
        _red (int): The red value.
        _green (int): The green value.
        _blue (int): The blue value.
        _alpha (int): The alpha or opacity.
    """
    
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue 
        self.opacity = 255

    def to_tuple(self):
        return (self._red, self._green, self._blue, self.opacity) 