# takes a list of words as an argument and returns the longest word
def longestWord(seq):
	answer = ''
	length = 0
	for word in seq:
		if len(word) > length:
			answer = word
			length = len(word)
	return answer 
