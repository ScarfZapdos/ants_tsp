import pygame
import fourmis
import time

width = 600
height = 700

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

def min_hw(cities,i):
    min = 10000
    for c in cities:
        if c[1][i] < min:
            min = c[1][i]
    return min

def max_hw(cities,i):
    max = 0
    for c in cities:
        if c[1][i] > max:
            max = c[1][i]
    return max

minw = min_hw(fourmis._CITIES,1)
minh = min_hw(fourmis._CITIES,0)
maxh = max_hw(fourmis._CITIES,0)
maxw = max_hw(fourmis._CITIES,1)

def normalize_coord(y,x):
    new_x = ((x-minw)/(maxw - minw))*(width-40)+20
    new_y = height-(((y-minh)/(maxh - minh))*(height-40)+20)
    return(new_x,new_y)

def find_coord(c):
    for city in fourmis._CITIES:
        if c == city[0]:
            return (city[1][0],city[1][1])
    return None

def main():
    ''' Initialization '''
    pygame.init()
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Ants TSP')
    best_distance = 50000
    best_path = []
    clock = pygame.time.Clock()
    white = (240, 240, 240)
    purple = (100, 0, 100)
    orange = (255, 129, 0)
    background = (41,70,91)
    font = pygame.font.SysFont("Times New Roman", 25)
    font2 = pygame.font.SysFont("Times New Roman", 19)
    title = font.render("Ants TSP in France Cities", True, white)
    caption1 = font.render("Purple for best path so far", True, purple)
    caption2 = font.render("Orange for pheromons", True, orange)

    for k in range(fourmis.graph.ITERATIONS):
        print(f"{bcolors.WARNING}Iteration {bcolors.ENDC}" + str(k+1) + f"{bcolors.WARNING} :{bcolors.ENDC}")
        display.fill(background)
        fourmi = fourmis.Fourmi()
        fourmi.find_path()
        if (fourmi.final_dist<best_distance):
            best_distance = fourmi.final_dist
            best_it = k+1
            best_path = fourmi.path
    # DRAWING LOOP
        display.blit(title,(10,10))
        display.blit(caption1,(10,50))
        display.blit(caption2,(10,90))

        for i in range(len(best_path)-1):
            pygame.draw.line(display, purple, normalize_coord(best_path[i][1][0], best_path[i][1][1]), normalize_coord(best_path[i+1][1][0], best_path[i+1][1][1]), 12)
        pygame.draw.line(display, purple, normalize_coord(best_path[-1][1][0], best_path[-1][1][1]), normalize_coord(best_path[0][1][0], best_path[0][1][1]), 12)

        for c1 in fourmis.graph.edges:
            for c2 in fourmis.graph.edges[c1]:
                x1,y1 = find_coord(c1)
                x2,y2 = find_coord(c2)
                if fourmis.graph.edges[c1][c2][0] > 0:
                    pygame.draw.line(display, orange, normalize_coord(x1,y1), normalize_coord(x2,y2), int(fourmis.graph.edges[c1][c2][0]*30))

        for i in range(len(fourmis._CITIES)):
            pygame.draw.circle(display, white, normalize_coord(best_path[i][1][0], best_path[i][1][1]),6)
        pygame.display.update()
        clock.tick(600)
        #END OF DRAWING LOOP
        fourmis.graph.fade_pheromons()
        print(f"{bcolors.WARNING}For now, the best distance is :{bcolors.ENDC}" + str(best_distance) + f"{bcolors.WARNING} km, found at iteration : {bcolors.ENDC}" + str(best_it) + f"{bcolors.WARNING}.{bcolors.ENDC}")
        print("")
        time.sleep(0.5)

    print(f"{bcolors.WARNING}The best path is : {bcolors.ENDC}")
    toret = f"{bcolors.FAIL}"
    old_city = best_path[0]
    toret += old_city[0]
    for city in best_path[1:]:
        toret += " --> " + city[0]
        old_city = city
    print(toret + f"{bcolors.ENDC}")
    print(f"{bcolors.WARNING}With a distance of : {bcolors.ENDC}" + str(best_distance))
    print("")
    print(f"{bcolors.OKBLUE}Parameters : {bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}Number of Ants : {bcolors.ENDC}" + str(fourmis.graph.ANT_NB))
    print(f"{bcolors.OKCYAN}Gamma : {bcolors.ENDC}" + str(fourmis.graph.GAMMA))
    print(f"{bcolors.OKCYAN}Alpha : {bcolors.ENDC}" + str(fourmis.graph.ALPHA))
    print(f"{bcolors.OKCYAN}Beta : {bcolors.ENDC}" + str(fourmis.graph.BETA))
    print(f"{bcolors.OKCYAN}Q : {bcolors.ENDC}" + str(fourmis.graph.Q))
    print(f"{bcolors.OKCYAN}Rho : {bcolors.ENDC}" + str(fourmis.graph.RHO))
    print("")

if __name__ == '__main__':
    main()
