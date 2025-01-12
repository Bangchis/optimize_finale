# PYTHON
the_input = []
while True:
    temp = input()
    if temp == "#":
        break
    else:
        the_input.append(temp)


n = int(the_input[0])
variable = [int(x) for x in the_input[1].split()]
commands = the_input[2::]
existed_commands = []


def IsEqual(i, j):
    if variable[i-1] != variable[j-1]:
        return abs(variable[i-1] - variable[j-1])
    else:
        return 0


def LessThanEqual(i, j):
    if variable[i-1] > variable[j-1]:
        return variable[i-1] - variable[j-1]
    else:
        return 0


def AllDifferent():
    count = 0
    freq = {}

    # Đếm tần số xuất hiện của mỗi phần tử
    for num in variable:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Tính số cặp có thể tạo ra từ các phần tử giống nhau
    for v in freq.values():
        if v > 1:
            count += v * (v - 1) // 2

    return count


def update(i, value, variable):
    variable[int(i)-1] = int(value)


for command in commands:
    if command.strip() == 'violations':
        vio = 0

        for e in existed_commands:

            if e.split()[1] == "AllDifferent":
                vio += AllDifferent()

                continue
            elif e.split()[1] == "IsEqual":

                vio += IsEqual(int(e.split()[2]), int(e.split()[3]))
            elif e.split()[1] == "LessThanEqual":

                vio += LessThanEqual(int(e.split()[2]), int(e.split()[3]))

        print(vio)
        continue
    elif command.split()[0] == "update":
        update(command.split()[1], command.split()[2], variable)

        continue
    else:
        existed_commands.append(command)
        continue
