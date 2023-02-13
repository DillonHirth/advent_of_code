# PART 1

class LanternFish:
    def __init__(self, age=9):
        self.age = age

    def __repr__(self):
        return str(self.age)

    def aging(self):
        if self.age == 0:
            fish_list.append(LanternFish())
            self.age = 6
        else:
            self.age -= 1


with open('input_test.txt') as input_file:
    input_line = input_file.readline()
    fish_list = [LanternFish(int(x)) for x in input_line.split(',')]
#print(fish_list)
for i in range(1, 81):
    for fish in fish_list:
        fish.aging()
#print(len(fish_list))


# PART 2
#wowowowow hahaha, the solution to part one was fun, but rather inefficient. tried it for part 2, and managed to get pycharm to pull out roughly 40gb's of memory for the dictionary XD hahahaha.
# super happy with this new solution, although less visually pleasing.
class LanternFishSchool:
    def __init__(self):
        self.school_of_fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    def __repr__(self):
        return str(self.school_of_fish)

    def aging(self):
        zero_count = self.school_of_fish[0]
        self.school_of_fish[0] = self.school_of_fish[1]
        self.school_of_fish[1] = self.school_of_fish[2]
        self.school_of_fish[2] = self.school_of_fish[3]
        self.school_of_fish[3] = self.school_of_fish[4]
        self.school_of_fish[4] = self.school_of_fish[5]
        self.school_of_fish[5] = self.school_of_fish[6]
        self.school_of_fish[6] = self.school_of_fish[7] + zero_count
        self.school_of_fish[7] = self.school_of_fish[8]
        self.school_of_fish[8] = zero_count


with open('input.txt') as input_file:
    input_line = input_file.readline()
    fish_list = [int(x) for x in input_line.split(',')]

fish_school = LanternFishSchool()
for item in fish_list:
    fish_school.school_of_fish[item] += 1
print("Initial:", fish_school.school_of_fish)
for i in range(1, 257):
    fish_school.aging()
    print(i, ":", fish_school.school_of_fish)
count = 0
for value in fish_school.school_of_fish.values():
    count += value
print("count: ", count)

