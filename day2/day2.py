def rps(p1, p2):
    scores = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    v1 = ord(p1)
    v2 = ord(p2)-23
    # 3 for tie, 6 for win
    if v1 == v2:
        return 3+scores[p2]
    if (v1 == 65 and v2 == 67) or (v1 == 67 and v2 == 66) or (v1 == 66 and v2 == 65):
        return scores[p2]
    return 6 + scores[p2]

def get_file():
    with open('day2input.txt') as f:
        file_text = f.readlines()
    return file_text

if __name__ == '__main__':
    file_text = get_file()
    strats = [line.split(' ') for line in file_text]
    print(strats)