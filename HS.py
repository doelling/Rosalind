import heapq

def main():
    with open('hs.txt', 'r') as f:
        items = int(f.readline().strip())
        unsHeap = [int(i.strip()) for i in f.readline().split(' ')]
    heapq.heapify(unsHeap)
    sHeap = [heapq.heappop(unsHeap) for i in range(len(unsHeap))]
    with open('hs_out.txt', 'w') as outf:
        for j in sHeap:
            outf.write('%i ' % j)

main()
