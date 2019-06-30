def findMaj(arr, n):
    candidate, count = 0, 0
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1
    if arr.count(candidate) > n:
        return candidate
    else:
        return -1

def main():
    with open('maj.txt', 'r') as f:
        params = [int(i.strip()) for i in f.readline().split(' ')]
        arrays = [[int(j.strip()) for j in line.split(' ')] for line in f.readlines()]
    majLen = (params[1] + 1) // 2
    maj = [str(findMaj(i, majLen)) for i in arrays]
    print(' '.join(maj))

main()
