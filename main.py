def main():
	path = "books/frankenstein.txt"
	with open(path) as book:
		contents = book.read()
		words = word_count(contents)
		chars = char_count(contents)
		print(report(path, words, chars))

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

def report(path, word_count, char_count) -> str:
	report = ""
	report += f"report about book {path}\n\n"
	report += f"the book contains {word_count} words! wow!\n"
	for char, count in sorted(char_count.items(),
                           key=lambda item: item[1],
                           reverse=True):
		report+= f"{char} occurs {count} times.\n"
	report += "the report is done"
	return report


main()