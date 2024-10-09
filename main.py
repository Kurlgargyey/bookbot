def main():
	with open("books/frankenstein.txt") as f:
		contents = f.read()
		print(contents)
		print(word_count(contents))
		print(char_count(contents))

def word_count(string) -> int:
	return len(string.split())

def char_count(string) -> dict:
	tally = {}
	for char in string.lower():
		if not char.isalpha():
			continue
		if char in tally:
			tally[char] += 1
		else:
			tally[char] = 1
	return tally

main()