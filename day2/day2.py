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

def correct_rps(p1, p2):
    scores = {
        'A': 1,
        'B': 2,
        'C': 3
    }
    if p1 == 'A':
        if p2 == 'X':
            return scores['C']
        if p2 == 'Y':
            return scores['A']+3
        return scores['B']+6
    if p1 == 'B':
        if p2 == 'X':
            return scores['A']
        if p2 == 'Y':
            return scores['B']+3
        return scores['C']+6
    if p1 == 'C':
        if p2 == 'X':
            return scores['B']
        if p2 == 'Y':
            return scores['C']+3
        return scores['A']+6

def get_file():
    with open('day2input.txt') as f:
        file_text = f.readlines()
    return file_text

if __name__ == '__main__':
    file_text = get_file()
    strats = [line.split(' ') for line in file_text]
    scores = [correct_rps(s[0], s[1][:-1]) if '\n' in s[1] else correct_rps(s[0], s[1]) for s in strats]
    print(sum(scores))