firstCol = []
secondCol = []

# read file
with open('C:/Users/zkraimer/Downloads/AOC_Day1_Input.txt', 'r') as f:
    # split file into lines
    for line in f:
    # create two lists of values base on lines
        firstCol.append(int(line.split()[0]))
        secondCol.append(int(line.split()[1]))
        
# value to track total similarity
totalSim = 0

#loop through whole list adding similarity for each value in the first list
for value in firstCol:
    #find count of value in the second list
    count = secondCol.count(value)
    
    totalSim += value * count
    
print(totalSim)
