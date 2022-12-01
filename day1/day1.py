def sum_elves(values:str):
    vals = values.split('\n')
    return sum([int(v) for v in vals])

def get_file_values():
    with open('day1input.txt') as f:
        file_text = f.read()
    return file_text.split('\n\n')

def get_maximum_calories():
    file_text_lines = get_file_values()
    return max([sum_elves(line) for line in file_text_lines])

def get_top_three_calories():
    file_text_lines = get_file_values()
    cal_values = [sum_elves(line) for line in file_text_lines]
    cal_values.sort(reverse=True)
    return sum(cal_values[0:3])

if __name__ == '__main__':
    print(get_maximum_calories())
    print(get_top_three_calories())