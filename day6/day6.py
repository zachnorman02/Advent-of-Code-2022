if __name__ == '__main__':
    with open('day6/day6input.txt') as f:
        text = f.read()
    found = False
    idx = 13 #3
    while not found:
        chars = [c for c in text[idx-13:idx+1]]
        # if len(set(chars)) == 4:
        if len(set(chars)) == 14:
            found = True
        else:
            idx+=1
    print(idx+1)
    