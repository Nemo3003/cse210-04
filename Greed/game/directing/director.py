from game.casting.stone import Stone
from game.shared.point import Point
from game.shared.color import Color
import random as r

WHITE = Color(255, 255, 255)

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        player = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)  

    def _do_updates(self, cast):
        gem = Stone()
        gem.set_text("$") #recommend $ or + or <> sign for the gem 💠\U0001F4A0
        gem.set_points(1)
        gem.set_velocity(Point(0,5))
        gem.set_position(Point(r.randint(15, 885),15))
        green = Color(0, 255, 0)
        gem.set_color(green)

        rock = Stone()
        rock.set_text("O") #recommend O or @ for the rock 🧱\U0001F9F1
        rock.set_points(-1)
        rock.set_velocity(Point(0,5))
        rock.set_position(Point(r.randint(15, 885),15))
        red = Color(255,0,0)
        rock.set_color(red)

        cast.add_actor("stones", gem)
        cast.add_actor("stones", rock)

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()

        player = cast.get_first_actor("player")
        player_x = player.get_position().get_x()
        player_y = player.get_position().get_y()
        score = cast.get_first_actor("score")
        for actor in cast.get_actors("stones"):
            actor.move_next(max_x, max_y)

            if actor.get_text() == "$": #recommend $ or + or <> sign for the gem  💠\U0001F4A0
                actor_x = actor.get_position().get_x()
                actor_y = actor.get_position().get_y()
                if ((player_x - 10 < actor_x < player_x + 10) and (player_y - 10 < actor_y < player_y + 10)):
                    score.add_points(1)
                if actor_y > max_y - 30 or((player_x - 10 < actor_x < player_x + 10) and (player_y - 10 < actor_y < player_y + 10)):
                    cast.remove_actor("stones", actor)
                    
            elif actor.get_text() == "O": #recommend O or @ for the rock 🧱\U0001F9F1
                actor_x = actor.get_position().get_x()
                actor_y = actor.get_position().get_y()
                if ((player_x - 10 < actor_x < player_x + 10) and (player_y - 10 < actor_y < player_y + 10)):
                    score.add_points(-1)
                if actor_y > max_y - 30 or ((player_x - 10 < actor_x < player_x + 10) and (player_y - 10 < actor_y < player_y + 10)):
                    cast.remove_actor("stones", actor)
        player.move_next(max_x, max_y)

        
    def _do_outputs(self, cast):
        self._video_service.clear_buffer()
        player = cast.get_first_actor("player")
        score = cast.get_first_actor("score")
        score.set_text(f"SCORE: {score.get_points()}")
        for actor in cast.get_actors("stones"):
            self._video_service.draw_actor(actor)
        self._video_service.draw_actor(player)
        self._video_service.draw_actor(score)
        self._video_service.flush_buffer()