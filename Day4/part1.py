with open('file.txt') as f:
    lines = f.read()

tests = lines.split("\n\n")

def some():
	first = ['byr','iyr' ,'eyr' ,'hgt' , 'hcl' , 'ecl' ,'pid', 'cid']
	second = ['byr','iyr' ,'eyr' ,'hgt' , 'hcl' , 'ecl' ,'pid']
	par = 0
	count = 0
	for line in lines:
		print(tests[par])
		if all(x in tests[par] for x in first) or all(x in tests[par] for x in second):
			print("yay")
			count = count + 1
			print(count)
		else:
			print("no")
		par = par +1
		print(count)



some()