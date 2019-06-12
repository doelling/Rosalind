import math

def combo(n, k):
    combin = float(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
    return combin

def main():
    gens = int(input())
    atLeast = int(input())
    totalDesc = 2 ** gens
    prob = 0
    for i in range(atLeast, totalDesc + 1):
        prob += float(combo(totalDesc, i)*(0.25 ** i)*(0.75 ** (totalDesc - i)))
    print(prob)

main()
