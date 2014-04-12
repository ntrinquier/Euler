file = open('names.txt', 'r')

names = file.readline().split(',')
score = 0
weights = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, '\n': 0}

names.sort()

for index, name in enumerate(names):
	name_weight = 0

	for letter in name:
		name_weight += weights[letter]
	
	score += (index + 1)*name_weight

file.close()

print score
