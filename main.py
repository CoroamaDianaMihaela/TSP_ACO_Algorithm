
"""
This is an ACO algorithm for determining the shortest path throughout all the nodes
"""
from Lab_5.Load_data import load_data_EDGES, load_data_TXT, load_data_TSP
from Lab_5.Utils import ACO


def run():
    name = "optimal_experiment.tsp"
    ## OPTIMAL VALUE: 1343
    # ar9152
    # "data_for_tsp_2.tsp"
    # aves - sparrow - social.edges
    # SFHH - conf - sensor
    delim = ' '
    # TODO: in functie de fiecare fisier pe care lucram trb sa schimb deliminatorul
    difference = 0
    if name[len(name) - 5:] == "edges":
        prblParam, distance_per_city, source_city, dest_city, difference = load_data_EDGES(name, delim)
    elif name[len(name) - 3:] == "txt":
        prblParam, distance_per_city, source_city, dest_city = load_data_TXT(name, delim)
    else:
        prblParam, distance_per_city, source_city, dest_city = load_data_TSP(name, delim)

    if difference != 0:
        ACO(prblParam, distance_per_city, difference)
    else:
        ACO(prblParam, distance_per_city)


run()
