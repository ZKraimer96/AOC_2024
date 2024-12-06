import re

with open('C:/Users/kman9/Coding/AOC_Day3_Input.txt', 'r') as file:
    content = file.read()

pattern = "do\\(\\)|don't\\(\\)|mul\\(\\d*,\\d*\\)"

matches = re.findall(pattern, content)

totalVal = 0

do = True
for match in matches:
    if(match == "do()"):
        do = True
        continue
    elif(match == "don't()"):
        do = False
        continue
    elif(do):
        num1 = ""
        num2 = ""
        i = 0
        while i < len(match) and not match[i].isdigit():
            i += 1
        
        while i < len(match) and match[i].isdigit():
            num1 += match[i]
            i += 1
        
        i += 1
        while i < len(match) and match[i].isdigit():
            num2 += match[i]
            i += 1

        totalVal += int(num1) * int(num2)
        
print(totalVal)