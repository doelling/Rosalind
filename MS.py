from heapq import merge #Returns sorted merged list given 2 presorted lists   

def mergeSort(arr):
    if len(arr) <= 1:
        return arr #End recursion at single entries
    mid = len(arr)//2
    lArr = mergeSort(arr[:mid])
    rArr = mergeSort(arr[mid:])
    return(list(merge(lArr, rArr))) #1 item lists are sorted by default

def main():
    with open('ms.txt', 'r') as f:
        lenArray = int(f.readline().strip())
        toSort = [int(i.strip()) for i in f.readline().split(' ')]
    print(mergeSort(toSort))

main()
