# PART 1
syntax_open = {'[':']', '{':'}', '(':')', '<':'>'}
syntax_closed = {']':'[', '}':'{', ')':'(', '>':'<'}
score_dict = {']':0, '}':0, '>':0, ')':0}
score = 0

def traversal(list):
    for i in range(len(list)-1):
        if syntax_open.get(list[i]) == list[i+1]:
            list.pop(i)
            list.pop(i)
            return traversal(list)
    print(''.join(list))
    return list

def scoring(list):
    for i in range(len(list)):
        if list[i] in syntax_closed.keys() and syntax_closed[list[i]] != list[i-1]:
            print("error:",list[i])
            score_dict[list[i]] += 1
            return score_dict
        else:
            return "dank"

with open('input.txt') as input_file:
    for line in input_file:
        scoring(traversal(list(line.strip('\n'))))
score += score_dict[']'] * 57
score += score_dict[')'] * 3
score += score_dict['}'] * 1197
score += score_dict['>'] * 25137
print(score)




# from statistics import median
#
# corrupt_scores = {
#     ")": 3,
#     "]": 57,
#     "}": 1197,
#     ">": 25137,
# }
# incomplete_scores = {
#     ")": 1,
#     "]": 2,
#     "}": 3,
#     ">": 4,
# }
# matches = {
#     "(": ")",
#     "[": "]",
#     "{": "}",
#     "<": ">",
# }
#
#
# def part_one(filename: str) -> int:
#     with open(filename) as f:
#         lines = map(lambda line: line.strip(), f.readlines())
#
#     total = 0
#     for line in lines:
#         queue = []
#         for ch in line:
#             if ch in matches:
#                 queue.append(matches[ch])
#             else:
#                 if not queue or ch != queue.pop():
#                     print(corrupt_scores[ch])
#                     total += corrupt_scores[ch]
#                     break
#
#     return total
#
#
# def part_two(filename: str) -> int:
#     with open(filename) as f:
#         lines = map(lambda line: line.strip(), f.readlines())
#
#     scores = []
#     for line in lines:
#         queue = []
#         is_corrupted = False
#         for ch in line:
#             if ch in matches:
#                 queue.append(matches[ch])
#             else:
#                 if not queue or ch != queue.pop():
#                     is_corrupted = True
#                     break
#         if not is_corrupted:
#             score = 0
#             while queue:
#                 ch = queue.pop()
#                 score = 5 * score + incomplete_scores[ch]
#             scores.append(score)
#
#     return median(scores)
#
#
# if __name__ == "__main__":
#     input_path = "input.txt"
#     print("---Part One---")
#     print(part_one(input_path))
#
#     print("---Part Two---")
#     print(part_two(input_path))

# 3
# 3
# 25137
# 3
# 3
# 25137
# 57
# 3
# 57
# 1197
# 1197
# 1197
# 3
# 57
# 57
# 57
# 25137
# 57
# 57
# 25137
# 1197
# 25137
# 3
# 3
# 1197
# 1197
# 3
# 25137
# 25137
# 25137
# 57
# 1197
# 25137
# 3
# 25137
# 57
# 57
# 3
# 3
# 1197
# 3
# 3
# 3
# 57
# 3
# 25137
# 25137
# 25137
# 57
# 25137
# 25137

