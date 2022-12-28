# Open the file in read mode
with open("input.txt", "r") as file:
  # Use a for loop to read the lines of the file one by one
	for line in file:
		print(line[0] + line[2])
	
	
