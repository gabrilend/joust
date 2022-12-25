import array

class Location:

    def __init__(self, name, description, actors, adjacentPlaces):
        self.name = name
        self.description = description
        self.actors = actors
        self.adjacentPlaces = adjacentPlaces