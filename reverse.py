def reverse(input):
	
	# split words of string separated by space
	Words = input.split(" ")

	# reverse list of words
	Words=Words[-1::-1]

	# now join words with space
	rev = ' '.join(Words)
	
	return rev

if __name__ == "__main__":
	input = "the sky is blue"
	print reverse(input)

  
