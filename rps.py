# Open the file in read mode
with open("input.txt", "r") as file:
	totSum = 0
	for line in file:
					
		#keep track of round score
		roundSum = 0

		#handle Draw
		if line[0] == 'A' and line[2] == 'X' or \
		   line[0] == 'B' and line[2] == 'Y' or \
		   line[0] == 'C' and line[2] == 'Z':  
			roundSum += 3

		#choose Rock
		if line[2] == 'X':
			#add 1 for Rock
			roundSum += 1

			#Rock beats Scissors
			if line[0] == 'C':
				roundSum += 6	

		#choose Paper
		elif line[2] == 'Y':
			#add 2 for Paper
			roundSum += 2

			#Paper beats Rock	
			if line[0] == 'A':
				roundSum += 6
				
		#choose Scissors
		else:
			#add 3 for Scissors
			roundSum += 3

			#Scissors beat Paper
			if line[0] == 'B':
				roundSum += 6
		

		totSum += roundSum	
	print('Sum: ' + str(totSum))
