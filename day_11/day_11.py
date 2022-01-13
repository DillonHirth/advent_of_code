# PART 1
input_matrix = []

def cascading_flash(row, col):
    print("flash at:", row, ":", col)
    input_matrix[row][col] = 0

def increment(row, col):
    print("before:", input_matrix[row][col])
    input_matrix[row][col] = input_matrix[row][col] + 1
    print("after:", input_matrix[row][col])
    if input_matrix[row][col] > 9:
        print("flash!, now go check others!")
        cascading_flash(row, col)

with open('input_test2.txt') as input_file:
    for line in input_file:
        # convert string to list of integers then append to list of lists
        input_matrix.append(list(map(int, line.strip('\n'))))
for step in range(2):
    for row in range(len(input_matrix)):
        for col in range(len(input_matrix[row])):
            increment(row, col)

    with open('output.txt', 'a') as input_file:
        for line in input_matrix:
            # convert string to list of integers then append to list of lists
            print(line)
            input_file.write(''.join(str(int) for int in line)+'\n')
        input_file.write('\n')