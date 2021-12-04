with open('input.txt') as input_file:
    count = 0
    current_depth = int(input_file.readline())
    for line in input_file:
        next_depth = int(line)
        if next_depth > current_depth:
            count += 1
    print(count)


input_file_list = []

with open('input.txt') as input_file:
    for line in input_file:
        input_file_list.append(int(line))
count = 0
while len(input_file_list) > 3:
    current_window = input_file_list[:3]
    next_window = input_file_list[1:4]
    if sum(current_window) < sum(next_window):
        count += 1
    input_file_list.pop(0)
print(count)
