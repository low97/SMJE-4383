file_str = input("Open what file: ")
find_line_str = input ("Whuch line (Integer): ")

try:
	input_file = open(file_str)	#potential user error
	find_line_int = int(find_line_str)	#potential user error
	line_count_int = 1
	for line_str in input_file:
		if line_count_int == find_line_int:
			print("line{} of file {} is {}".format(find_line_int, file_str, line_str))
			break
		line_count_int += 1
	else:
		#get here if line sought doesn't exist
		print("line{} of file {} not found".format(find_line_int, file_str))
	input_file.close()
