import sys
file1 = open(sys.argv[1], 'r') 
Lines = file1.readlines()  

count = 0
block = 0
treeCount = 0
linecount = 0
obstacle = ''

for line in Lines: 
	print("checking line ",str(linecount))
	obstacle = line[block]
	print("Checking block" ,block)
	print(line[block])
	
	block=block+3	
	linecount=linecount+1

	if obstacle == '#':
		treeCount = treeCount + 1



	print(treeCount)
	