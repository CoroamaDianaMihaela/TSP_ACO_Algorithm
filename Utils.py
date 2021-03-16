import random
import math
import pyprind
import sys
from tqdm import tqdm
import time

from Chromosome import Chromosome


def calculate_decision(probability_edges):
    """
    This function determines the decision that is made

    :param probability_edges: the probability that the ant takes a certain edge
    :return: decision: an int , the position in which the next node is in
    """
    prob = []
    # probability_edges = sorted(probability_edges, key=lambda x: x, reverse=True)
    # neighbour_nodes=sorted(neighbour_nodes,key=lambda)
    for _ in range(0, len(probability_edges)):
        sum = 0
        for __ in range(_, len(probability_edges)):
            sum += probability_edges[__]
        prob.append(sum)
    r = random.uniform(0, 1)
    if len(prob) == 1:
        return 0
    for _ in range(0, len(prob) - 1):
        if prob[_] >= r > prob[_ + 1]:
            return _
        elif _ == len(prob) - 2:
            return _ + 1


def calculate_probability(pheromone_matrix, cost_matrix, pos, chr):
    """
    This function adds the next node to the path of the Chromosome using mathematical probability
    :param pheromone_matrix: matrix
    :param cost_matrix: matrix
    :param pos: int
    :param chr: Chromosome
    :return:
    """
    neighbour_pos = []
    probabiliy_edges = []
    und = 0
    for _ in range(0, len(cost_matrix[0])):
        if cost_matrix[pos][_] != 0 and _ + 1 not in chr.repres:
            neighbour_pos.append(_)
            und += pheromone_matrix[pos][_] * (1 / cost_matrix[pos][_])
    if len(neighbour_pos) == 0:
        print('')
        return chr.repres.pop()
    neighbour_pos = sorted(neighbour_pos, key=lambda x: cost_matrix[pos][x], reverse=False)
    for _ in neighbour_pos:
        P = pheromone_matrix[pos][_] * (1 / cost_matrix[pos][_])
        P /= und
        probabiliy_edges.append(P)
    decision = calculate_decision(probabiliy_edges)
    # pheromone_matrix[pos][neighbour_pos[decision]]
    chr.add_repres(neighbour_pos[decision] + 1)
    return 1


def repeat(chr):
    """
    This function verifies that there aren't duplicates in the Chromosome
    :param chr: Chromosome
    :return: None
    """
    for _ in chr.repres:
        nr = 0
        for __ in chr.repres:
            if _ == __:
                nr += 1
        if nr != 1:
            print(_)


def ACO(prblParam, cost_matrix, difference=0):
    """
    the algorithm that determines the shortest path
    :param prblParam: dictionary
    :param cost_matrix: matrix
    :param difference: int
    :return:
    """
    if difference != 0:
        pheromone_matrix = [[1 for _ in range(0, difference)] for __ in range(0, difference)]
        nrs = difference
    else:
        pheromone_matrix = [[1 for _ in range(0, prblParam['noNodes'])] for __ in range(0, prblParam['noNodes'])]
        nrs = prblParam['noNodes']
    for _ in range(0, nrs):
        pheromone_matrix[_][_] = 0
    for ant in tqdm(range(1000)):
        chr = Chromosome(prblParam)
        pos = 0
        chr.add_repres(1)
        length = 1
        while length != nrs:
            # TODO: aici nu merge daca folosim .edges pt ca mereu raman noduri in urma problema
            #  asta nu apare la fisierele de tip .TSP

            pop = calculate_probability(pheromone_matrix, cost_matrix, pos, chr)
            pos = chr.repres[len(chr.repres) - 1] - 1
            if pop == 1:
                length += 1
            else:
                length -= 1
        repeat(chr)
        chr.calculate_fitness(cost_matrix)
        time.sleep(0.5)
        L = 1 / chr.fitness
        L=L*100000
        for _ in range(0, len(chr.repres) - 1):
            pheromone_matrix[chr.repres[_] - 1][chr.repres[_ + 1] - 1] += L
        if ant==0 or ant==50:
            print(chr)

    print(chr)
    print('If you want to start from an city like 153 you need to add the difference, '
          'so just go through the last chromosome with a for and add it')
