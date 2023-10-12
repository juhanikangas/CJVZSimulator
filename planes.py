
class Plane:
    def __init__(self, model, name, weight, speed, hp):
        self.model = model
        self.name = name
        self.weight = weight
        self.speed = speed
        self.hp = hp

    def __str__(self):
        return (f"{{'model': '{self.model}', 'name': '{self.name}',"
                f" weight': '{self.weight}', 'max_speed': '{self.speed}',"
                f" 'hp': '{self.hp}'}}")


def plane_options():
    plane1 = Plane("Boeing 747", "Queen of the skies", 178000, 900, 200)
    plane2 = Plane("Lockheed SR-71", "Blackbird", 30617, 3529, 50)
    plane3 = Plane("Cessna 172", "Skyhawk", 767, 196, 150)
    plane4 = Plane("Concorde", "Concorde", 78700, 2180, 100)
    return [plane1, plane2, plane3, plane4]
