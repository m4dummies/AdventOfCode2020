def makeMap():
	file1 = open('map.txt', 'r') 
	Lines = file1.readlines()  

	count = 0
	block = 0
	treeCount = 0
	linecount = 0
	obstacle = ''
	file_object = open('sevenMap.txt', 'a')
	for line in Lines:
		line=line.strip()

		for x in range(32):
			line=line+line
			print('writng', str(x))
		file_object.write(line+'\r\n')

	file_object.close()

makeMap()