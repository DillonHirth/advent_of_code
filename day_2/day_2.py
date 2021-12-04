# PART 1
with open('input.txt') as input_file:
    x_pos = 0
    y_pos = 0
    for line in input_file:
        direction = line.split(' ')[0]
        distance = int(line.split(' ')[1])
        if direction == "forward":
            x_pos += distance
        elif direction == "down":
            y_pos += distance
        else:
            y_pos -= distance
print(x_pos * y_pos)

# PART 2
with open('input.txt') as input_file:
    x_pos = 0
    y_pos = 0
    aim_vector = 0
    for line in input_file:
        direction = line.split(' ')[0]
        distance = int(line.split(' ')[1])
        print("*******************************************")
        print("direction:", direction)
        print("distance:", distance)
        print("old_aim:", aim_vector)
        print("old_x_pos:", x_pos)
        print("old_y_pos:", y_pos)
        print("---------------------------")
        if direction == "forward":
            x_pos += distance
            y_pos += aim_vector * distance
        elif direction == "down":
            aim_vector += distance
        else:
            aim_vector -= distance
        print("direction:", direction)
        print("distance:", distance)
        print("aim:", aim_vector)
        print("x_pos:", x_pos)
        print("y_pos:", y_pos)
        print("*******************************************")
print("x_pos:", x_pos)
print("y_pos:", y_pos)
print("x*y:", x_pos * y_pos)