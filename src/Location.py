import array

class Location:

    def __init__(self, name, description, actors, adjacentPlaces):
        self.name = name
        self.description = description
        self.actors = actors
        self.adjacentPlaces = adjacentPlaces

    def move_to(self, actor):
        if actor not in self.actors:
            self.actors += actor
        actor.location = self
    
    def describe(self):
        pass

