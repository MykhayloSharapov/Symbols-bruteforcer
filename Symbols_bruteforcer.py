# this module generates all possible combination of commands
# to be performed on numbers

# there are three kind of command: add('+'), minus ('-') and concatenate ('c')
# number of their combination equals
# three powered by the number of positions available


# n = number of positions available
n=8

def combinations(n):
    i=1
    b=0
    while i <=n:
        b+=3**i
        i+=1
    return b

cl=['+', '-', 'c']
signs =['+', '-', 'c']

for j in cl:
    while len(cl)<combinations(n):
        for m in signs:
            cl.append(j+m)
        break

i=0
while i <combinations(n-1):
    cl.pop(0)
    i+=1
    
# this module takes in command lines from the list
# concatenate numbers (if applicable),
# clears command line from concatenation commands 
# and then executes the rest of commands
# on the list of numbers after concatenation (if any)

numbers = [1,2,3,4,5,6,7,8,9]

def concatenate (x,y):
    return int(str(x)+str(y))

d= []

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
    while '-' in zipped:
        for index, c in enumerate (zipped):
            if c =='-':
                b = zipped[index-1]- zipped[index+1]
                zipped[index-1]=b
                zipped.pop(index)
                zipped.pop(index)
    while '+' in zipped:
        for index, c in enumerate (zipped):
            if c =='+':
                b = zipped[index-1]+zipped[index+1]
                zipped[index-1]=b
                zipped.pop(index)
                zipped.pop(index)
    if zipped[0]==100: 
        d.append(line)

print (d)
