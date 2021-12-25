
class Cuboid:

    def __init__(self, coordinates: tuple):
        self.coordinates = coordinates

    def intersects(self, cuboid):
        for index, (min, max) in enumerate(self.coordinates):
            (outside_min, outside_max) = cuboid.coordinates[index]
            if max < outside_min:
                return False
            if min > outside_max:
                return False
        return True
