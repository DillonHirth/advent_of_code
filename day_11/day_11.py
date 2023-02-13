# PART 1
input_matrix = []


class indecent_flashing_octopus:
    def __init__(self, age, row, col):
        self.age = age
        self.row = row
        self.col = col
        self.has_flashed = False
        self.surrounding = [[row + 1, col - 1], [row + 1, col], [row + 1, col + 1],
                            [row, col - 1], [row, col + 1],
                            [row - 1, col - 1], [row - 1, col], [row - 1, col + 1]]

    def __repr__(self):
        return str(self.age)

    def cascading_flash(self):
        if self.age > 9:
            print("flash!")
            self.has_flashed = True
            for pair in self.surrounding:
                try:
                    if input_matrix[pair[0]][pair[1]].age > 9 and input_matrix[pair[0]][pair[1]].has_flashed != True:
                        input_matrix[pair[0]][pair[1]].cascading_flash()
                    else:
                        input_matrix[pair[0]][pair[1]].increment()
                except IndexError:
                    pass

    def increment(self):
        if self.has_flashed == False:
            print("before:", self.age)
            self.age += 1
            print("after:", self.age)
        else:
            pass

    def reset_to_zero(self):
        if self.has_flashed == True:
            self.has_flashed = False
            self.age = 0


with open('input_test.txt') as input_file:
    for line in input_file:
        # convert string to list of integers then append to list of lists
        input_matrix.append(list(map(int, line.strip('\n'))))

for row in range(len(input_matrix)):
    for col in range(len(input_matrix[row])):
        age = input_matrix[row][col]
        input_matrix[row][col] = indecent_flashing_octopus(age, row, col)

for step in range(2):
    for row in range(len(input_matrix)):
        for col in range(len(input_matrix[row])):
            input_matrix[row][col].increment()
    for row in range(len(input_matrix)):
        for col in range(len(input_matrix[row])):
            input_matrix[row][col].cascading_flash()
    for row in range(len(input_matrix)):
        for col in range(len(input_matrix[row])):
            input_matrix[row][col].reset_to_zero()


    with open('output.txt', 'a') as input_file:
        message = f"step: {step+1}"
        input_file.write(message + '\n')
        for line in input_matrix:
            # convert string to list of integers then append to list of lists
            input_file.write(''.join(str(int) for int in line) + '\n')
        input_file.write('\n')
