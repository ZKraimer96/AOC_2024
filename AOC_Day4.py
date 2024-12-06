def check_horizontal(x, line):
    count = 0
    if(x > 2):
        if(line[x-1] == 'M'):
            if(line[x-2] == 'A'):
                if(line[x-3] == 'S'):
                    count += 1
    if(x < len(line) - 3):
        if(line[x+1] == 'M'):
            if(line[x+2] == 'A'):
                if(line[x+3] == 'S'):
                    count += 1
    return count
    
def check_vertical(x, y, content):
    count = 0
    if(y > 2):
        if(content[y-1][x] == 'M'):
            if(content[y-2][x] == 'A'):
                if(content[y-3][x] == 'S'):
                    count += 1
    if(y < len(content) - 3):
        if(content[y+1][x] == 'M'):
            if(content[y+2][x] == 'A'):
                if(content[y+3][x] == 'S'):
                    count += 1
    
    return count
    
def check_diagnol(x, y, content):
    count = 0
    if(x > 2 and y > 2):
        if(content[y-1][x-1] == 'M'):
            if(content[y-2][x-2] == 'A'):
                if(content[y-3][x-3] == 'S'):
                    count += 1
    if(x < len(content[y]) - 3 and y < len(content) - 3):
        if(content[y+1][x+1] == 'M'):
            if(content[y+2][x+2] == 'A'):
                if(content[y+3][x+3] == 'S'):
                    count += 1
    if(x > 2 and y < len(content) - 3):
        if(content[y+1][x-1] == 'M'):
            if(content[y+2][x-2] == 'A'):
                if(content[y+3][x-3] == 'S'):
                    count += 1
    if(x < len(content[y]) - 3 and y > 2):
        if(content[y-1][x+1] == 'M'):
            if(content[y-2][x+2] == 'A'):
                if(content[y-3][x+3] == 'S'):
                    count += 1
    
    return count
    
def check_cross(x, y, content):
    leftDiag = False
    rightDiag = False
    if(x > 0 and y > 0 and x < len(content[y]) - 1 and y < len(content) - 1):
        if(content[y-1][x-1] == 'M'):
            if(content[y+1][x+1] == 'S'):
                leftDiag = True
        if(content[y-1][x-1] == 'S'):
            if(content[y+1][x+1] == 'M'):
                leftDiag = True
        if(content[y+1][x-1] == 'M'):
            if(content[y-1][x+1] == 'S'):
                rightDiag = True
        if(content[y+1][x-1] == 'S'):
            if(content[y-1][x+1] == 'M'):
                rightDiag = True
        
        
    return (leftDiag and rightDiag)
    
content = []
with open('C:/Users/kman9/Coding/AOC_Day4_Input.txt', 'r') as file:
    content = file.readlines()

y = 0
xmasCount = 0
while y < len(content):
    line = content[y]
    x = 0
    while x < len(line):
        if(line[x] == 'X'):
            xmasCount += check_horizontal(x, line)
            xmasCount += check_vertical(x, y, content)
            xmasCount += check_diagnol(x, y, content)
        x += 1
    y += 1
print(xmasCount)

y = 0
xmasCount = 0
while y < len(content):
    line = content[y]
    x = 0
    while x < len(line):
        if(line[x] == 'A'):
            if(check_cross(x, y, content)):
                xmasCount += 1
        x += 1
    y += 1
print(xmasCount)