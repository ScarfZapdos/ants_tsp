import random
import array
import numpy as np


_CITIES = [["Bordeaux", [44.833333,-0.566667]], ["Paris",[48.8566969,2.3514616]],["Nice",[43.7009358,7.2683912]], ["Arras",[50.283333,2.783333]],
["Lyon",[45.7578137,4.8320114]],["Nantes",[47.2186371,-1.5541362]],["Brest",[48.4,-4.483333]],["Lille",[50.633333,3.066667]], ["Nancy",[48.6937223,6.1834097]],
["C-F",[45.783333,3.083333]],["Strasbourg",[48.583333,7.75]],["Poitiers",[46.583333,0.333333]], ["Angouleme",[45.6512748,0.1576745]],
["Angers",[47.466667,-0.55]],["Montpellier",[43.6,3.883333]],["Caen",[49.183333,-0.35]],["Rennes",[48.083333,-1.683333]],["Pau",[43.3,-0.366667]]]

def distance(c1,c2):
    d = np.sqrt((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)
    return d

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Graph():
    RANDOMSEED = 12345
    ANT_NB = 10
    GAMMA = 0.2 # Paramètre de choix de piste jamais explorée / default 0.2
    ALPHA = 1 # Paramètre d'intensité de la piste / default 0.8
    BETA = 1.4 # Paramètre de visibilité de la ville / default 0.6
    Q = 1.25 # Paramètre de puissance des phéromones / default 1
    RHO = 0.9  # Evaporation des phéromones / default 0.9
    ITERATIONS = 50
    edges = None

    def __init__(self,seed=12345,ant_nb=10,g=0.2,a=0.8,b=0.6,q=1,rho=0.9):
        self.RANDOMSEED = seed
        self.ANT_NB = ant_nb
        self.GAMMA = g
        self.ALPHA = a
        self.BETA = b
        self.Q = q
        self.RHO = rho
        self.edges = {}
        for city1 in _CITIES:
            self.edges[city1[0]] = {}
            for city2 in _CITIES:
                if (city1==city2):
                    continue
                self.edges[city1[0]][city2[0]] = [0,distance(city1[1],city2[1])]

    def fade_pheromons(self):
        for city1 in self.edges:
            for city2 in self.edges[city1]:
                 self.edges[city1][city2][0] *= self.RHO

    def set_var(self,g=0.2,a=0.8,b=0.6,q=1,rho=0.9):
        self.GAMMA = g
        self.ALPHA = a
        self.BETA = b
        self.Q = q
        self.RHO = rho

    def set_iter(self,iter=50):
        self.ITERATIONS = iter

graph = Graph()

class Fourmi():
    path = []
    remaining = _CITIES.copy()
    final_dist = 0
    current_city = None

    def __init__(self):
        self.current_city = _CITIES[random.randint(0,len(_CITIES)-1)]
        self.path = []
        self.path.append(self.current_city)
        self.remaining = _CITIES.copy()
        self.remaining.remove(self.current_city)

    def probability(self,c1,c2):
        denom = graph.GAMMA + (graph.edges[c1][c2][0])**graph.ALPHA + (1/(graph.edges[c1][c2][1]))**graph.BETA
        num = 0
        for city in self.remaining:
            num += graph.GAMMA + (graph.edges[c1][city[0]][0])**graph.ALPHA + (1/(graph.edges[c1][city[0]][1]))**graph.BETA
        return (denom/num)

    def nextCity(self):
        probabs = {}
        for potcity in self.remaining:
            p = self.probability(self.current_city[0],potcity[0])
            probabs[potcity[0]] = p
        best_city = max(probabs, key=probabs.get)
        for city in _CITIES:
            if (city[0] == best_city):
                bc = city
        self.final_dist += distance(self.current_city[1],bc[1])
        self.remaining.remove(bc)
        self.path.append(bc)
        self.current_city = bc

    def find_path(self):
        while self.remaining:
            self.nextCity()
        #Leaves Pheromons
        old_city = self.path[0]
        self.final_dist += distance(self.path[0][1],self.path[-1][1])
        for city in (self.path[1:]):
            graph.edges[old_city[0]][city[0]][0] += graph.Q/self.final_dist
            old_city = city
        #print("")
        #print(f"{bcolors.WARNING}Chemin Fourmi :{bcolors.ENDC}")
        #self.print_path()

    def print_path(self):
        toret = ""
        old_city = self.path[0]
        toret += old_city[0]
        for city in self.path[1:]:
            toret += " --> " + city[0]
            old_city = city
        print(toret)
        print(f"{bcolors.WARNING}Final distance : {bcolors.ENDC}" + str(self.final_dist))



def main(write=False):
    #print("")
    best_distance = 50000
    best_path = []
    for k in range(graph.ITERATIONS):
        if not write:
            print(f"{bcolors.WARNING}Iteration {bcolors.ENDC}" + str(k+1) + "{bcolors.WARNING} :{bcolors.ENDC}")
            print(_CITIES)
        fourmi = Fourmi()
        fourmi.find_path()
        if (fourmi.final_dist<best_distance):
            best_distance=fourmi.final_dist
            best_it = k+1
            best_path = fourmi.path
            graph.fade_pheromons()
        if not write:
            print(f"{bcolors.WARNING}For now, the best distance is :{bcolors.ENDC}" + str(best_distance) + f"{bcolors.WARNING} km, found at iteration : {bcolors.ENDC}" + str(best_it) + f"{bcolors.WARNING}.{bcolors.ENDC}")
            print("")
    if not write:
        print(f"{bcolors.WARNING}The best path is : {bcolors.ENDC}")
    toret = f"{bcolors.FAIL}"
    old_city = best_path[0]
    toret += old_city[0]
    for city in best_path[1:]:
        toret += " --> " + city[0]
        old_city = city
    if not write:
        print(toret + f"{bcolors.ENDC}")
        print(f"{bcolors.WARNING}With a distance of : {bcolors.ENDC}" + str(best_distance))
        print("")
    if write:
        f = open("results_r.txt","a")
        #f.write("g={},a={},b={},q={},rho={},best_distance={},iterations={}\n".format(graph.GAMMA,graph.ALPHA,graph.BETA,graph.Q,graph.RHO,best_distance,best_it))
        f.write("r={},best_distance={},iterations={}\n".format(graph.RHO,best_distance,best_it))
    return best_path
