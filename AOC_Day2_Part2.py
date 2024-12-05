
def safe(values):
    i = 0
    direct = 0
    while i < len(values)-1:
        curr = values[i]
        next = values[i+1]
        
        if(curr == next):
            return False;
        
        if(direct == 0):
            if(next > curr):
                direct = 1
            else:
                direct = -1
        
        if((next < curr and direct == 1) or (next > curr and direct == -1)):
            return False
            
        if(abs(curr - next) > 3):
            return False
        
        i += 1
    return True



safeCount = 0

# read file
with open('C:/Users/zkraimer/Downloads/AOC_Day2_Input.txt', 'r') as f:
    # split file into lines
    for line in f:
        values = [int(x) for x in line.split()]
        
        if(safe(values)):
            safeCount += 1
        else:
            i = 0
            while i < len(values):
                copyValues = values.copy()
                copyValues.pop(i)
                if(safe(copyValues)):
                    safeCount += 1
                    break;
                i += 1
print(safeCount)