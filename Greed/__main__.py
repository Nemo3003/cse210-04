from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.score import Score

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point
import emoji

img = emoji.emojize(":smile:", use_aliases=True)

FRAME_RATE = 60
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 30
COLS = 60
ROWS = 40
CAPTION = img + "Greed"
WHITE = Color(255, 255, 255)
BLUE = Color(0, 0, 255)

def main():
    cast = Cast()
    x = int(MAX_X / 2)
    y = int(570)
    position = Point(x, y)

    player = Actor()
    player.set_text("(*^*)")
    player.set_font_size(FONT_SIZE)
    player.set_color(BLUE)
    player.set_position(position)
    cast.add_actor("player", player)
    # create intial score
    score = Score()
    score.set_position(Point(MAX_X // 2, 15))
    score.set_color(WHITE)
    cast.add_actor("score", score)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()