import re
import sys

# checks if s is an in or not
def tryint(s):
    try:
        return int(s)
    except ValueError:
        return s

def alphanum_key(s):
    #  Turn a string into a list of chars and numbers. 
    # like 15B will be ["", "15","B"] 
    return [tryint(c) for c in re.split('([0-9]+)', s)]

colors = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

if(len(sys.argv) != 3):  # checks the number of arguments
    print("the number of arguments is incorrect")
    sys.exit()

# open a file with the name of the first argument given
inputFile = open(sys.argv[1], "r")  

# then add every line in a list
nodesList = []
for elem in inputFile: 
    elem = elem.split()
    nodesList.append(elem)

 # sorts the list by its length
sortedNodes = list(sorted(nodesList, key=len, reverse=True))
# a list to store the result of the coloring
result = [None]*len(sortedNodes)  

# gests every node in the sorted list
for u in range(0, len(sortedNodes)): 
    # a list of available colours
    available = [True]*len(colors)
    node = sortedNodes[u]

    # gests every neighbor for the node
    for i in range(1, len(node)):    
        
        for r in result:
            if (r != None):
                if (int(node[i]) in alphanum_key(r)):
                    c = colors.index(alphanum_key(r)[2])
                    if (available[c] == True):
                        # checks if the color has been used if yes set it as not available
                        available[c] = False
                        break

    # assign the node the first available color
    for c in range(len(colors)-1):
        if (available[c] == True):
            result[u] = node[0] + colors[c]
            break
    
#sort the result by human sort like 1A comes before 10A
result.sort(key=alphanum_key)
# print(result)

# print the result in a new text file
output = open(sys.argv[2], "w")
for elem in result:
    output.write(str(elem) +"\n")
output.close()
inputFile.close()





