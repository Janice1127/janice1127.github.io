# Core libraries
import arcade as ac
import pathlib as pl
# Sprites
from sprites import map

# Where the program executes
class Main(ac.Window):
    def __init__(self):
        super().__init__(500, 500, "TCHS map")
        ac.set_background_color(ac.color.WHITE)
        # Variables
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        # map
        self.map = map()

    def on_update(self, delta_run):
        self.map.update()
        
    def update_player_speed(self):
        self.map.change_x = 0
        self.map.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.map.change_y = -5
        elif self.down_pressed and not self.up_pressed:
            self.map.change_y = 5
        if self.left_pressed and not self.right_pressed:
            self.map.change_x = 5
        elif self.right_pressed and not self.left_pressed:
            self.map.change_x = -5

    # def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
    #     self.button_press = True

    # def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
    #     self.button_press = False
    
    def on_key_release(self, key, modifiers):
        if key == ac.key.UP:
            self.up_pressed = False
            self.update_player_speed()
        elif key == ac.key.DOWN:
            self.down_pressed = False
            self.update_player_speed()
        elif key == ac.key.LEFT:
            self.left_pressed = False
            self.update_player_speed()
        elif key == ac.key.RIGHT:
            self.right_pressed = False
            self.update_player_speed()

    # def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
    #     if self.button_press:
    #         print(dx)
    #         if dx < 0:
    #             self.map.change_x = -5
    #         if dx > 0:
    #             self.map.change_x = 5
    #         if dy < 0:
    #             self.map.change_y = 5
    #         if dy > 0:
    #             self.map.change_y = -5
    #     else:
    #         self.map.change_x = 0
    #         self.map.change_y = 0
    
    def on_key_press(self, key: int, modifiers: int):
        if key == ac.key.UP:
            self.up_pressed = True
            self.update_player_speed()
        elif key == ac.key.DOWN:
            self.down_pressed = True
            self.update_player_speed()
        elif key == ac.key.LEFT:
            self.left_pressed = True
            self.update_player_speed()
        elif key == ac.key.RIGHT:
            self.right_pressed = True
            self.update_player_speed()
            
    def on_draw(self):
        self.clear()
        self.map.draw()

program = Main()
program.run()