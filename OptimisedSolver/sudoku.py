# sudoku solver
from math import log2

with open("sample.txt", "r") as file:
    lines = [(line.rstrip('\n')).replace(' ', '') for line in file] # reading all the lines into a list (spaces and \n excluded)
print(lines)

size = (len(lines[0]))
print(size)

candidates = [['' for i in range(size)] for i in range(size)] # initialising a candidates array to store candidates of each X
print(candidates)

# calculating number of unknowns
xCount = 0  
for i in range(size):
    for j in range(size):
        if lines[i][j] == 'X':
            xCount+=1 

while xCount > 0:
    changed = False
    # grouping boxed numbers
    boxes = []
    boxSize = int(log2(size))
    for i in range(0,size,boxSize):
        for j in range(0,size,boxSize):
            box = ''
            for k in range(i,i+boxSize):
                box += lines[k][j:j+boxSize]
            boxes.append(box)
    print(boxes)
                
    for i in range(size):
        for j in range(size):
            if lines[i][j] == 'X':
                for number in range(1,size+1):
                    num = str(number)
                    if num in lines[i]: # checking if in row
                        continue
                    colFlag = 0
                    for k in range(size):
                        if lines[k][j] == num: # checking if in column
                            colFlag = 1
                            break
                    if colFlag == 1:
                        continue
                    # finding out to which box number belongs
                    boxRow = 0
                    for k in range(0,size,boxSize):
                        if (i<k+boxSize) and (i >= k):
                            break
                        boxRow += 1
                    boxCol = 0
                    for k in range(0,size,boxSize):
                        if (j<k+boxSize) and (j >= k):
                            break
                        boxCol += 1
                    if num in boxes[(boxRow*boxSize)+boxCol]:
                        continue
                    candidates[i][j] += num # if number not in row, column, and box, add it to candidates
    for i in range(size):
        for j in range(size):
            if len(candidates[i][j]) == 1: # if only 1 candidate for a specific X, that's the answer
                            lines[i] = lines[i][:j] + candidates[i][j] + lines[i][j+1:]
                            candidates[i][j] = ''
                            xCount -= 1
                            changed = True
            candidates[i][j] = '' # clearing candidates array for next repetition
    if (changed == False) and (xCount > 0):
        break

for i in range(size):
    lines[i] = ' '.join(lines[i])
    lines[i] = lines[i] + '\n'
lines[size-1] = lines[size-1].rstrip('\n')
with open("sample.txt", "a") as file:
    file.write("\n\n")
    file.write("Solution:\n")
    file.writelines(lines)