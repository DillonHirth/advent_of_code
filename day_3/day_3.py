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
power_consumption = gamma_decimal * epsilon_decimal
print("power_consumption: ", power_consumption)

# Part 2
with open('input.txt') as input_file:
    input_list = input_file.readlines()


def oxy_gen_rating(sweet_list, pointer=0):
    new_list = []
    filter = bit_criteria_more(sweet_list, pointer)
    for item in sweet_list:
        if int(item[pointer]) == filter:
            new_list.append(item.strip('\n'))
    pointer += 1
    if len(new_list) > 1:
        return oxy_gen_rating(new_list, pointer)
    else:
        oxy_gen_binary = int(''.join([str(integer) for integer in new_list]))
        return binary_to_decimal(oxy_gen_binary)


def co2_scrub_rating(sweet_list, pointer=0):
    new_list = []
    filter = bit_criteria_fewer(sweet_list, pointer)
    for item in sweet_list:
        if int(item[pointer]) == filter:
            new_list.append(item.strip('\n'))
    pointer += 1
    if len(new_list) > 1:
        return co2_scrub_rating(new_list, pointer)
    else:
        co2_scrub_binary = int(''.join([str(integer) for integer in new_list]))
        return binary_to_decimal(co2_scrub_binary)


def bit_criteria_more(sweet_list, position=0):
    # create empty list
    current_item = [0] * len(sweet_list[0].strip('\n'))
    count = 0
    for list_item in sweet_list:
        next_item = list(list_item.strip('\n'))
        result = zip(current_item, next_item)
        sum_list = [int(x) + int(y) for (x, y) in result]
        current_item = sum_list
        count += 1
    if sum_list[position] >= count / 2:
        return 1
    else:
        return 0


def bit_criteria_fewer(sweet_list, position=0):
    # create empty list
    current_item = [0] * len(sweet_list[0].strip('\n'))
    count = 0
    for list_item in sweet_list:
        next_item = list(list_item.strip('\n'))
        result = zip(current_item, next_item)
        sum_list = [int(x) + int(y) for (x, y) in result]
        current_item = sum_list
        count += 1
    if sum_list[position] >= count / 2:
        return 0
    else:
        return 1

oxy_gen_rating(input_list)
co2_scrub_rating(input_list)
life_support_rating = oxy_gen_rating(input_list) * co2_scrub_rating(input_list)
print("life_support_rating: ", life_support_rating)
