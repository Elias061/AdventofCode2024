number=[]

def Read_File():
    
    file = open("C:\\Users\\beel174\\Documents\\GitHub\\AdventofCode2024\\Day2\\source.txt")
    content = file.read()
    content = content.split("\n")
    return content


def data_handling(content):
    for index in content:
        einzelne_zahlen=index.split(" ")
        number.append(einzelne_zahlen)
    return number
    

def mode_increasing(number):
    index=0
    validList= []
    for liste in number:
        index = 0
        StatusValide = True
        for element in liste:
            if int(element) > int(element[index])+1:
                print(f"valid {element}")
                #StatusValide= True
            else:
                print(f"huso {element}")    
                StatusValide = False


content = Read_File()
data_handling(content)
mode_increasing(number)