import random
import matplotlib.pyplot as plt
from numpy import array
import matplotlib

matplotlib.use('TkAgg')
vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
doubles_c = 'ltrnkm'
no_y = 'kfqvwxz'
star_classes = {
    'O': '#9aafff',  # голубой
    'B': '#cad7ff',  # бело-голубой
    'A': '#f8f7ff',  # белый
    'F': '#fff4ea',  # жёлто-белый
    'G': '#fff2a1',  # жёлтый
    'K': '#ffc46f',  # оранжевый
    'M': '#ff6060',  # красный
}
numbers = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX'
}


def russificate(word):
    word = word.lower()
    new_word = ''
    skip = False
    for i in range(0, len(word)):
        if skip:
            skip = False
            continue
        try:
            if word[i] + word[i + 1] == 'ph':
                new_word += 'ф'
                skip = True
                continue
            elif word[i] + word[i + 1] == 'th':
                new_word += 'з'
                skip = True
                continue
            elif word[i] + word[i + 1] == 'gh':
                new_word += 'г'
                skip = True
                continue
            elif word[i] + word[i + 1] == 'kh':
                new_word += 'х'
                skip = True
                continue
            elif word[i] + word[i + 1] == 'wu':
                new_word += 'ву'
                skip = True
                continue
            elif word[i] + word[i + 1] == 'oo':
                new_word += 'у'
                skip = True
                continue
            elif word[i] + word[i + 1] == 'ee':
                new_word += 'и'
                skip = True
                continue

        except IndexError:
            pass
        if word[i] == 'a':
            new_word += 'а'
        if word[i] == 'b':
            new_word += 'б'
        if word[i] == 'c':
            try:
                if word[i + 1] in 'eiy':
                    new_word += 'с'
                    continue
            except IndexError:
                pass
            new_word += 'к'
        if word[i] == 'd':
            new_word += 'д'
        if word[i] == 'e':
            new_word += 'и'
        if word[i] == 'f':
            new_word += 'ф'
        if word[i] == 'g':
            try:
                if word[i + 1] in vowels:
                    new_word += 'г'
                    continue
            except IndexError:
                new_word += 'г'
                continue
            new_word += 'ж'
        if word[i] == 'h':
            new_word += 'х'
        if word[i] == 'i':
            new_word += 'и'
        if word[i] == 'j':
            new_word += 'дж'
        if word[i] == 'k':
            new_word += 'к'
        if word[i] == 'l':
            new_word += 'л'
        if word[i] == 'm':
            new_word += 'м'
        if word[i] == 'n':
            new_word += 'н'
        if word[i] == 'o':
            new_word += 'о'
        if word[i] == 'p':
            new_word += 'п'
        if word[i] == 'q':
            new_word += 'к'
        if word[i] == 'r':
            new_word += 'р'
        if word[i] == 's':
            new_word += 'с'
        if word[i] == 't':
            new_word += 'т'
        if word[i] == 'u':
            new_word += 'у'
        if word[i] == 'v':
            new_word += 'в'
        if word[i] == 'w':
            new_word += 'у'
        if word[i] == 'x':
            new_word += 'кс'
        if word[i] == 'y':
            new_word += 'и'
        if word[i] == 'z':
            new_word += 'з'
        if word[i] == '-':
            new_word += '-'
    return new_word.capitalize()


def gen_rand_name():
    name = ''
    name += random.choice(vowels + consonants)
    length = random.randint(3, 8)
    for i in range(1, length + 1):

        if name[i - 1] in consonants:
            if name[i - 1] in 'ptgk':
                is_nex_h = random.randint(1, 10)
                if is_nex_h == 1:
                    name += 'h'
                    continue
            # Mostly u after q
            if name[i - 1] == 'q':
                is_nex_u = random.randint(1, 3)
                if is_nex_u < 3:
                    name += 'u'
                    continue

            # Double consonants
            if name[i - 1] in doubles_c:
                try:
                    if name[i - 2] == name[i - 1]:
                        name += random.choice(vowels)
                        continue
                except IndexError:
                    pass
                is_nex_double = random.randint(1, 10)
                if is_nex_double < 3:
                    name += name[i - 1]
                    continue

            # No Y after K F Q V W X Z
            if name[i - 1] in no_y and i != length:
                name += random.choice(vowels[:-1])
                continue

            name += random.choice(vowels)
        else:
            # Double vowels
            if name[i - 1] != 'y':
                try:
                    if name[i - 2] == name[i - 1]:
                        name += random.choice(consonants)
                        continue
                except IndexError:
                    pass
                is_nex_double = random.randint(1, 10)
                if is_nex_double < 2:
                    name += name[i - 1]
                    continue
            name += random.choice(consonants)
    return name.capitalize()


