# Open the file in read mode
with open("input.txt", "r") as file:
	totSum = 0
	for line in file:
		roundSum = 0
		if line[2] == 'X':
			#add 3 to round sum for choosing X
			roundSum += 3
			#add three if round end in draw
			if = line[0] == 'X':
				roundSum += 3	
			#
			elif line[0] == 'Z':
				roundSum += 6	

		elif line[2] == 'Y':
			print(line[2] + ": " + "Paper" + "+ 2")
		else:
			print(line[2] + ": " + "Scissors" + "+ 1")

	
