import string
kicsi = list(string.ascii_lowercase)
nagy = list(string.ascii_uppercase)



def getValue(d):
    value = 1
    for i in kicsi:
        if i == d:
            break
        else:
            value = value + 1 
    return value   

def getValueNagy(d):
    value = 27
    for i in nagy:
        if i == d:
            break
        else:
            value = value + 1 
    return value   


    
def part1():
    file = open("C:\\Users\\tasna\\Documents\\Szkript\\AD22\\3\\input.txt")
    kozos = []
    for i in file:
        firstpart, secondpart = i[:len(i)//2], i[len(i)//2:]
        comm = set(firstpart)&set(secondpart)
        temp = ''.join(comm)
        kozos.append(temp)
        
    sumKicsi = 0
    sumNagy = 0

    for i in kozos:
        if i in kicsi:
            sumKicsi = sumKicsi + getValue(i)
        if i in nagy:
            sumNagy = sumNagy + getValueNagy(i)
            
    part1 = sumKicsi+sumNagy
    print(str(part1))
    file.close()

def part2():
    file = open("C:\\Users\\tasna\\Documents\\Szkript\\AD22\\3\\input.txt")
    
    b = []
    temp = file.read().splitlines()
    for i in temp:
        b.append(i)
    
    kozos2 = []
    for i in range(0,len(b)-2,3):
        c = set(b[i])&set(b[i+1])&set(b[i+2])
        temp = ''.join(c)
        kozos2.append(temp)
    
    sk = 0
    sn = 0
    
    for i in kozos2:
        if i in kicsi:
            sk = sk + getValue(i)
        if i in nagy:
            sn = sn + getValueNagy(i)
            
    part1 = sk+sn
    print(str(part1))
    
    file.close()
       
def main():
    part1()
    part2()

if __name__ == "__main__":
    main()