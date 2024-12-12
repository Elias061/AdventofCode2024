print("Day 1, Question 1")
left_list=[]
right_list=[]
index=0
differenz=0

def readDataFromFile():
    global left_list
    global right_list
    global index
    global differenz
    
    file = open("C:\\Users\\beel174\\Documents\\GitHub\\AdventofCode2024\\Day1\\source.txt")
    content = file.read()
    content=content.split("\n")
    for line in content:
        line.split(" ")
        temp_arr=line.split("   ")
        left_list.append(int(temp_arr[0]))
        right_list.append(int(temp_arr[1]))
        left_list.sort()
        right_list.sort()
    if len(left_list)==len (right_list):
        for index in range (len(left_list)):
          dif=  abs(left_list[index]-right_list[index])
          differenz+=dif
    print(differenz)
    file.close()
   
readDataFromFile()
