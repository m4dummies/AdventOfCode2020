file = open('myfile.txt', 'r')
lines = file.readlines()
count = 0
valid = 0

for line in lines:
    params = line.strip().split(" ")
    alpha = params[1].replace(":","")
    mainString = params[2]
    start,end=params[0].split("-")
    occur = 0
    occur = mainString.count(alpha)
    start = int(start)
    end = int(end)

    if(occur >= start and occur <= end):
        print("yay")
        valid = valid + 1
    else:
        print("oops")
    print(valid)