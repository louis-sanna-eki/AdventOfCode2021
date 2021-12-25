DIMENSIONS_COUNT = 3


class Cuboid:

    def __init__(self, coordinates: list):
        self.coordinates = coordinates

    def intersects(self, cuboid) -> bool:
        for index, (min, max) in enumerate(self.coordinates):
            (to_remove_min, to_remove_max) = cuboid.coordinates[index]
            if max < to_remove_min:
                return False
            if min > to_remove_max:
                return False
        return True

    # return remaining space as cuboid
    def remove(self, cuboid) -> list:
        result = []
        for index, [self_min, self_max] in enumerate(self.coordinates):
            (to_remove_min, to_remove_max) = cuboid.coordinates[index]
            if (self_min < to_remove_min):
                new_cuboid_coordinates = self.coordinates[0:index] + [[
                    self_min, to_remove_min - 1]] + self.coordinates[index+1:DIMENSIONS_COUNT]
                result.append(Cuboid(new_cuboid_coordinates))
            if (self_max > to_remove_max):
                new_cuboid_coordinates = self.coordinates[0:index] + [[
                    to_remove_max+1, self_max]] + self.coordinates[index+1:DIMENSIONS_COUNT]
                result.append(Cuboid(new_cuboid_coordinates))
            if (self_max > to_remove_max) or (self_min < to_remove_min):
                remaining_cuboid_coordinates = self.coordinates[0:index] + [[
                    max(self_min, to_remove_min), min(self_max, to_remove_max)]] + self.coordinates[index+1:DIMENSIONS_COUNT]
                remaining_cuboid = Cuboid(remaining_cuboid_coordinates)
                result.extend(remaining_cuboid.remove(cuboid))
                break
        return result

    def volume(self) -> int:
        result = 1
        for [self_min, self_max] in self.coordinates:
            result *= self_max - self_min + 1
        return result
