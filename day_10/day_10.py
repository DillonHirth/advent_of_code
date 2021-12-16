# PART 1
syntax_open = {'[':']', '{':'}', '(':')', '<':'>'}
syntax_closed = {']':'[', '}':'{', ')':'(', '>':'<'}

def traversal(list):
    for i in range(len(list)-1):
        if syntax_open.get(list[i]) == list[i+1]:
            list.pop(i)
            list.pop(i)
            traversal(list)
            break
    return ''.join(list)


with open('input_test.txt') as input_file:

    for line in input_file:
        print(traversal(list(line.strip('\n'))))




