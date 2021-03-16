import math

def load_data_TXT(fileName, delim):
    f = open(fileName, "r")
    number_cities = int(f.readline())
    print(number_cities)
    distance_per_city = [[0] for _ in range(0, number_cities)]
    for _ in range(0, number_cities):
        numbers = f.readline()
        numbers = numbers.split(delim)
        distance_per_city[_] = []
        for number in numbers:
            distance_per_city[_].append(float(number))

    source_city = f.readline()
    if source_city != '':
        source_city = int(source_city)
    else:
        source_city = number_cities
    dest_city = f.readline()
    if dest_city != '':
        dest_city = int(dest_city)
    else:
        dest_city = 1
    f.close()
    prblParam = {'noNodes': number_cities}
    return prblParam, distance_per_city, source_city, dest_city


def calculate_distances(coordinates, number_cities):
    distance_each_city = [[] for _ in range(0, number_cities)]
    for v in range(0, len(coordinates)):
        for v_2 in range(0, len(coordinates)):
            if v != v_2:
                x = (coordinates[v][0] - coordinates[v_2][0]) ** 2
                y = (coordinates[v][1] - coordinates[v_2][1]) ** 2
                distance_each_city[v].append(math.sqrt(x + y))
            else:
                distance_each_city[v].append(0)

    return distance_each_city


def load_data_TSP(fileName, delim):
    f = open(fileName, 'r')
    buffer = f.readline()
    while buffer != 'NODE_COORD_SECTION\n':
        buffer = f.readline()
    coordinates = []
    nr_c = 0
    ok = 1
    pos = 0
    while ok:
        pos += 1
        coordinate = f.readline()
        if coordinate == 'EOF' or coordinate == 'EOF\n':
            nr_c = int(len(coordinates))
            ok = 1
            break
        else:
            coordinate = coordinate.split(delim)
            coordinates.append((float(coordinate[1]), float(coordinate[2])))

    number_cities = nr_c
    source_city = number_cities
    dest_city = 1
    distance_per_city = calculate_distances(coordinates, number_cities)
    f.close()
    prblParam = {'noNodes': number_cities}
    return prblParam, distance_per_city, source_city, dest_city


def load_data_EDGES(fileName, delim):
    f = open(fileName, "r")
    lines = []
    numbers = f.readline()
    cities = []
    maximum = 0
    minimum = 9999
    while numbers != '':
        lines.append(numbers)
        line = numbers.split(delim)
        for l in line[:2]:
            if int(l) not in cities:
                cities.append(int(l))
                if maximum < int(l):
                    maximum = int(l)
                if minimum > int(l):
                    minimum = int(l)
        # p1 = int(numbers[0])
        # p2 = int(numbers[1])
        # distance_per_city[p1][p2] = int(numbers[3])
        numbers = f.readline()

    number_cities = len(cities)
    print(number_cities)
    difference = maximum - minimum + 1

    distance_per_city = [[0 for __ in range(0, difference)] for _ in range(0, difference)]

    for _ in range(0, len(lines)):
        number = lines[_]
        number = number.split(delim)
        # if minimum!=1:
        #     minimum-=1
        p1 = int(number[0]) - minimum
        p2 = int(number[1]) - minimum
        # TODO: asta nu merge pt ca nu poti avea matrice[143][1222] pt chiar daca ai 400 de orase ai un oras 1222 la
        #  care tehnic nu se ajunge
        distance_per_city[p1][p2] = float(number[2])
        distance_per_city[p2][p1] = float(number[2])

    source_city = f.readline()
    if source_city != '':
        source_city = int(source_city)
    else:
        source_city = maximum
    dest_city = f.readline()
    if dest_city != '':
        dest_city = int(dest_city)
    else:
        dest_city = minimum
    f.close()
    prblParam = {'noNodes': number_cities}
    if difference == number_cities:
        difference = 0
    return prblParam, distance_per_city, source_city, dest_city, difference
