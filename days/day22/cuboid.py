DIMENSIONS_COUNT = 3


class Cuboid:

    def __init__(self, coordinates: list):
        self.coordinates = coordinates

    def intersects(self, cuboid):
        for index, (min, max) in enumerate(self.coordinates):
            (to_remove_min, to_remove_max) = cuboid.coordinates[index]
            if max < to_remove_min:
                return False
            if min > to_remove_max:
                return False
        return True

    def remove(self, cuboid):  # return remaining space as cuboid
        result = []
        for index, (min, max) in enumerate(self.coordinates):
            (to_remove_min, to_remove_max) = cuboid.coordinates[index]
            if (min < to_remove_min):
                new_cuboid_coordinates = self.coordinates[0:index] + [[
                    min, to_remove_min - 1]] + self.coordinates[index+1:DIMENSIONS_COUNT]
                result.append(Cuboid(new_cuboid_coordinates))
            if (max > to_remove_max):
                new_cuboid_coordinates = self.coordinates[0:index] + [[
                    to_remove_max+1, max]] + self.coordinates[index+1:DIMENSIONS_COUNT]
                result.append(Cuboid(new_cuboid_coordinates))

        return result