def calc_dist(a, b):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    dist_x = abs(x1 - x2)
    dist_y = abs(y1 - y2)
    dist = (dist_x ** 2 + dist_y ** 2) ** (1 / 2)
    return dist


class Star:
    id = 1
    neighbours = []

    def __repr__(self):
        return f'<Star {self.id} | {self.name}>'

    def __init__(self, stars):
        self.name = gen_rand_name()
        self.id = Star.id
        Star.id += 1
        double_name = random.randint(1, 3)
        if double_name == 1 and len(self.name) < 5:
            self.name += '-' + gen_rand_name()
        self.star_class = random.choice('OBAFGKM')
        self.color = star_classes[self.star_class]
        field = 500
        min_dist = 5
        self.coords = [random.randint(-field, field), random.randint(-field, field)]
        repeat = True
        while repeat:
            repeat = False
            for star in stars:
                x1 = abs(self.coords[0])
                x2 = abs(star.coords[0])
                y1 = abs(self.coords[1])
                y2 = abs(star.coords[1])
                if x2 > x1:
                    x1, x2 = x2, x1
                if y2 > y1:
                    y1, y2 = y2, y1
                while x1 - x2 < min_dist:
                    repeat = True
                    self.coords[0] = random.randint(-field, field)
                    x1 = abs(self.coords[0])
                    x2 = abs(star.coords[0])
                    if x2 > x1:
                        x1, x2 = x2, x1
                while y1 - y2 < min_dist:
                    repeat = True
                    self.coords[1] = random.randint(-field, field)
                    y1 = abs(self.coords[1])
                    y2 = abs(star.coords[1])
                    if y2 > y1:
                        y1, y2 = y2, y1

        self.planets = []

        if self.star_class == 'M':
            max_planets = 4
        else:
            many_planets = random.randint(0, 10)
            if many_planets > 7:
                max_planets = 9
            else:
                max_planets = 6
        planet_number = random.randint(0, max_planets)
        for i in range(1, planet_number + 1):
            self.planets.append(Planet(self.name, i))


class Planet:
    def __init__(self, star_name, number):
        self.name = star_name + '-' + numbers[number]


if __name__ == '__main__':
    stars = []
    for i in range(0, 50):
        stars.append(Star(stars))
    print(f'Generated {len(stars)} stars')
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#000000')
    i = 0
    for star in stars:
        neighbours = []
        for o_star in stars:
            if o_star == star:
                continue
            o_dist = calc_dist(star.coords, o_star.coords)
            if len(neighbours) < 10:
                neighbours.append(o_star)
            else:
                for index, neighbour in enumerate(neighbours):
                    neighbour_dist = calc_dist(star.coords, neighbour.coords)
                    if o_dist < neighbour_dist:
                        neighbours[index] = o_star
        star.neighbours = neighbours

    for star in stars:
        star.neighbours = list(dict.fromkeys(star.neighbours))
        for index, n in enumerate(star.neighbours):
            if star in n.neighbours:
                a = array([n.coords[0], star.coords[0]])
                b = array([n.coords[1], star.coords[1]])
                plt.plot(a, b, c='#A0FF80')
            else:
                star.neighbours.pop(index)

    for star in stars:
        i += 1
        rgb = array([255, 255 - i * 3, 255 - i * 3]) / 255
        plt.scatter(star.coords[0], star.coords[1], c=star.color)
        plt.text(star.coords[0] + 5, star.coords[1] - 5, star.name + ' [' + str(star.id) + ']', fontsize=6, c='#ffffff')
        print(f'{star.id}) {star.name} | {russificate(star.name)} | Type: {star.star_class}')
        for n in star.neighbours:
            print(f'    ({n.id}) {n.name}')
    plt.show()
