def advMonth(lst):
    babies = sum(lst[1:])
    for i in reversed(range(1, len(lst), 1)):
        lst[i] = lst[i-1]
    lst[0] = babies
    return lst
    

def main ():
    noMos = int(input())
    lifetime = int(input())
    simulator = [0 for i in range(lifetime)]
    simulator[0] = 1
    for i in range(noMos-1):
        simulator = advMonth(simulator)
    print(sum(simulator))

main()
    
