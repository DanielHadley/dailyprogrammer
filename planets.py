# http://www.reddit.com/r/dailyprogrammer/comments/284mep/6142014_challenge_166b_easy_planetary_gravity/
"""Planetary Gravity Calculator"""
from math import pi

# http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array
content = [line.strip() for line in open('planets')]

G = 6.67e-11 # Gravitational constant

M = int(content[0]) # Mass of the object


class Planet(object):
    name = ""
    radius = 0
    density = 0  # in kilograms per cubic metre

    def __init__(self, name, radius, density):
        super(Planet, self).__init__()
        self.name = name
        self.radius = radius
        self.density = density
        self.volume = 4.0/3 * pi * self.radius**3
        self.mass = self.volume * self.density
        self.newtons = G * (((M * self.mass)) / (self.radius)**2)


for planet in content[2:]:
    details = planet.strip().split(',')
    plnt = Planet(details[0], int(details[1]), int(details[2]))
    print("{} : {} Newtons".format(plnt.name, round(plnt.newtons, 3))) 



