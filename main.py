def main():
	path = "books/frankenstein.txt"
	with open(path) as book:
		contents = book.read()
		print_report(path, word_count(contents), char_count(contents))

def word_count(string) -> int:
	return len(string.split())

def char_count(string) -> dict:
	tally = {}
	for char in filter(lambda char: char.isalpha(), string.lower()):
		tally[char] = tally.get(char, 0) + 1
	return tally

def print_report(path, word_count, char_count) -> str:
	print(f"report about book {path}\n")
	print(f"the book contains {word_count} words! wow!")
	for char, count in sorted(char_count.items(),
                           key=lambda item: item[1],
                           reverse=True):
		print(f"{char} occurs {count} times.")
	print("the report is done")

main()