# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting='Hello, <name>!'):
    other_greeting = greeting.replace('<name>', name)
    return other_greeting

def force(mass, body='earth'):
    planets = {
    'earth': 9.8,
    'mercury': 3.7,
    'venus': 8.9,
    'moon': 1.6,
    'mars': 3.7,
    'jupiter': 24.9,
    'saturn': 10.4,
    'uranus': 8.9,
    'neptune': 11.1,
    'pluto': 0.6,
    'sun': 274.0
    }
    if body not in planets:
        return f"Invalid planet name '{body}'"
    gravity = planets[body]
    force = mass * gravity
    return force


def pull(m1, m2, d):
    g = 6.674*(10**-11)
    f = g*((m1*m2)/(d**2))
    return f


print(force(0.1))
print(greet('Bob'))
print(pull(800,1500,3))

