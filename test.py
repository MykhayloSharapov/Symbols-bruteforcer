numbers = [1,2,3,4,5,6,7,8,9]

def concatenate (x,y):
    return int(str(x)+str(y))

cltocheck = [   'cc+c-c+-', 'cc-c-c+c', 'cc-c-c-c']

cl = [ 'c------c', 'cc+-+c-c']

for line in cl:
    a = list (line)
    zipped = []
    i = 0
    while i <len(a):
        zipped.append(numbers[i])
        zipped.append(a[i])
        i+=1
    zipped.append(numbers[-1])
    while 'c' in zipped:
        for index, c in enumerate(zipped): 
            if c =='c':
                b = concatenate(zipped[index-1],zipped[index+1])
                zipped[index-1]=b
                zipped.pop(index)
                zipped.pop(index)
                print(zipped)
    while '-' in zipped:
        for index, c in enumerate (zipped):
            if c =='-':
                b = zipped[index-1]- zipped[index+1]
                zipped[index-1]=b
                zipped.pop(index)
                zipped.pop(index)
                print(zipped)
    while '+' in zipped:
        for index, c in enumerate (zipped):
            if c =='+':
                b = zipped[index-1]+zipped[index+1]
                zipped[index-1]=b
                zipped.pop(index)
                zipped.pop(index)
                print(zipped)
    
