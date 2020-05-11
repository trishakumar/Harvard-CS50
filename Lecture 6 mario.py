height = 0

while(height <= 0 or height > 23):
    height = int(input("Height: "))

for row in range(height):
    
    for i in range(height - (row + 1)):
        print(" ", end='')
    
    for i in range(row + 1):
        print("#", end='')
 
    print("  ", end='')
    
    print("")
