import fourmis

count = 0

def main():
    for g in range(1,4):
        for a in range(6,11):
            print("{}/15".format(count+1))
            for b in range(4,7):
                for q in range(1,4):
                    for rho in range(6,13):
                        for k in range (15):
                            fourmis.graph.set_var(g/10,a/10,b/10,q/2,rho/10)
                            fourmis.main(True)


def best_gamma():
    fourmis.graph.set_iter(120)
    for g in range(25,400,25):
        print(str(int(g/25))+"/15")
        for _ in range(500):
            fourmis.graph.set_var(g=g/1000)
            fourmis.main(True)

def best_alpha():
    fourmis.graph.set_iter(120)
    for a in range(20,140,20):
        print(str(int(a/20))+"/6")
        for _ in range(500):
            fourmis.graph.set_var(a=a/100)
            fourmis.main(True)

def best_beta():
    fourmis.graph.set_iter(120)
    for b in range(20,180,20):
        print(str(int(b/20))+"/8")
        for _ in range(500):
            fourmis.graph.set_var(b=b/100)
            fourmis.main(True)

def best_Q():
    fourmis.graph.set_iter(120)
    for q in range(50,175,25):
        print(str(int((q-25)/25))+"/5")
        for _ in range(500):
            fourmis.graph.set_var(q=q/100)
            fourmis.main(True)


def best_rho():
    fourmis.graph.set_iter(120)
    for r in range(40,110,10):
        print(str(int((r-30)/10))+"/7")
        for _ in range(500):
            fourmis.graph.set_var(rho=r/100)
            fourmis.main(True)

def find_best():
    fourmis.graph.set_iter(300)
    fourmis.main()

best_rho()
