
m = [[0,12,0,0,0,0],[0,26,0,14,0,0],[0,0,0,40,0,0],[0,0,0,17,0,31],[0,9,0,0,0,0],[0,0,0,0,0,85]]
def flatten(input):
	new_list = []
	for i in input:
		for j in i:
			if(j == 0):
				continue
			else:
				new_list.append(j)
	return new_list

print(flatten(m))
print(m)

for i in m:
	print(i)
	