print("Day 1, Question 1")
left_list = []
right_list = []
index = 0
differenz = 0


def readDataFromFile():
    global left_list
    global right_list
    global index
    global differenz
    i = 0
    file = open(
        "C:\\Users\\beel174\\Documents\\GitHub\\AdventofCode2024\\Day1\\source.txt"
    )
    content = file.read()
    content = content.split("\n")
    for line in content:
        line.split(" ")
        temp_arr = line.split("   ")
        left_list.append(int(temp_arr[0]))
        right_list.append(int(temp_arr[1]))
        left_list.sort()
        right_list.sort()
    if len(left_list) == len(right_list):
        sumOfSimCount = 0
        counter = 0
        while counter < len(left_list):
            simCount = 0
            for element in right_list:
                if left_list[counter] == element:
                    simCount = simCount + 1
            sumOfSimCount = sumOfSimCount + int(left_list[counter]) * simCount
            counter = counter + 1
        print(sumOfSimCount)

    file.close()


readDataFromFile()
