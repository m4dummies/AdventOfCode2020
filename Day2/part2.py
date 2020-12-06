file = open('myfile.txt', 'r')
lines = file.readlines()
count = 0

valid = 0 


for line in lines:
	params = line.strip().split(" ")
	alpha = params[1].replace(":", "")
	mainString = params[2] 
		
	start,end=params[0].split("-")
	
	occur=0
	occur = mainString.count(alpha)
	
	start = int(start) -1
	end = int(end) -1

	gotstart = mainString[int(start)]
	
	if(len(mainString) > end ):
		gotend =mainString[int(end)]
		print('gotend : ',gotend)
	else:
		print("wrong")

	if ((gotstart != gotend) and (gotstart==alpha or gotend==alpha)):
		print("Nice")
		valid=valid+1
	else:
		print("wrong")
	print(valid)