#Generate hailstone sequence
number_str = input("Enter a positive integer: ")
number = int(number_str)
count = 0

print ("Starting with number : ",number)
print ("Sequence is: ")

while number > 1: #Stop when the sequence reaches 1

	if number%2:
		number = number*3 +1
	else:
		number = number/2
	print(number,",", end=' ') # add number to the sequence

	count += 1

else:
	print () #Blank line for nicer output
	print ("Sequence is ",count,"number long")

