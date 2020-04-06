import random

def initializePopulation(i):
    population = []
    for i in range(1,i+1):
        individual = []
        for j in range(8):
            zeroone = random.randint(0,1)
            individual.append(zeroone)
        population.append(individual)
    return population

def decode(arr):
    #solution = []
    #print(arr)
    #for i in arr:
    arrx1 = arr[:4]
    arrx2 = arr[4:]
    x1 = phenotype(arrx1,-3,3)
    x2 = phenotype(arrx2,-2,2)
    #solution.append(fitnessValue(x1,x2))
    value = fitnessValue(x1,x2)
    return value, x1, x2

def phenotype(arr,rmin,rmax):
    x = rmin+((rmax-rmin)/(2**-1+2**-2+2**-3+2**-4))*(arr[0]*2**-1+arr[1]*2**-2+arr[2]*2**-3+arr[3]*(2**-4))
    return x

def defaultFunction(x1,x2):
    func = (4-2*1*(x1**2)+(x1**4)/3)*x1**2+x1*x2+(-4+4*(x2**2))*x2**2
    return func

def fitnessValue(x1,x2):
    func = defaultFunction(x1,x2)
    fit = 1/(func+0.001)
    return float("%.3f"%fit)

def tournament(population,k):
    solution = []
    for i in range(len(population)):
        best = []
        for i in range(k):
            idv = population[random.randint(0, len(population) - 1)]
            # print(idv)
            if (best == []):
                best = idv
                # print("If best: ",best)
                # print("Nilai decode best mula2: ",main.decode(best))
            else:
                value_idv, x1_idv, x2_idv = decode(idv)
                value_best, x1_best, x2_best = decode(best)
                if (value_idv > value_best):
                    # print("Else best: ",best)
                    # print("Else idv: ",idv)
                    # print("ini nilai decode idv: ",main.decode(idv))
                    # print("ini nilai decode best: ", main.decode(best))
                    best = idv
                    # print("new best: ",best)
                # else:
                # print("ini nilai decode idv: ", main.decode(idv))
                # print("ini nilai decode best: ", main.decode(best))
                # print("best: ",best)
            # print("Iterasi ke-",i)
        solution.append(best)
    return solution

def crossover(solution):
    offspring = []
    count = 0
    for i in solution:
        crossoverProb = 66.7 / 100
        rng = random.uniform(0, 1)
        if (count % 2 == 0):
            if (rng <= crossoverProb):
                # print("pass")
                start = random.randint(1, len(i) - 2)
                end = random.randint(1, len(i) - 2)
                if start > end:
                    start, end = end, start
                parent1 = solution[count]
                parent2 = solution[count + 1]
                # print("ini count: ",count)
                # print(start)
                # print(end)
                # print(parent1)
                # print(parent2)
                # print("______")
                offspring1 = parent1[:start] + parent2[start:end] + parent1[end:]
                offspring2 = parent2[:start] + parent1[start:end] + parent2[end:]
                # print(offspring1)
                # print(offspring2)
                offspring.append(offspring1)
                offspring.append(offspring2)
                # print(offspring)
                # print("////////")
            else:
                # print("nope")
                parent1 = solution[count]
                parent2 = solution[count + 1]
                offspring.append(parent1)
                offspring.append(parent2)
                # print(offspring)
                # print("////////")
        count = count + 1
    return offspring

def mutate(offspring):
    mutatedoffs = []
    count = 0
    mutationProb = 0.1
    for i in offspring:
        rng = random.uniform(0, 1)
        #print(rng)
        if (rng < mutationProb):
            #print("pass")
            mutate = offspring[count]
            randIndex = random.randint(0, len(mutate) - 1)
            if (mutate[randIndex] == 0):
                mutate[randIndex] = 1
            elif (mutate[randIndex] == 1):
                mutate[randIndex] = 0
            mutatedoffs.append(mutate)
            #print("/////")
        else:
            #print("nope")
            #print(offspring[count])
            normal = offspring[count]
            mutatedoffs.append(normal)
            #print(mutatedoffs)
            #print("/////")
        count = count + 1
    return mutatedoffs

def listPair(list):
    pairList = []
    for i in list:
        a, x1, x2 = decode(i)
        pair = [i,a]
        pairList.append(pair)
    pairList = sorted(pairList, key=lambda tup: tup[1], reverse=True)
    return pairList

def generationReplace(population,mutatedoffs):
    nextGenPair = []
    nextGen = []
    c1 = 0
    c2 = 0
    for i in listPair(population):
        if (c1 <= (len(listPair(population)) / 2 - 1)):
            nextGenPair.append(i)
        else:
            break
        c1 = c1 + 1
    for i in listPair(mutatedoffs):
        if (c2 <= (len(listPair(mutatedoffs)) / 2 - 1)):
            nextGenPair.append(i)
        else:
            break
        c2 = c2 + 1
    nextGenPair = sorted(nextGenPair, key=lambda tup: tup[1], reverse=True)
    for i in nextGenPair:
        nextGen.append(i[0])
    #print(nextGenPair)
    return nextGen

def showAndCheck(nextGen):
    value, x1, x2 = decode(nextGen[0])
    print("Kromosom Terbaik : ",nextGen[0])
    print("Nilai X1         : ",x1)
    print("Nilai X2         : ",x2)
    print("Nilai Fitness    : ",value)
    print("Nilai Function   : ",defaultFunction(x1,x2))
    print("\n")

def runAlgorithm(x,n):
    a = initializePopulation(x)
    for i in range(n):
        print("Generasi ke-",i+1)
        #print("Populasi awal        : ",a)
        b = tournament(a,4)
        #print("Hasil turnament      : ",b)
        c = crossover(b)
        #print("Hasil crossover      : ",c)
        d = mutate(c)
        #print("Hasil mutasi         : ",d)
        e = generationReplace(a,d)
        #print("Generasi baru        : ",e)
        f = showAndCheck(e)
        a = e
x = int(input("Masukkan jumlah individu dalam populasi(harus genap): "))
n = int(input("Masukkan jumlah generasi                            : "))
if (x%2 == 0):
    runAlgorithm(x,n)
else:
    print("Angka harus genap, pls")