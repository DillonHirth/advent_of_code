# PART 1
def intersections(dict, tuple_pair):
    if dict.get(tuple_pair) == None:
        dict[tuple_pair] = 0
    else:
        dict[tuple_pair] = 1


with open('input.txt') as input_file:
    ray_dict = {}
    for line in input_file:
        row = line.strip('\n').split(' -> ')
        pair1 = row[0]
        pair2 = row[1]
        x1 = int(pair1.split(',')[0])
        y1 = int(pair1.split(',')[1])
        x2 = int(pair2.split(',')[0])
        y2 = int(pair2.split(',')[1])

        if x1 == x2 or y1 == y2:
            #print(f"pair1: {x1},{y1} \tpair2: {x2},{y2}\n")
            if x1 == x2:
                if y1 > y2:
                    for item in range(y2, y1 - 1):
                        y_new = item + 1
                        new_pair = (x1, y_new)
                        intersections(ray_dict, new_pair)
                else:
                    for item in range(y1, y2 - 1):
                        y_new = item + 1
                        new_pair = (x1, y_new)
                        intersections(ray_dict, new_pair)
            if y1 == y2:
                if x1 > x2:
                    for item in range(x2, x1 - 1):
                        x_new = item + 1
                        new_pair = (x_new, y1)
                        intersections(ray_dict, new_pair)
                else:
                    for item in range(x1, x2 - 1):
                        x_new = item + 1
                        new_pair = (x_new, y1)
                        intersections(ray_dict, new_pair)
            intersections(ray_dict, (x1, y1))
            intersections(ray_dict, (x2, y2))
        else:
            #print(f"pair1: {x1},{y1} \tpair2: {x2},{y2}\n")
            x_difference = x1 - x2
            y_difference = y1 - y2
            x_new = []
            y_new = []
            if x_difference > 0:
                for item in range(abs(x_difference)-1):
                    x_new.append(x1 - (item+1))
            elif x_difference < 0:
                for item in range(abs(x_difference)-1):
                    x_new.append((x1 + (item+1)))
            if y_difference > 0:
                for item in range(abs(y_difference)-1):
                    y_new.append(y1 - (item+1))
            elif y_difference < 0:
                for item in range(abs(y_difference)-1):
                    y_new.append((y1 + (item+1)))
            new_pair_list = zip(x_new, y_new)
            for item in new_pair_list:
                intersections(ray_dict, item)


            intersections(ray_dict, (x1, y1))
            intersections(ray_dict, (x2, y2))

    sum = 0
    for item in ray_dict.values():
        sum += item
    print(sum)
