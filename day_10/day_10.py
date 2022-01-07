# PART 1
syntax_open = {'[':']', '{':'}', '(':')', '<':'>'}
syntax_closed = {']':'[', '}':'{', ')':'(', '>':'<'}
score_dict = {']':0, '}':0, '>':0, ')':0}
part2_score = []
incompletes = []

def traversal(list):
    for i in range(len(list)-1):
        if syntax_open.get(list[i]) == list[i+1]:
            list.pop(i)
            list.pop(i)
            return traversal(list)
    print(''.join(list))
    return list

def part2_scoring(list):
    score_dict_part2 = {'[': 2, '{': 3, '<': 4, '(': 1}
    score = 0
    for item in reversed(list):
        print("score: ", score)
        score = (score * 5) + score_dict_part2[item]
        print("score now:", score)
    return score

def scoring(list):
    error = False

    for i in range(len(list)):
        if list[i] in syntax_closed.keys() and syntax_closed[list[i]] != list[i-1]:
            print("error:",list[i])
            score_dict[list[i]] += 1
            error = True
            return score_dict
    if error == False:
        print('found incomplete', list)
        incompletes.append(list)

with open('input.txt') as input_file:
    for line in input_file:
        scoring(traversal(list(line.strip('\n'))))

part1_score = 0
part1_score += score_dict[']'] * 57
part1_score += score_dict[')'] * 3
part1_score += score_dict['}'] * 1197
part1_score += score_dict['>'] * 25137
print("part1: ", part1_score)

for item in incompletes:
    part2_score.append(part2_scoring(item))
middle_score = sorted(part2_score)
print("part2: ", middle_score[len(middle_score)//2])
