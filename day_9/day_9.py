# PART 1
low_points = []
basin_dict = {}
def check_basin_crawler(point):
    points = []
    row = point[0]
    col = point[1]
    if row == 0:
        next_row = row + 1
        if input_list[next_row][col] != '9':
            points.append((next_row, col))
    elif row == len(input_list)-1:
        prev_row = row - 1
        if input_list[prev_row][col] != '9':
            points.append((prev_row, col))
    else:
        prev_row = row - 1
        next_row = row + 1
        if input_list[prev_row][col] != '9':
            points.append((prev_row, col))
        if input_list[next_row][col] != '9':
            points.append((next_row, col))

    if col == 0:
        next_col = col + 1
        if input_list[row][next_col] != '9':
            points.append((row, next_col))
    elif col == len(input_list[row])-1:
        prev_col = col - 1
        if input_list[row][prev_col] != '9':
            points.append((row, prev_col))
    else:
        prev_col = col - 1
        next_col = col + 1
        if input_list[row][prev_col] != '9':
            points.append((row, prev_col))
        if input_list[row][next_col] != '9':
            points.append((row, next_col))
    return points







def check_basin(point):
    basin_found = []
    to_search = []
    found_points = []
    basin_found.append(point)
    to_search.append(point)
    search = True
    while search == True:
        for point in to_search:
            found_points += check_basin_crawler(point)
        completed_search = found_points + to_search
        to_search = [x for x in found_points if x not in basin_found]
        found_points = []
        for item in completed_search:
            if item not in basin_found:
                basin_found.append(item)
        if to_search:
            pass
        else:
            search = False
    basin_dict[point] = len(basin_found)



def check_horizontal(row_col_tuple):
    row = row_col_tuple[0]
    col = row_col_tuple[1]
    if col == 0:
        next_col = col + 1
        if input_list[row][next_col] > input_list[row][col]:
            return True
        return False
    elif col == len(input_list[row])-1:
        prev_col = col - 1
        if input_list[row][prev_col] > input_list[row][col]:
            return True
        return False
    else:
        prev_col = col - 1
        next_col = col + 1
        if input_list[row][next_col] > input_list[row][col] and input_list[row][prev_col] > input_list[row][col]:
            return True
        return False


def check_vertical(row_col_tuple):
    row = row_col_tuple[0]
    col = row_col_tuple[1]
    if row == 0:
        adj_down_row = row + 1
        if input_list[adj_down_row][col] > input_list[row][col]:
            return True
        return False
    elif row == len(input_list)-1:
        adj_up_row = row - 1
        if input_list[adj_up_row][col] > input_list[row][col]:
            return True
        return False
    else:
        adj_down_row = row + 1
        adj_up_row = row - 1
        if input_list[adj_up_row][col] > input_list[row][col] and input_list[adj_down_row][col] > input_list[row][col]:
            return True
        return False


def risk_level(in_list):
    risk = 0
    for i in range(len(in_list)):
        for k in range(len(in_list[i])):
            row = i
            col = k
            vertical_check = check_vertical((row, col))
            horizontal_check = check_horizontal((row, col))
            if vertical_check and horizontal_check:
                current = in_list[row][col]
                risk += int(current) + 1
                low_points.append((i, k))
    return risk



with open('input.txt') as input_file:
    input_list = []
    for line in input_file:
        input_list.append(list(line.strip('\n')))
risk = risk_level(input_list)
print("Risk: ", risk)
print("Low Points: ", low_points)
for point in low_points:
    check_basin(point)
my_keys = sorted(basin_dict, key=basin_dict.get, reverse=True)[:3]
print(my_keys)
total = 1
for key in my_keys:
    total *= basin_dict[key]
print(total)
