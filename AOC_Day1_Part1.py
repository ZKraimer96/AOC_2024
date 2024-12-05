firstCol = []
secondCol = []

# read file
with open('C:/Users/zkraimer/Downloads/AOC_Day1_Input.txt', 'r') as f:
    # split file into lines
    for line in f:
    # create two lists of values base on lines
        firstCol.append(int(line.split()[0]))
        secondCol.append(int(line.split()[1]))
        
# value to track total difference
totalDif = 0

#loop through whole list adding difference and removing mins as going
while len(firstCol) > 0:
    #find index of smallest value in each list
    firstMin = min(firstCol)
    secondMin = min(secondCol)
    
    totalDif += abs(firstMin - secondMin)
    
    firstCol.remove(firstMin)
    secondCol.remove(secondMin)
    
print(totalDif)
