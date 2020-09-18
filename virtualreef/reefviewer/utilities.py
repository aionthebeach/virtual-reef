
import re

def convertToCamelCase(originalString):
	words = re.findall(r"[\w']+", originalString)
	finalWords = []
	for word in words[1:]:
		finalWords.append(word.capitalize())
	return words[0] + "".join(finalWords)
	