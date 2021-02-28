from collections import namedtuple

Observation = namedtuple("Observation", "color location_seen")

class BirdWatchingSession():
    def __init__(self):
        self.birds_seen = 0
        self.classifications = []

    def record(self, *observations):
        self.classifications.append([self.classify(observation.color, observation.location_seen) for observation in observations])
        birds_seen = self.birds_seen + len(observations)

    def classify(self, color, location_seen):
        # It's a peninsula bird if it was seen on Solidarity Drive
        peninsula_bird = location_seen = "Solidarity Drive"
        if peninsula_bird:
            if color is "black":
                return "Red-Shouldered Blackbird"
            if color is "red":
                return "Serrano (Field Museum's Scarlet Maccaw)"
            if color is "green":
                return "Pablo (Field Museum's Greenwing Maccaw)"
            if color is "grey":
                return "Seagull"
        else:
            if color is "brown":
                return "juvenile Bald Eagle"
            if color is "grey":
                return "Eastern Heron"
            if color is "black":
                return "Raven"

session = BirdWatchingSession()
session.record(Observation('black', 'Solidarity Drive'))
session.record(Observation('black', 'Clark Park'))
session.record(Observation('grey', 'Solidarity Drive'))
session.record(Observation('red', 'Solidarity Drive'))
session.record(Observation('brown', 'Starved Rock State Park'))
session.record(Observation('grey', 'Chicago River'))
print(session.birds_seen)
print(session.classifications)


