# PART 1

def special_counter(value_list):
    count = 0
    for sequence in value_list:
        if len(sequence) not in [5, 6]:
            count += 1
    return count

with open('input.txt') as input_file:
    total = 0
    for line in input_file:
        output_values_list = [x.strip('\n') for x in line.split(' | ')[1].split(' ')]
        total += special_counter(output_values_list)
print(total)

# PART 2

def process_input_values(value_list):
    signals = 'abcdefg'
    key_dict = {}
    pos_dict = {}
    for item in value_list:
        if len(item) == 2:
            key_dict['1'] = item
        elif len(item) == 3:
            key_dict['7'] = item
        elif len(item) == 4:
            key_dict['4'] = item
        elif len(item) == 7:
            key_dict['8'] = item
    pos_dict['TOP'] = [x for x in key_dict['7'] if x not in key_dict['1']][0]
    for item in value_list:
        if len(item) == 5 and all(x in item for x in key_dict['7']):
            key_dict['3'] = item
    pos_dict['BOTTOM'] = [x for x in key_dict['3'] if x not in key_dict['4'] and x not in pos_dict['TOP']][0]
    pos_dict['MIDDLE'] = [x for x in key_dict['4'] if x not in key_dict['1'] and x in key_dict['3']][0]
    pos_dict['TOP_LEFT'] = [x for x in key_dict['4'] if x not in key_dict['1'] and x not in key_dict['3']][0]
    for item in value_list:
        if len(item) == 5 and pos_dict['TOP_LEFT'][0] in item:
            key_dict['5'] = item
    pos_dict['BOTTOM_RIGHT'] = [x for x in key_dict['1'] if x in key_dict['5']][0]
    pos_dict['TOP_RIGHT'] = [x for x in key_dict['1'] if x not in pos_dict['BOTTOM_RIGHT']][0]
    pos_dict['BOTTOM_LEFT'] = [x for x in signals if x not in pos_dict.values()][0]
    key_dict['2'] = [pos_dict['TOP'], pos_dict['BOTTOM'], pos_dict['MIDDLE'], pos_dict['TOP_RIGHT'], pos_dict['BOTTOM_LEFT']]
    key_dict['6'] = [pos_dict['TOP'], pos_dict['TOP_LEFT'], pos_dict['BOTTOM'], pos_dict['MIDDLE'], pos_dict['BOTTOM_RIGHT'], pos_dict['BOTTOM_LEFT']]
    key_dict['9'] = [pos_dict['TOP'], pos_dict['TOP_LEFT'], pos_dict['BOTTOM'], pos_dict['MIDDLE'], pos_dict['TOP_RIGHT'], pos_dict['BOTTOM_RIGHT']]
    key_dict['0'] = [pos_dict['TOP'], pos_dict['TOP_LEFT'], pos_dict['BOTTOM'], pos_dict['BOTTOM_LEFT'], pos_dict['TOP_RIGHT'], pos_dict['BOTTOM_RIGHT']]
    print("key: ", key_dict)
    print("pos: ", pos_dict)
    return key_dict

def process_output_values(output_list, key_dict):
    total = ''
    for items in output_list:
        items.sort()
        for key in key_dict.keys():
            list = key_dict[key]
            list.sort()
            if list == items:
                total += key
    print("total: ", total)
    return total




with open('input.txt') as input_file:
    output_total = 0
    for line in input_file:
        input_values_list = [list(x.strip('\n')) for x in line.split(' | ')[0].split(' ')]
        output_values_list = [list(x.strip('\n')) for x in line.split(' | ')[1].split(' ')]

        output_total += int(process_output_values(output_values_list, process_input_values(input_values_list)))
    print("output_total: ", output_total)

