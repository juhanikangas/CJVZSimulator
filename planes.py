class Plane:
    def __init__(self, model, name, weight, speed, hp, exp):
        self.model = model
        self.name = name
        self.weight = weight
        self.speed = speed
        self.hp = hp
        self.exp = exp

    def str(self):
        return (f"{{'model': '{self.model}', 'name': '{self.name}',"
                f" weight': '{self.weight}', 'max_speed': '{self.speed}',"
                f" 'hp': '{self.hp}'}}")


def plane_options():
    plane1 = Plane("Cessna 172", "Skyhawk", 767, 196, 300, 0)
    plane2 = Plane("UltraGlide U-50", "Stingray", 3200, 450, 300, 500)
    plane3 = Plane("SwiftWing R-75", "Falcon", 7800, 850, 100, 900)
    plane4 = Plane("Concorde", "Concorde", 78700, 2180, 50, 1000)
    plane5 = Plane("Boeing 747", "Queen of the skies", 178000, 900, 200, 1000)
    plane6 = Plane("SpeedStar S-700", "Viper", 12000, 700, 400, 1200)
    plane7 = Plane("Lockheed SR-71", "Blackbird", 30617, 3529, 1, 2000)
    return [plane1, plane2, plane3, plane4, plane5, plane6, plane7]
