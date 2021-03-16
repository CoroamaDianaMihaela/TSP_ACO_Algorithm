from random import randint


class Chromosome:

    def __init__(self,prblParam=None):
        # prblParam aici e number_of_cities
        self.__prblParam = prblParam
        self.__repres=[]

        self.__fitness = 0.0


    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=None):
        self.__repres = l

    @fitness.setter
    def fitness(self, fitness):
        self.__fitness = fitness

    def calculate_fitness(self, distance_each_city):
        sum = 0
        for i in range(0, self.__prblParam['noNodes'] - 1):
            sum += distance_each_city[self.__repres[i] - 1][self.__repres[i + 1] - 1]
        self.__fitness = sum

    def add_repres(self,node):
        self.__repres.append(node)

    def prblParam(self):
        return self.__prblParam

    def source_city(self):
        return self.__source_city

    def destination_city(self):
        return self.__dest_city

    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fitness: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
