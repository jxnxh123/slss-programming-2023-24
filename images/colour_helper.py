# colour helper
# author: Jonah
# date: december 19, 2023

def is_light(pixel: tuple) -> bool:
    """Returns true if given pixel is "light"

    Params:
        pixel - 3-tuple of values red, green, blue

    Returns:
        True if pixel is light false if not
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = (red + green + blue) / 3

    if average >= 128:
        return True
    else:
        return False
8:44
def is_light(pixel: tuple) -> bool:
    """Returns true if given pixel is "light"

    Params:
        pixel - 3-tuple of values red, green, blue

    Returns:
        True if pixel is light false if not
    """
    return pixel >= (128, 128, 128)