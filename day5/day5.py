if __name__ == '__main__':
    with open('day5/day5input.txt') as f:
        lines = f.readlines()
    stacks = lines[:8]
    directions = lines[9:]
    full_stacks = [
        [s[0] for s in stacks if s[0] not in (' ', '\n')],
        [s[2] for s in stacks if s[2] not in (' ', '\n')],
        [s[4] for s in stacks if s[4] not in (' ', '\n')],
        [s[6] for s in stacks if s[6] not in (' ', '\n')],
        [s[8] for s in stacks if s[8] not in (' ', '\n')],
        [s[10] for s in stacks if s[10] not in (' ', '\n')],
        [s[12] for s in stacks if s[12] not in (' ', '\n')],
        [s[14] for s in stacks if s[14] not in (' ', '\n')],
        [s[16] for s in stacks if s[16] not in (' ', '\n')],
    ]
    for d in directions:
        dirs = [n for n in d.replace('move', '').replace('from', '').replace('to', '').split(' ') if n != '']
        amt = int(dirs[0])
        fro = int(dirs[1])
        to = int(dirs[2])
        part2list = []
        for i in range(amt):
            # full_stacks[to-1].insert(0, full_stacks[fro-1].pop(0))
            part2list.append(full_stacks[fro-1].pop(0))
        full_stacks[to-1] = part2list + full_stacks[to-1]
    print(full_stacks)
        
