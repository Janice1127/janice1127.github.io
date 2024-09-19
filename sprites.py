import arcade as ac
import pathlib as pl

class Map(ac.Sprite):
    def __init__(self):
        super().__init__(
            str(pl.Path().parent) + "/tchsmap.png", 
            5,
            center_x=ac.get_display_size()[0] / 2,
            center_y=ac.get_display_size()[1] / 2
        )

    def update(self):
        super().update()