# invoice border pattern

rows=7
cols=30

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols -1:
            print("*" , end="")
        else:
            print(" ",end="")
    print()

#receipt pattern

rows=8

for i in range(rows):
    for j in range(20):
        print("*" , end="")
    print()   

#invoice number pattern

rows = 5

for i in range(1, rows + 1):
    for j in range(1,6):
        print(j, end=" ")
    print() 

#receipt number pattern

rows = 5

for i in range(1, rows + 1):
    for j in range(1,i + 1):
        print(j, end=" ")
    print() 

# inverted star pattern

rows = 5 

for i in range(rows,0,-1):
    for j in range(i):
        print("*", end=" ")
    print() 

# star triangle

rows = 5 

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print() 