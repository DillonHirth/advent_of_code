# PART 1
# like day_6, make a dict with position and count, i can then determine the fuel consumption faster using counts

crab_dict = {}
with open('input.txt') as input_file:
    input_line = input_file.readline()
    crab_list = [int(x) for x in input_line.split(',')]

for item in crab_list:
    if crab_dict.get(item) == None:
        crab_dict[item] = 1
    else:
        crab_dict[item] += 1
print(crab_dict)
fuel_consumption = {}
for h_pos in range(min(crab_dict.keys()), max(crab_dict.keys()) + 1):
    fuel_use = 0
    for item in crab_dict:
        distance = abs(item - h_pos)
        crab_count_at_hpos = crab_dict[item]
        fuel_use += distance * crab_count_at_hpos
    fuel_consumption[h_pos] = fuel_use
print(min(fuel_consumption.values()))

# PART 2

crab_dict = {}
with open('input.txt') as input_file:
    input_line = input_file.readline()
    crab_list = [int(x) for x in input_line.split(',')]

for item in crab_list:
    if crab_dict.get(item) == None:
        crab_dict[item] = 1
    else:
        crab_dict[item] += 1
print(crab_dict)
fuel_consumption = {}
for h_pos in range(min(crab_dict.keys()), max(crab_dict.keys()) + 1):
    fuel_use = 0
    for item in crab_dict:
        distance = abs(item - h_pos)
        crab_count_at_hpos = crab_dict[item]
        fuel_use += sum(range(distance+1)) * crab_count_at_hpos
    fuel_consumption[h_pos] = fuel_use
print(min(fuel_consumption.values()))
