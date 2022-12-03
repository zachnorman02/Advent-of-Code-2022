if __name__ == '__main__':
    with open('day3input.txt') as f:
        lines = f.readlines()
    total = 0
    for i in range(0,len(lines),3):
        c1 = lines[i]
        c2 = lines[i+1]
        c3 = lines[i+2]
        for x in c1:
            if x in c2 and x in c3:
                value = ord(x)-96 if ord(x)>96 else ord(x)-38
                total += value
                break
    print(total)
    