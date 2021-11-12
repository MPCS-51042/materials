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
            if color ==  "black":
                return "Red-Shouldered Blackbird"
            if color == "red":
                return "Serrano (Field Museum's Scarlet Maccaw)"
            if color == "green":
                return "Pablo (Field Museum's Greenwing Maccaw)"
            if color == "grey":
                return "Seagull"
        else:
            if color == "brown":
                return "juvenile Bald Eagle"
            if color == "grey":
                return "Eastern Heron"
            if color == "black":
                return "Raven"


