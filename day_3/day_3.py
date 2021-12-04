# PART 1
def binary_to_decimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


with open('input.txt') as input_file:
    current_line = list(input_file.readline().strip('\n'))
    count = 1
    line_length = len(current_line)
    for line in input_file:
        next_line = list(line.strip('\n'))
        result = zip(current_line, next_line)
        sum_list = [int(x) + int(y) for (x, y) in result]
        current_line = sum_list
        count += 1

print("result: ", sum_list)
gamma = []
for number in sum_list:
    if number > (count / 2):
        gamma.append(1)
    else:
        gamma.append(0)
gamma_binary = int(''.join([str(integer) for integer in gamma]))
gamma_decimal = binary_to_decimal(gamma_binary)
epsilon_binary = int(''.join(['1' if i == '0' else '0' for i in str(gamma_binary)]))
epsilon_decimal = binary_to_decimal(epsilon_binary)
print(gamma)
print("gamma_binary: ", gamma_binary)
print("gamma_decimal: ", gamma_decimal)
print("epsilon_binary: ", epsilon_binary)
print("epsilon_decimal: ", epsilon_decimal)
power_consumption = gamma_decimal * epsilon_decimal
print("power_consumption: ", power_consumption)