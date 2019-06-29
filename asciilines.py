'''create a command-line program that will accept a single .tvg file argument and render the file as ASCII on standard output'''

import sys
import os
import numpy as np


#Update the canvas depending on rendering commands
def changeCanvas(line, canvas, row, column):
  #check if the types of the elements in the rendering comand are correct
  if (type(line[0] is str)) and (type(line[1] is int)) and (type(line[2] is int)) and (line[3] == 'h' or line[3] == 'v') and (type(line[4]) is int) and (line[4] > 0):
    canvas[line[1],line[2]] = line[0] #find the first position to render
    maxColumnInd = column - 1
    maxRowInd = row - 1
    
    #if horizontal line
    if(line[3] == 'h'):
      newInd1 = line[2] + line[4] - 1 #the expected column index after redering
      if newInd1 <= maxColumnInd: #if the index is in the range, update the element one by one
        for i in range(line[2], (newInd1 + 1)):
          canvas[line[1],i] = line[0]
      else: #if the index is out of range, update the elements until the maximum index is met
        for i in range(line[2], (maxColumnInd + 1)):
          canvas[line[1],i] = line[0]

    #if vertical line
    if(line[3] == 'v'):
      newInd2 = line[1] + line[4] - 1 #the expected row index after rendering
      if newInd2 <= maxRowInd: #if the index is in the range, update the element one by one
        for j in range(line[1], (newInd2 + 1)): 
          canvas[j,line[2]] = line[0]
      else: #if the index is out of range, update the elements until the maximum index is met
        for j in range(line[1], (maxRowInd + 1)):
          canvas[j,line[2]] = line[0]
 
  else: 
    print("Invalid rendering command") #if the type of the elements in the rendering command are incorrect, output an error message




#main part

#get the path from the command line
path = sys.argv[1] 

#check if path exists
if os.path.exists(path):
  with open(path, 'r') as f:
    line = f.readline() #read the first line
    line = line.split(" ") #split the items 
    row = line[0] #get the row number
    column = line[1] #get the column number
    row = int(row) #convert to integer type
    column = int(column)
    if(row > 0 and column > 0): #when the canvas size is valid
        canvas = np.chararray((row, column)) 
        canvas[:] = '.' #initialize the canvas 2d array, filled with '.'
        line = f.readline() #read the second line(render command)
        while line: #loop until no more lines
          line = ''.join(line) #convert to string array
          line = line.split(" ")
          line[1] = int(line[1]) #convert special elements to integers 
          line[2] = int(line[2])
          line[4] = int(line[4])
          if(len(line) != 5): #check if the render command length is correct
            print("Invalid length of the rendering command")
            break
          else:
            changeCanvas(line, canvas, row, column)
            line = f.readline() #read another line
        print(canvas)

    else:
      print("Invalid canvas size") #if the canvas size is invalid, output an error message
else:
  print("No such path") #if the path doesn't exist, output an error message


