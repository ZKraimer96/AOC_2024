safeCount = 0

# read file
with open('C:/Users/zkraimer/Downloads/AOC_Day2_Input.txt', 'r') as f:
    # split file into lines
    for line in f:
        values = [int(x) for x in line.split()]
        
        prevIndex = 0
        prevLess = True
        prevMore = True
        safe = True
        for value in values[1:]:
            prevValue = values[prevIndex]
            if(prevValue < value and prevLess and (value - prevValue) <= 3):
                prevMore = False
            elif(prevValue > value and prevMore and (prevValue - value) <= 3):
                prevLess = False
            else:
                safe = False
            prevIndex += 1
        if(safe):    
            safeCount += 1
            
            
print(safeCount)