from save_restore import save_galaxy, load_galaxy

class Galaxy:

    def __init__(self, name):
        self.name = name
        self.avg_speed = 0
        self.list_of_planets = set()
        self.number_of_planets = len(self.list_of_planets)

    def calculate_avg_speed(self):
        total_speed = 0
        for planet in self.list_of_planets:
            total_speed += planet.speed
        return  total_speed / len(self.list_of_planets)

    def planet_add(self, planet):
        self.list_of_planets.add(planet)
        planet.galaxy = self
        self.update_attrs()

    def planet_del(self, planet):
        self.list_of_planets.remove(planet)
        self.update_attrs()

    def update_avg_speed(self):
        self.avg_speed = self.calculate_avg_speed()

    def update_num_of_planet(self):
        self.number_of_planets = len(self.list_of_planets)

    def update_attrs(self):
        self.update_avg_speed()
        self.update_num_of_planet()


class Planet:

    def __init__(self, name, speed, galaxy=False):
        self.name =  name
        self.speed = speed # https://ru.wikipedia.org/wiki/Орбитальная_скорость
        self.galaxy = galaxy

        if self.galaxy:
            self.update_galaxy()

    def update_galaxy(self):
        self.galaxy.planet_add(self)
        self.galaxy.update_avg_speed()
        self.galaxy.update_num_of_planet()


mw = Galaxy("MilkyWay")

earth = Planet(galaxy=mw, name="Earth", speed=29.78)
mars = Planet(galaxy=mw, name="Mars", speed=24.13)
uranus = Planet(name="Uranus", speed = 6.81)

mw.planet_add(uranus)
mw.planet_del(mars)

file = 'gal.pickle'
save_galaxy(mw, file)


galaxy = load_galaxy(file)
print(galaxy.number_of_planets)

andromeda = Galaxy("Andromeda")
andromeda.planet_add(Planet(name="Planet1", speed=30, galaxy=andromeda))
andromeda.planet_add(Planet(name="Planet2", speed=40, galaxy=andromeda))
print(andromeda.avg_speed)

andr_file = "andr.pickle"
save_galaxy(andromeda, andr_file)
andromeda2 = load_galaxy(andr_file)
print(andromeda2.avg_speed, andromeda2.list_of_planets)
