if __name__ == '__main__':
    with open('day4/day4input.txt') as f:
        input = f.readlines()
    full_overlap=0
    overlap=0
    pairs = [l.split(',') for l in input]
    for pair in pairs:
        r1 = pair[0].split('-')
        r2 = pair[1].split('-')
        section1 = list(range(int(r1[0]),int(r1[1])+1))
        section2 = list(range(int(r2[0]),int(r2[1])+1))
        if all(x in section2 for x in section1) or all(x in section1 for x in section2):
            full_overlap += 1
        if any(x in section2 for x in section1) or any(x in section1 for x in section2):
            overlap += 1
    
    print(full_overlap)
    print(overlap)