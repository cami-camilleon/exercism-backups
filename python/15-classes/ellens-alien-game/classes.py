"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    starting_health = 3
    total_aliens_created = 0

    def __init__(self, x_coord, y_coord):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.health = Alien.starting_health
        Alien.total_aliens_created = Alien.total_aliens_created + 1

    def hit(self):
        if self.health > 0:
            self.health = self.health - 1
    
    def is_alive(self):
        return self.health > 0
    
    def teleport(self, x_coord, y_coord):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord

    def collision_detection(self, object):
        pass
        


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(start_positions):
    alienlist = []
    for coords in start_positions:
        alienlist.append(Alien(coords[0], coords[1]))
    
    return alienlist

newalien = Alien(1, 2)

print(newalien.total_aliens_created)